#include <condition_variable>
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

condition_variable cv;
mutex m;

int val = 0;
void add(int num)
{
  lock_guard<mutex> lock(m);
  val += num;
  cout << "add: " << val << endl;
  cv.notify_one();
}

void sub(int num)
{
  unique_lock<mutex> ulock(m);
  cv.wait(ulock, []{return (val != 0) ? true : false;});
  if(val >= num) {
    val -= num;
    cout << "sub: " << val << endl;
  }
  else {
    cout << "sub: " << "not enough" << endl;
  }
}

int main()
{
  thread t1(sub, 5);
  thread t2(add, 10);
  
}