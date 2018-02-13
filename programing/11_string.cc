#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
  string a,b,c;
  char ch;
  cin >> a >> b;
  c = a + b;
  cout << a.length() << " " << b.length() << endl;
  cout << c << endl;
  ch = a[0];
  a[0] = b[0];
  b[0] = ch;
  cout << a << " " << b << endl;
  return 0;
}
