#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n,p,a,b, tmp;
  vector<int> arr;
  cin >> n;
  for(int i=0; i < n; i++){
    cin >> tmp;
    arr.push_back(tmp);
  }
  cin >> p;
  arr.erase(arr.begin() + p-1);
  cin >> a;
  cin >> b;
  arr.erase(arr.begin() + a-1, arr.begin() + b-1);
  cout << arr.size() << endl;
  for(int i=0; i < arr.size(); i++)
    cout << arr[i] << " ";
  return 0;
}
