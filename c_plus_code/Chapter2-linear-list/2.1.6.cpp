#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
//one of method well done 
class Solution{
public:
	int longestConsecutive(const vector<int> &nums){
		unordered_map<int,bool> used;
		for(auto i:nums) used[i] = false;
		int longest = 0;
		for(auto i:nums){
			if(used[i]) continue;
			int length = 1;
			used[i] = true;
			for(int j=i+1;used.find(j)!=used.end();++j){
				used[j] = true;
				++length;
			}
			for(int j=i-1;used.find(j)!=used.end();--j){
				used[j] = true;
				++length;
			}
			longest = max(longest,length);
		}
		return longest;
	}
};
int main(){
	const vector<int> testvec{100, 4, 200, 1, 3, 2};
	Solution().longestConsecutive(testvec);
	return 0;
}