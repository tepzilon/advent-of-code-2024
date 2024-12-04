#include <iostream>
#include <string>

using namespace std;

int main()
{
  vector<string> grid;
  string line;
  int dir[8][2]={{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1}};
  while(getline(cin, line)) {
    grid.push_back(line);
  }
  int width = grid[0].size();
  int height = grid.size();
  int cnt = 0;
  for(int i = 0; i < height; i++) {
    for(int j = 0; j < width; j++) {
      for (int k = 0; k < 8; k++) {
        int y = i + 3*dir[k][0];
        int x = j + 3*dir[k][1];
        if(y >= 0 && y < height && x >= 0 && x < width) {
          if(grid[i][j] == 'X' && grid[i+dir[k][0]][j+dir[k][1]] == 'M' && grid[i+2*dir[k][0]][j+2*dir[k][1]] == 'A' && grid[i+3*dir[k][0]][j+3*dir[k][1]] == 'S') {
            cnt++;
          }
        }
      }
    }
  }
  cout << cnt << endl;
  return 0;
}