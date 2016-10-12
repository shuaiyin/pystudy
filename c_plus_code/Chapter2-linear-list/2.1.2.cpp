//leetcode,Remove Duplicates from Sorted Array II 
#include<iostream>
#include<vector>
using namespace std;
class Solution{
public:
  int removeDuplicates(vector<int> & nums){
    if(nums.size() <=2 ) return nums.size();
    int index =2 ;
    for(int i=2;i<nums.size();i++){
      if(nums[i] != nums[index-2]) nums[index++] = nums[i];
    }
    return index;
  };

};

int main(){
 vector<int> v(10,2);
 Solution so = Solution();
 int b = so.removeDuplicates(v);
 cout << b << endl;
    
}
//1.not only did the input type is same as the output,but also the output is smaller than the input ,so we can reuse the space of the input to ensure the O(1) space complexiy  


