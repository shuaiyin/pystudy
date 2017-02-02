//LeetCode,Remove Duplicates from Sorted Array
#include<iostream>
#include<vector>
using namespace std;
class Solution{
public:
   int removeDuplicates(vector<int> & nums){
      if(nums.empty()) return 0;
      int index =0;
      for(int i=1;i<nums.size();i++){
           if(nums[index] != nums[i])
		 nums[++index]=nums[i];
    
      } 
      return index +1;


   };
};
int main(){
   
   vector<int> v(10,-1);
   //init a vector with the ten -1 same element 
   cout << v;
   return 0;
   Solution so = Solution();
   cout << so.removeDuplicates(v) << endl;
   return 0;
}
