#include <iostream>

using namespace std;

struct disk_space {
    int id;
    bool is_empty;
};

disk_space new_space() { return {0, true}; }

disk_space new_file(int id) { return {id, false}; }

struct disk {
    bool is_space;
    int global_id;
    vector<disk_space> space;

    disk() {
        is_space = false;
        global_id = 0;
        space.clear();
    }

    void read() {
        char c;
        while (cin.get(c)) {
            int times = c - '0';
            for (int i = 0; i < times; i++) {
                if (is_space) {
                    space.push_back(new_space());
                } else {
                    space.push_back(new_file(global_id));
                }
            }
            if (is_space) {
                global_id++;
            }
            is_space = !is_space;
        }
    }

    void compact() {
        int i = 0, j = space.size() - 1;
        while (true) {
            while (i < space.size() && !space[i].is_empty) i++;
            while (j >= 0 && space[j].is_empty) j--;
            if (i >= j) break;
            if (i < space.size() && space[i].is_empty && j >= 0 &&
                !space[j].is_empty) {
                swap(space[i], space[j]);
            }
        }
    }

    void debug() {
        for (int i = 0; i < space.size(); i++) {
            if (space[i].is_empty)
                cout << ".";
            else
                cout << space[i].id;
        }
        cout << "\n";
    }

    long long checksum() {
        long long sum = 0;
        for (int i = 0; i < space.size(); i++) {
            sum += i * space[i].id;
        }
        return sum;
    }
};

int main() {
    auto d = disk();
    d.read();
    d.compact();
    // d.debug();
    cout << d.checksum() << "\n";
    return 0;
}