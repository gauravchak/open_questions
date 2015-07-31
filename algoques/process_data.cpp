#include "utils.hpp"
#include "tertiary_random_forest.hpp"

class OutputDumper : public AlgoComp::OutputChangeListener
{
 private:
  std::ofstream outputdatafile_;
  unsigned int samplingrate_;
  unsigned int samplingcounter_;
  AlgoComp::cyclecount_t total_dump_time_;

 public:
  OutputDumper ( const std::string & _dumpfilename_ , unsigned int _samplingrate_ )
      : samplingrate_(_samplingrate_) , samplingcounter_(0u) , total_dump_time_(0)
  {
	outputdatafile_.open ( _dumpfilename_.c_str(), std::ios::out|std::ios::binary ) ;
    if ( ! outputdatafile_.is_open() )
    {
      std::cerr << "ERROR: Cannot open " << _dumpfilename_ << " for writing." << std::endl;
      exit ( 0 ) ;
    }
  }

  ~OutputDumper ()
  {
    outputdatafile_.close();
  }

  void OnOutputChange ( double _new_out_value_ ) 
  {
      
    AlgoComp::cyclecount_t prev_call_ = AlgoComp::GetCpucycleCount();
    samplingcounter_ ++;
    if ( samplingcounter_ >= samplingrate_ )
    {
      outputdatafile_ << _new_out_value_ << std::endl;
      samplingcounter_ = 0;
    }
    AlgoComp::cyclecount_t after_call_ = AlgoComp::GetCpucycleCount();
    total_dump_time_ += (after_call_-prev_call_);
  }

  AlgoComp::cyclecount_t GetDumpTime() { return total_dump_time_; }
};

int main ( int argc, char ** argv )
{
  if ( argc < 3 )
  {
    std::cerr << "Usage:: forestfile inputdatafile outputdatafile [samplingrate=1000]" << std::endl;
    exit ( 0 );
  }

  std::string forest_filename_ = std::string ( argv[1] );
  std::string inputdatafilename_ = std::string ( argv[2] );
  std::string outputdatafilename_ = std::string ( argv[3] );
  unsigned int samplingrate_ = 1000u;
  if ( argc > 4 ) { 
    samplingrate_ = std::max ( 1, atoi ( argv[4] ) ) ;
  }

  std::ifstream inputdatafile_;
  inputdatafile_.open ( inputdatafilename_.c_str(), std::ifstream::in ) ;
  if ( ! inputdatafile_.is_open() )
  {
    std::cerr << "ERROR: Cannot open " << inputdatafilename_ << " for reading." << std::endl;
    exit ( 0 ) ;
  }


  const int kDataLineBufferLen = 1024 ;
  char readline_buffer_ [ kDataLineBufferLen ];
  memset ( readline_buffer_, '\0', kDataLineBufferLen );

  AlgoComp::cyclecount_t total_time_taken_ = 0;

  AlgoComp::TertiaryRandomForest tertiary_random_forest_;
  tertiary_random_forest_.InitializeForest ( forest_filename_.c_str() );

  OutputDumper dumper_(outputdatafilename_, samplingrate_);
  tertiary_random_forest_.SubscribeOutputChange(&dumper_);

  std::vector < double > last_indicator_values_ ;

  while ( inputdatafile_.good ( ) )
  {
    memset ( readline_buffer_, '\0', kDataLineBufferLen );
    inputdatafile_.getline ( readline_buffer_, kDataLineBufferLen ) ;
    AlgoComp::PerishableStringTokenizer st_ ( readline_buffer_, kDataLineBufferLen );
    const std::vector < const char * > & tokens_ = st_.GetTokens ( );
    if ( tokens_.size ( ) < 2 )
      continue;

    double base_price_ = atof ( tokens_[1] ); // the real target price is sum of base_price and forest_delta_value_
    if ( last_indicator_values_.empty ( ) )
    {
      for ( unsigned int i = 2u; i < tokens_.size (); i ++ )
      {
        last_indicator_values_.push_back ( atof ( tokens_[i] ) ) ;
      }
    }

    for ( unsigned int i = 2u; i < tokens_.size (); i ++ )
    {
      last_indicator_values_[i-2u] = atof ( tokens_[i] ) ;
      // As of now, calling OnInputChange for every variable change
      // Later we can change this to only significant changes only
      // Perhaps calculation of what is a significant change is best done inside the TertiaryRandomForest ?
      AlgoComp::cyclecount_t prev_call_ = AlgoComp::GetCpucycleCount();
      double forest_delta_value_ = tertiary_random_forest_.OnInputChange ( i-1u, last_indicator_values_[i-2u] ) ;
      AlgoComp::cyclecount_t after_call_ = AlgoComp::GetCpucycleCount();
      total_time_taken_ += ( after_call_ - prev_call_ );
    }
  }

  std::cout << "Outputfile: " << outputdatafilename_ << " written. " << std::endl;
  std::scientific;
  std::cout << "Computation cycles: "<< 1.0*(total_time_taken_ - dumper_.GetDumpTime()) << std::endl;
  std::cout << "Printing cycles: " << 1.0*(dumper_.GetDumpTime()) << std::endl;
}
