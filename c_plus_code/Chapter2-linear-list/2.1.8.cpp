#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution{
public:
vector< vector<int> > threeSum(vector<int> &nums){
   vector< vector<int> > result;
   if(nums.size() < 3) return result;
   sort(nums.begin(),nums.end());
   const int target = 0 ;//for that the define result is 0
   //we can use auto to simplify our type define,for that the origin type 
   //is so redundant and when using type define,it can judge type auto
   //in fact in this place,if we do not use auto,we must use something like follow:
   //vector< vector<int> >::iterator it = nums.end()    ,etc  
   auto last = nums.end();
   for(auto i = nums.begin() ; i != prev(last,2);++i){
   		auto j = next(i);
   		if(i > nums.begin() && *i == *(i -1)) continue;//skip the duplicate value 
   		auto k = last -1;
   		while(j < k){
   			if(*i + *j + *k < target){
   				++j;
   				while(*j == *(j-1) && j < k) ++j;
   			}else if(*i + *j + *k > target){
   				--k;
   				while(*k == *(k+1) && j < k) --k;
   			}else{
   				result.push_back({*i,*j,*k});
   				++j;
   				--k;
   				while(*j == *(j-1) && *k == *(k+1) && j < k) ++j;
   			}
   		}
   }
   return result;
  }

};
int main(){
   // Solution so = Solution();
   int init_arr[] = {-1,0,1,2,-1,-4};
   vector<int> input_vector(init_arr,init_arr+6);
   Solution so = Solution();
   vector< vector<int> >  result =  so.threeSum(input_vector);
   for(i iter = result.begin();iter != result.end(); ++iter){
   	 cout << "heheda" << endl;
   }




   


}
