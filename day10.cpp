#include <iostream>

using namespace std;

int grid[500][500];
bool visited[500][500];
int width, height, sum;
int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
string line;
vector<pair<int, int> > nines;
queue<pair<int, int> > q;
stack<pair<int, int> > history;

int main() {
    while (getline(cin, line)) {
        if (width == 0) width = line.size();
        for (int i = 0; i < width; i++) {
            grid[height][i] = line[i] - '0';
            if (grid[height][i] == 9) {
                nines.push_back(make_pair(height, i));
            }
        }
        height++;
    }
    for (auto nine : nines) {
        q.push(nine);
        while (!q.empty()) {
            auto now = q.front();
            q.pop();
            int now_i = now.first;
            int now_j = now.second;
            if (visited[now_i][now_j]) {
                continue;
            }
            visited[now_i][now_j] = true;
            history.push(make_pair(now_i, now_j));
            if (grid[now_i][now_j] == 0) {
                sum++;
            }
            for (int k = 0; k < 4; k++) {
                int next_i = now_i + dir[k][0];
                int next_j = now_j + dir[k][1];
                if (next_i >= 0 && next_i < height && next_j >= 0 &&
                    next_j < width && !visited[next_i][next_j] &&
                    grid[next_i][next_j] == grid[now_i][now_j] - 1) {
                    q.push(make_pair(next_i, next_j));
                }
            }
        }
        while (!history.empty()) {
            auto top = history.top();
            history.pop();
            visited[top.first][top.second] = false;
        }
    }
    cout << sum << "\n";
    return 0;
}