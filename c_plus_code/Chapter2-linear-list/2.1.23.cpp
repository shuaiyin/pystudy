#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
//well done 
class Solution{
public:
	int singleNumber(vector<int> &nums){
		 int x = 0;//oper with 0 bit with remain the original 
		 for(auto iter=nums.begin();iter!=nums.end();++iter){
		 	x ^= *iter;
		 }
		 return x;
		 
	}

	// int singleNumber2(vector<int> &nums){
	// 	reutrn accumulate(nums.begin(),nums.end(),0,bit_xor<int>());
	// }


};

int main(){
 int arr[] = {12,2,14,14,2};
 vector<int> init_vect(arr,arr+5);
 Solution so = Solution();
 int result = so.singleNumber(init_vect);
 cout << result << endl;
 return 0;
}
