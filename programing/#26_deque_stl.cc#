#include <iostream>
#include <algorithm>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
  deque <int> deq;
  for(int i=0;i<n;i++){
    while(!deq.empty() && arr[i] > deq.back()) deq.pop_back(); //deq.front() is always maximum element 
    deq.push_back(arr[i]);
    if(i >= k && arr[i-k] == deq.front()) deq.pop_front();
    if(i >= k-1) printf(i < n-1? "%d ":"%d\n", deq.front());
  }
}

int main(){
  
  int t;
  cin >> t;
  while(t>0) {
    int n,k;
    cin >> n >> k;
    int i;
    int arr[n];
    for(i=0;i<n;i++)
      cin >> arr[i];
    printKMax(arr, n, k);
    t--;
  }
  return 0;
}
