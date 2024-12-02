#include <iostream>
#include <sstream>
#include <vector>
#include <cassert>

using namespace std;

int main()
{
  string line;
  vector<int> list_a, list_b;
  while (getline(cin, line))
  {
    stringstream ss(line);
    int a, b;
    ss >> a >> b;
    list_a.push_back(a);
    list_b.push_back(b);
  }
  sort(list_a.begin(), list_a.end());
  sort(list_b.begin(), list_b.end());
  assert(list_a.size() == list_b.size());
  int len = list_a.size();
  int total = 0;
  for (int i = 0; i < len; i++)
  {
    total += abs(list_a[i] - list_b[i]);
  }
  cout << total << endl;
}