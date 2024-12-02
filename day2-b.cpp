#include <iostream>
#include <sstream>
#include <string>

using namespace std;

bool is_safe(vector<int> &v)
{
  int len = v.size();
  bool is_asc;
  for (int i = 1; i < len; i++)
  {
    int diff = v[i] - v[i - 1];
    if (diff < -3 || diff == 0 || diff > 3)
    {
      return false;
    }
    if (i == 1)
    {
      is_asc = diff > 0;
    }
    else if (is_asc && diff < 0 || !is_asc && diff > 0)
    {
      return false;
    }
  }
  return true;
}

vector<int> removed_index(vector<int> v, int index)
{
  v.erase(v.begin() + index);
  return v;
}

int main()
{
  string line;
  int cnt = 0;
  while (getline(cin, line))
  {
    stringstream ss(line);
    string s;
    vector<int> v;
    while (getline(ss, s, ' '))
    {
      int num = stoi(s);
      v.push_back(num);
    }
    int len = v.size();
    for (int i = 0; i < len; i++)
    {
      vector<int> v_removed = removed_index(v, i);
      if (is_safe(v_removed))
      {
        cnt++;
        break;
      }
    }
  }
  cout << cnt << endl;
  return 0;
}