#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	bool canJump(const vector<int>& nums){
		int reach = 1;//
		for(int i=0;i<reach && reach < nums.size();i++){
			reach = max(reach,i+1+nums[i]);
			return reach >= nums.size();
		}
	}
};

int main(){
	vector<int> vec({2,3,1,1,4});
	auto ret = Solution().canJump(vec);
	return 0;
}