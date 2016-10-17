#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int  arr[] = {1,4,78,2,55,69,456};
  vector<int> avet(arr,arr+5);
  sort(avet.begin(),avet.end());
  for(vector<int>::const_iterator iter = avet.begin(); iter != avet.end(); ++iter){
     cout << *iter << endl;
  }

}
