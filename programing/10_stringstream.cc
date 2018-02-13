#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
  stringstream ss;
  vector<int> res;
  int temp;
  char ch;
  ss << str;
  while(!ss.eof()){
    ss >> temp >> ch;
    res.push_back(temp);
  }
  return res;
}

int main() {
  string str;
  cin >> str;
  vector<int> integers = parseInts(str);
  for(int i = 0; i < integers.size(); i++) {
    cout << integers[i] << "\n";
  }
  
  return 0;
}
