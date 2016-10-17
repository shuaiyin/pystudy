#include<iostream>

class Solution{
public:
   vector< vector<int> > fourSum(vector<int> &nums,int target){
      vector< vector<int> > result;
      if(nums.size() < 4) return result;
      sort(nums.begin(),nums.end());
 
      unordered_map<int,vector< pair<int,int> >> cache;
      for(size_t a = 0; a< nums.size(); ++a){
         for(size_t b = a +1; b<nums.size(); ++b){
            cache[nums[a] + nums[b]].push_back(pair<int,int>(a,b));
         }
      }
      for(int c =0;c<nums.size(); ++c){
        for(size_t d = c+1; d< nums.size(); ++d){
           const int key = target - nums[c] - nums[d];
           if(cache.find(key) == cache.end()) continue;
           const auto & vec = cache[key];
           
        }
      }
 
   }


}
