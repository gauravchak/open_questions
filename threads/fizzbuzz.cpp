// constructing atomics
#include <iostream> // std::cout
#include <atomic>   // std::atomic, std::atomic_flag, ATOMIC_FLAG_INIT
#include <thread>   // std::thread, std::this_thread::yield
#include <vector>   // std::vector
#include <chrono>

std::atomic<int> cur_num;

class Myprinter
{
  private:
    int max_num;
    bool div3;
    bool div5;
    const char *gstr;

  public:
    Myprinter(int _max_num, bool _div3, bool _div5, const char *_gstr)
        : max_num(_max_num), div3(_div3), div5(_div5), gstr(_gstr)
    {
    }

    void operator()()
    {
        while (cur_num < max_num)
        {
            if (cur_num % 15 == 0)
            {
                if (div3 && div5)
                {
                    std::cout << " " << cur_num << gstr;
                    cur_num++;
                }
            }
            else if (cur_num % 5 == 0)
            {
                if (div5 && !div3)
                {
                    std::cout << " " << cur_num << gstr;
                    cur_num++;
                }
            }
            else if (cur_num % 3 == 0)
            {
                if (div3 && !div5)
                {
                    std::cout << " " << cur_num << gstr;
                    cur_num++;
                }
            }
            else
            {
                if (!(div3 || div5))
                {
                    std::cout << " " << cur_num++;
                }
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }
};

int main()
{
    cur_num = 1;
    int max_num = 30;
    Myprinter m1(max_num, false, false, nullptr);
    Myprinter m3(max_num, true, false, "Fizz");
    Myprinter m5(max_num, false, true, "Buzz");
    Myprinter m15(max_num, true, true, "Fizzbuzz");

    std::thread thread_num(m1);
    std::thread thread_3_only(m3);
    std::thread thread_5_only(m5);
    std::thread thread_15(m15);

    thread_num.join();
    thread_3_only.join();
    thread_5_only.join();
    thread_15.join();
    std::cout << std::endl;
    return 0;
}