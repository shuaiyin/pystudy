#include<iostream>
#include<string.h>
#include<vector>
using namespace std; 


int main(){

  // vector<char> testvector = {'a','b','c','d'};

  //first define way 
  int init_arr[] = {2,25,20,8,9,50};
  init_arr[6] = 5555;
  int arr_len = sizeof(init_arr)/sizeof(int);
  cout << arr_len << endl;
  cout << *(init_arr+6) << endl;
  cout << sizeof(init_arr) << endl;
  return 0;
  vector<int> init_vector(init_arr,init_arr+arr_len);
  vector<int>::iterator  iter = init_vector.begin();
  vector<int>:: iterator new_iter =   init_vector.erase(iter); 
  cout << *new_iter <<endl;
  return 0;
  while(iter != init_vector.end()){
     cout << *iter++ << endl;
  }
  
 
 
  return 0;
}
