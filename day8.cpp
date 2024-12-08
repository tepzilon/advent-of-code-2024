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
    for (auto &[c, positions] : anthenas) {
        for (int i = 0; i < positions.size(); i++) {
            for (int j = i + 1; j < positions.size(); j++) {
                auto vec_pos_i_to_pos_j = vec_sub(positions[j], positions[i]);
                auto antinode_pos_1 = vec_add(positions[j], vec_pos_i_to_pos_j);
                if (in_bound(antinode_pos_1)) {
                    antinodes.insert(antinode_pos_1);
                }
                auto vec_pos_j_to_pos_i = vec_sub(positions[i], positions[j]);
                auto antinode_pos_2 = vec_add(positions[i], vec_pos_j_to_pos_i);
                if (in_bound(antinode_pos_2)) {
                    antinodes.insert(antinode_pos_2);
                }
            }
        }
    }
    cout << antinodes.size() << "\n";
    return 0;
}