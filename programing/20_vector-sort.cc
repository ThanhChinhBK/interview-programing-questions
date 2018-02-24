#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n,tmp;
  vector<int> arr;
  cin >> n;
  for(int i=0; i < n; i++){
    cin >> tmp;
    arr.push_back(tmp);
  }
  sort(arr.begin(), arr.end());
  for(int i=0; i < n; i++)
    cout << arr[i] << " ";
  return 0;
}
