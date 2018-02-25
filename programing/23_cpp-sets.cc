#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
  set<int> arr;
  int n, q, val;
  set<int> :: iterator itr;
  cin >> n;
  for(int i=0; i < n; i++){
    cin >> q >> val;
    if(q==1)
      arr.insert(val);
    else if(q==2)
      arr.erase(val);
    else{
      itr = arr.find(val);
      if(itr==arr.end())
        cout << "No" << endl;
      else
        cout << "Yes" << endl;
    }
  }
  return 0;
}
