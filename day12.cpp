#include <iostream>

using namespace std;

vector<string>grid;
string line;
int width, height, perimeter, area, sum;
int visited[1005][1005];
int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};


void dfs(int i, int j) {
    area++;
    for(int k = 0; k < 4; k++) {
        int ni = i + dir[k][0];
        int nj = j + dir[k][1];
        if(ni < 0 || ni >= height || nj < 0 || nj >= width ||  grid[ni][nj] != grid[i][j]) {
            perimeter++;
        }
        if(ni >= 0 && ni < height && nj >= 0 && nj < width && !visited[ni][nj] && grid[ni][nj] == grid[i][j]) {
            visited[ni][nj] = true;
            dfs(ni, nj);
        }
    }
}

int main() {
    while(getline(cin, line)) {
        grid.push_back(line);
        if(width == 0) {
            width = line.size();
        }
        height++;
    }
    for(int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++) {
            if(!visited[i][j]) {
                perimeter = 0;
                area = 0;
                visited[i][j] = true;
                dfs(i, j);
                sum += perimeter * area;
            }
        }
    }
    cout << sum << "\n";
    return 0;
}