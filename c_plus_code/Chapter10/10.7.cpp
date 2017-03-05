#include<iostream>
using namespace std;

class Solution{
public:
	vector<vector<int>> combinationSum(vector<int>& nums,int target){
		sort(nums.begin(),nums.end());
		vector<vector<int>> result;//finaly resutl 
		vector<int> path;//center result 
		dfs(nums,path,result,target,0);
		return result;
	}

private:
	void dfs(vector<int>& nums,vector<int>& path,vector<vector<int>>& result,int gap,int start){
		if(gap == 0){
			result.push_back(path);//available result 
			return;
		}
		for(size_t i= start,i<nums.size();i++){//extend status 
			if(gap < nums[i]) return;//cut 
			path.push_back(nums[i]);//execute extend action 
			dfs(nums,path,result,gap-nums[i],i);
			path.pop_back();//cancel action 
		}
	}

};

int main(){

	return 0;
}