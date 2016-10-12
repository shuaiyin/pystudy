#include<iostream>
#include<string.h>
#include<vector>
using namespace std; 


int main(){
  //first define way 
  vector<int> v;
  for(int i=0;i<10;i++){
    v.push_back(i);
    cout << "the size of " << v.size() <<"\n"; 
   
  }
  for(int i=0;i<10;i++){
     cout << v[i];
     break;
  }
 
 
  return 0;
}
