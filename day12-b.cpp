#include <iostream>
#include <set>

#define X first
#define Y second

using namespace std;


string line;
int width, height, perimeter, area;
long long int sum;
bool visited[1005][1005], roi[1005][1005];
char grid[1005][1005];
set<pair<int,int> >region;
int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

void dfs(int i, int j) {
    if(visited[i][j]) return;
    visited[i][j] = true;
    roi[i][j] = true;
    region.insert(make_pair(i, j));
    area++;
    for(int k = 0; k < 4; k++) {
        int ni = i + dir[k][0];
        int nj = j + dir[k][1];
        if(ni >= 1 && ni <= height && nj >= 1 && nj <= width && !visited[ni][nj] && !roi[ni][nj] && grid[ni][nj] == grid[i][j]) {
            dfs(ni, nj);
        }
    }
}

int main() {
    while(getline(cin, line)) {
        if(width == 0) {
            width = line.size();
        }
        height++;
        for(int i = 0; i < width; i++) {
            grid[height][i+1] = line[i];
        }
    }
    for(int i = 1; i <= height; i++) {
        for(int j = 1; j <= width; j++) {
            if(!visited[i][j]) {
                perimeter = 0;
                area = 0;
                dfs(i, j);
                for(auto p : region) {
                    for(int k = 0; k < 4; k++) {
                        int next_k = (k + 1) % 4;
                        int ai = p.X + dir[k][0];
                        int aj = p.Y + dir[k][1];
                        int bi = p.X + dir[next_k][0];
                        int bj = p.Y + dir[next_k][1];
                        int ci = p.X + dir[k][0] + dir[next_k][0];
                        int cj = p.Y + dir[k][1] + dir[next_k][1];
                        if((!roi[ai][aj] && !roi[bi][bj]) || (roi[ai][aj] && roi[bi][bj] && !roi[ci][cj])) {
                            perimeter++;
                        }
                    }
                }
                sum += (long long int )area * (long long int )perimeter;
                for(auto p : region) {
                    roi[p.X][p.Y] = false;
                }
                region.clear();
            }
        }
    }
    cout << sum << "\n";
    return 0;
}