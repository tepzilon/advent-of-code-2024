#include <iostream>
#include <string>

using namespace std;

enum State {
  expect_m = 0,
  expect_u = 1,
  expect_l = 2,
  expect_lparen = 3,
  expect_digit_a = 4,
  expect_digit_b = 5,
};

int main() {
  char c;
  int state = expect_m;
  int sum = 0;
  int cnt = 0;
  bool read_digit_ok = false;
  string a, b;
  while(cin.get(c)) {
    switch(state) {
      case expect_m:
        if(c == 'm') {
          state = expect_u;
        }
        break;
      case expect_u:
        if(c == 'u') {
          state = expect_l;
        } else {
          state = expect_m;
        }
        break;
      case expect_l:
        if(c == 'l') {
          state = expect_lparen;
        } else {
          state = expect_m;
        }
        break;
      case expect_lparen:
        if(c == '(') {
          state = expect_digit_a;
          a = "";
        } else {
          state = expect_m;
        }
        break;
      case expect_digit_a:
        if (isdigit(c)) {
          a += c;
        } else if(c == ',') {
          state = expect_digit_b;
          b = "";
        } else {
          state = expect_m;
        }
        break;
      case expect_digit_b:
        if (isdigit(c)) {
          b += c;
        } else if(c == ')') {
          sum += stoi(a) * stoi(b);
          state = expect_m;
        } else {
          state = expect_m;
        }
        break;
    }
  }
  cout << sum << "\n";
}