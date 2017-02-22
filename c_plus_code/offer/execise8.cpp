#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	int FindMinNumOfReverseVec(vector<int>& vec){
		size_t first = 0;
		size_t last = vec.size()-1;
		size_t middle = (first+last)/2;

		return 0;
	}

	long long Fibonacci(unsigned int n){
		if(n <= 0) return 0;
		if(n == 1) return 1;
		return Fibonacci(n-1) + Fibonacci(n-2);

	}

};

int main(){
	auto ret = Solution().Fibonacci(100);
	cout << ret << endl;
	return 0;
	vector<int> vec({5,6,7,8,0,1,2});
	Solution().FindMinNumOfReverseVec(vec);
	return 0;
}