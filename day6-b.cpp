#include <iostream>
#include <stack>

using namespace std;

struct History {
  int i;
  int j;
  int dir;
};

int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
bool is_obstacle[1000][1000];
bool visited_with_dir[1000][1000][4];
bool is_infinit_loop;
int width, height, start_i, start_j, cur_i, cur_j, cur_dir, next_i, next_j, cnt;
string line;
stack<History>history;

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
  for (int extra_obst_i = 0; extra_obst_i < height; extra_obst_i++)
  {
    for (int extra_obst_j = 0; extra_obst_j < width; extra_obst_j++)
    {
      if (is_obstacle[extra_obst_i][extra_obst_j])
      {
        continue;
      }
      is_obstacle[extra_obst_i][extra_obst_j] = true;

      cur_i = start_i;
      cur_j = start_j;
      cur_dir = 0;
      is_infinit_loop = false;
      while(!history.empty()) {
        History top_stack_hist = history.top();
        history.pop();
        visited_with_dir[top_stack_hist.i][top_stack_hist.j][top_stack_hist.dir] = false;
      }
      while (true)
      {
        if (visited_with_dir[cur_i][cur_j][cur_dir])
        {
          is_infinit_loop = true;
          break;
        }
        visited_with_dir[cur_i][cur_j][cur_dir] = true;
        History new_history = {cur_i, cur_j, cur_dir};
        history.push(new_history);
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
      if (is_infinit_loop)
      {
        cnt++;
      }

      is_obstacle[extra_obst_i][extra_obst_j] = false;
    }
  }
  cout << cnt << "\n";
  return 0;
}