#pragma once 

#include "utils.hpp"

namespace AlgoComp {

  class InputChangeListener {
  public:
    virtual ~InputChangeListener ( ) { };

    virtual double OnInputChange ( unsigned int input_index_, double input_value_ ) = 0;
  };


  class OutputChangeListener {
  public:
    virtual ~OutputChangeListener ( ) { };

    virtual void OnOutputChange ( double _new_out_value_ ) = 0;
  };


  class TertiaryRandomForest : public InputChangeListener {
  public:
    Forest * t_forest; // this is the forest datastructure we are using now
    OutputChangeListener * _output_listener_; 
    std::vector<double> current_predictor_value_vec_;
    // std::vector<double> forest_output_vec_; // this is the output of each tree in the forest
    double forest_output_;

    TertiaryRandomForest ( )
      : t_forest(nullptr),
	_output_listener_(nullptr),
	current_predictor_value_vec_(),
	forest_output_(0)
    {
    }
    
    //Will be called for initializing the Forest object
    //Can use Forest Class in utils.hpp to parse the forestfile
    void InitializeForest ( const char * const forest_filename_ ) {
      t_forest = new Forest(forest_filename_);
      current_predictor_value_vec_.resize(t_forest->num_predictors_, 0);
    }

    #define ONE_OR_ZERO 1
    
    double GetValue ( const Tree & tree, const Node & node ) {
      if ( !node.is_leaf_) {
        if ( current_predictor_value_vec_[node.predictor_index_ - ONE_OR_ZERO] < node.boundary_value_vec_[0]) {
          return GetValue ( tree, tree[node.child_node_index_vec_[0]] );
        }
        else if ( ( current_predictor_value_vec_[node.predictor_index_ - ONE_OR_ZERO] <= node.boundary_value_vec_[1] ) &&
                  ( current_predictor_value_vec_[node.predictor_index_ - ONE_OR_ZERO] >= node.boundary_value_vec_[0] ) ) {
          return GetValue ( tree, tree[node.child_node_index_vec_[1]] );
        }
        else {
          return GetValue ( tree, tree[node.child_node_index_vec_[2]] );
        }
      }
      else {
	return node.predicted_value_;
      }
    }
    
    //Will be called to notfiy changes in predictor values
    //Should return the updated output value
    double OnInputChange ( unsigned int input_index_, double input_value_ ) {
      current_predictor_value_vec_[input_index_ - ONE_OR_ZERO] = input_value_;
      forest_output_ = 0;
      for (const Tree & tree : t_forest->tree_vec_) {
	forest_output_ += GetValue ( tree, tree[0] );
      }
      forest_output_ /= (double)t_forest->tree_vec_.size();
      _output_listener_->OnOutputChange(forest_output_);
      return forest_output_;
    }
    
    //_new_listener_ shoud be notified by calling _new_listener_->OnOutputChange on every change in Forest Output
    //should return true if _new_listener_ is successfully subscribed to Forest output updates
    bool SubscribeOutputChange ( OutputChangeListener * _new_listener_ ) {
      _output_listener_ = _new_listener_;
      return true;
    }
  };

}
