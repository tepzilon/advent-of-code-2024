#include <iostream>
#include <map>
#include <set>

using namespace std;

int width, height;
string line;
map<char, vector<pair<int, int> > > anthenas;
set<pair<int, int> > antinodes;

pair<int, int> vec_inverse(pair<int, int> &v) {
    return make_pair(-v.first, -v.second);
}

pair<int, int> vec_add(pair<int, int> &u, pair<int, int> &v) {
    return make_pair(u.first + v.first, u.second + v.second);
}

pair<int, int> vec_sub(pair<int, int> &u, pair<int, int> &v) {
    auto v_inverse = vec_inverse(v);
    return vec_add(u, v_inverse);
}

bool in_bound(pair<int, int> &u) {
    auto i = u.first;
    auto j = u.second;
    return i >= 0 && i < height && j >= 0 && j < width;
}

int main() {
    while (getline(cin, line)) {
        if (width == 0) {
            width = line.size();
        }
        for (int j = 0; j < width; j++) {
            if (line[j] == '.' || line[j] == '#') {
                continue;
            }
            anthenas[line[j]].push_back(make_pair(height, j));
        }
        height++;
    }
    for (auto &[_, positions] : anthenas) {
        for (int i = 0; i < positions.size(); i++) {
            for (int j = i + 1; j < positions.size(); j++) {
                auto vec_pos_i_to_pos_j = vec_sub(positions[j], positions[i]);
                auto antinode_pos = positions[i];
                while (in_bound(antinode_pos)) {
                    antinodes.insert(antinode_pos);
                    antinode_pos = vec_add(antinode_pos, vec_pos_i_to_pos_j);
                }
                antinode_pos = vec_sub(antinode_pos, vec_pos_i_to_pos_j);
                while (in_bound(antinode_pos)) {
                    antinodes.insert(antinode_pos);
                    antinode_pos = vec_sub(antinode_pos, vec_pos_i_to_pos_j);
                }
            }
        }
    }
    cout << antinodes.size() << "\n";
    return 0;
}