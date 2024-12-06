#include <iostream>
#include <cassert>

using namespace std;

int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
bool is_obstacle[1000][1000];
bool visited[1000][1000];
bool visited_with_dir[1000][1000][4];
int width, height;
int start_i, start_j;
int cur_i, cur_j, cur_dir, next_i, next_j;
int cnt;
string line;

bool in_bound(int i, int j)
{
  return i >= 0 && i < height && j >= 0 && j < width;
}

int main()
{
  while (getline(cin, line))
  {
    if (width == 0 && line.size() > 0)
    {
      width = line.size();
    }
    for (int j = 0; j < width; j++)
    {
      is_obstacle[height][j] = line[j] == '#';
      if (line[j] == '^')
      {
        start_i = height;
        start_j = j;
      }
    }
    height++;
  }
  cur_i = start_i;
  cur_j = start_j;
  cur_dir = 0;
  while (true)
  {
    if(!visited[cur_i][cur_j]) {
      cnt++;
    }
    visited[cur_i][cur_j] = true;
    assert(!visited_with_dir[cur_i][cur_j][cur_dir]);
    visited_with_dir[cur_i][cur_j][cur_dir] = true;
    next_i = cur_i + dir[cur_dir][0];
    next_j = cur_j + dir[cur_dir][1];
    if (in_bound(next_i, next_j))
    {
      if (is_obstacle[next_i][next_j])
      {
        cur_dir = (cur_dir + 1) % 4;
      }
      else
      {
        cur_i = next_i;
        cur_j = next_j;
      }
    }
    else
    {
      break;
    }
  }
  cout << cnt << "\n";
  return 0;
}