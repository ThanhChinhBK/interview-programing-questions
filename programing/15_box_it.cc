#include <iostream>

using namespace std;

class Box{
private:
  int l=0;
  int b=0;
  int h=0;

public:
  int getLength(){ return l;}
  int getBreadth(){ return b;}
  int getHeight(){return h;}
  long long CalculateVolume() { return (long long) l*b*h;}


  Box(int length, int breadth, int height){
    l=length;
    b=breadth;
    h=height;
  }

  Box(Box& B){
    l=B.getLength();
    b=B.getBreadth();
    h=B.getHeight();

  }
    
  Box(){}

  ~Box(){
  }

  bool operator<(Box &B){
    int ll=B.getLength();
    int bb=B.getBreadth();
    int hh=B.getHeight();
    if(l < ll || (b < bb && l==ll) || (h < hh && b==bb && l==ll))
      return true;
    else
      return false;
  }

  

};

ostream& operator<<(ostream& out, Box B){
    return out<<B.getLength()<<' '<<B.getBreadth()<<' '<<B.getHeight();
}

void check2(){
  int n;
  cin>>n;
  Box temp;
  for(int i=0;i<n;i++){
    int type;
    cin>>type;
    if(type ==1){
      cout<<temp<<endl;
    }
    if(type == 2){
      int l,b,h;
      cin>>l>>b>>h;
      Box NewBox(l,b,h);
      temp=NewBox;
      cout<<temp<<endl;
    }
    if(type==3){
      int l,b,h;
      cin>>l>>b>>h;
      Box NewBox(l,b,h);
      if(NewBox<temp){
        cout<<"Lesser\n";
      }
      else{
        cout<<"Greater\n";
      }
    }
    if(type==4){
      cout<<temp.CalculateVolume()<<endl;
    }
    if(type==5){
      Box NewBox(temp);
      cout<<NewBox<<endl;
    }
  }
}

int main(){
  check2();
}
