#include <iostream>
#include <map>

using namespace std;

struct disk_space {
    int id;
    bool is_empty;

    bool id_is(int id) { return !is_empty && this->id == id; }
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
        int id = global_id, i, j = space.size() - 1, x, y, a, b;
        int has_space = true;
        while (id >= 0) {
            // find file
            while (j >= 0 && !space[j].id_is(id)) j--;
            y = j;
            while (y >= 0 && space[y].id_is(id)) y--;
            int file_size = j - y;

            // find remaining space
            i = y;
            has_space = false;
            while (true) {
                while (i >= 0 && !space[i].is_empty) i--;
                if (i < 0) break;
                x = i;
                while (x >= 0 && space[x].is_empty) x--;
                int available_space = i - x;
                if (available_space >= file_size) {
                    has_space = true;
                    a = i + 1;
                    b = x + 1;
                }
                i = x;
            }
            if (has_space) {
                while (j > y && b < a) {
                    swap(space[j--], space[b++]);
                }
            }
            j = y;
            id--;
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