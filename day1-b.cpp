#include <iostream>
#include <sstream>
#include <vector>
#include <cassert>
#include <map>

using namespace std;

int main()
{
  string line;
  vector<int> list_a;
  map<int, int> bucket;
  while (getline(cin, line))
  {
    stringstream ss(line);
    int a, b;
    ss >> a >> b;
    list_a.push_back(a);
    if (bucket.find(b) == bucket.end())
    {
      bucket[b] = 1;
    }
    else
    {
      bucket[b]++;
    }
  }
  int total = 0;
  for (auto a : list_a)
  {
    if (bucket.find(a) != bucket.end())
    {
      total += a * bucket[a];
    }
  }
  cout << total << endl;
}