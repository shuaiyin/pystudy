#include<iostream>
using namespace std;


class Solution{
public:
	int NumberOf1Between1AndN_Solution(int n){
		int count = 0;
		for(int i=1;i<=n;i++){
			int cur = i;
			while(cur){
				if(cur%10 == 1) count++;
				cur = cur/10;
			}
		}
		return count;
	}
};

int main(){
	auto ret = Solution().NumberOf1Between1AndN_Solution(205852525);
	cout << ret << endl;
	return 0;
}