#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
  Node* next;
  Node* prev;
  int value;
  int key;
  Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
  Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
protected: 
  map<int,Node*> mp; //map the key to the node in the linked list
  int cp;  //capacity
  Node* tail; // double linked list tail pointer
  Node* head; // double linked list head pointer
  virtual void set(int, int) = 0; //set function
  virtual int get(int) = 0; //get function

};

class LRUCache : public Cache {

public:
  LRUCache(int n){ 
    cp=n;
    tail = head = NULL;
  } 

  void set(int key, int value){
    if(mp.count(key)==0){      
      Node *tmp = new Node(key, value);
      if(mp.size()==0){
        head = tail = tmp;
        tail->prev = head;
        head->next = tail;
      }
      else {
        if(mp.size()==cp){
          Node *cur_tail = tail;
          tail = cur_tail-> prev;
          mp.erase(cur_tail->key);
          free(cur_tail);
        }
        tail->next = tmp;
        tmp -> prev = tail;
        head -> prev = tmp;
        tmp -> next = head;
        head = tmp;
      }
      mp[key] = tmp;
    }
    else{
      Node *tmp = mp[key];
      tmp -> value = value;
      tmp->prev->next = tmp->next;
      tmp->next->prev = tmp->prev;
      tmp->next = head;
      head->prev = tmp;
      tmp-> prev = tail;
      tail -> next = tmp;
      head = tmp;
    }
  }

  int get(int key) {
    if (mp.count(key) == 0) return -1;
        return mp[key]->value;
    }
};

int main() {
  int n, capacity,i;
  cin >> n >> capacity;
  LRUCache l(capacity);
  for(i=0;i<n;i++) {
    string command;
    cin >> command;
    if(command == "get") {
      int key;
      cin >> key;
      cout << l.get(key) << endl;
    } 
    else if(command == "set") {
      int key, value;
      cin >> key >> value;
      l.set(key,value);
    }
  }
  return 0;
}
