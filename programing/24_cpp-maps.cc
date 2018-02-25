#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
  int n, q, val;
  string key;
  cin >> n;
  map <string, int> mp;
  for(int i = 0; i < n; i++){
    cin >> q >> key;
    if(q==1){
      cin >> val;
      mp[key]+=val;
    }
    else if(q==2)
      mp.erase(key);
    else
      cout << mp[key] << endl;
    
  }
  return 0;
}
