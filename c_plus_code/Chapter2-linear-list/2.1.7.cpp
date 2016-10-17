#include <iostream>
// #include<tr1/unordered_map>
// using namespace std;
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;
/*
using a hash table to save the index of each num 
time complexiyy O(n) 
space complexity O(n)

*/
class Solution{
public:
    vector<int> twoSum(vector<int> &nums, int target){
      unordered_map<int,int> mapping;
      vector<int> result;
      for(int i=0;i<nums.size();i++){
        mapping[nums[i]] = i;
      }
      for(int i=0;i<nums.size();i++){
          const int gap = target - nums[i];
          cout << "the gap is " << gap << endl;
          //题目当中提到了index1 is not less than index2   !=
          if(mapping.find(gap) != mapping.end() && mapping[gap] != i){
             result.push_back(i+1);
	           result.push_back(mapping[gap] +1);
             break;
          }
      }
      return result;
    }





};

int main(){
 vector<int> v;
 for(vector<int>::size_type ix=0;ix <= 10; ix++){
   v.push_back(ix);
 }
for(vector<int>::const_iterator it = v.begin(); it!= v.end(); ++it){
   cout << *it << endl;
}
cout << "another way to iter below : " << endl;
for(int i=0;i<v.size();i++){
  cout << v[i] << endl;
}
 Solution so = Solution();
 vector<int> result = so.twoSum(v,3);
 return 0;
 // cout << "first index is " << result[0] << "second index is " << result[1];


  return 0;
}


////g++ -std=c++0x 2.1.7.cpp   you should add a compiler option 