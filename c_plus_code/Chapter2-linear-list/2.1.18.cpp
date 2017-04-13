#include<iostream>
#include<vector>
using namespace std;
//leetcode ac 0309
class Solution{
public:
	int climbStairs(int n){
		if(n <= 0) return 0;
		vector<int> dataCache(n+1,0);
		int res = climbStairs(n,dataCache);
		return res;
	}
private:
	int climbStairs(int n,vector<int>& dataCache){
		if(n == 1) return 1;
		if(n == 2) return 2;
		if(dataCache[n]) return dataCache[n];
		return  dataCache[n]  = climbStairs(n-1,dataCache) + climbStairs(n-2,dataCache);
	}
};

int main(){
	int n = 6;
	auto ret = Solution().climbStairs(n);
	cout << ret << endl;
	return 0;
}