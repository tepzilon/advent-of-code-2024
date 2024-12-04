#include <iostream>
#include <string>

using namespace std;

int main()
{
  vector<string> grid;
  string line;
  while(getline(cin, line)) {
    grid.push_back(line);
  }
  int width = grid[0].size();
  int height = grid.size();
  int cnt = 0;
  for(int i = 1; i < height-1; i++) {
    for(int j = 1; j < width-1; j++) {
      if(grid[i][j] == 'A') {
        bool ok1 = false, ok2 = false;
        if((grid[i-1][j-1] == 'M' && grid[i+1][j+1] == 'S') || (grid[i-1][j-1] == 'S' && grid[i+1][j+1] == 'M')) {
          ok1 = true;
        }
        if((grid[i-1][j+1] == 'M' && grid[i+1][j-1] == 'S') || (grid[i-1][j+1] == 'S' && grid[i+1][j-1] == 'M')) {
          ok2 = true;
        }
        if(ok1 && ok2) {
          cnt++;
        }
      }
    }
  }
  cout << cnt << endl;
  return 0;
}