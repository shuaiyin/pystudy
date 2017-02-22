#include<iostream>
using namespace std;


class Solution{
public:
	//wrong method,it do not care negative integer 
	int NumberOfOneWrong(int n){
		int count =0;
		while(n){
			if(n&1) ++count;
			n = n >> 1;
		}
		return count;
	}

	//good method
	int NumberOfOne(int n){
		int count = 0;
		unsigned int flag = 1;//keep in mind,this place using unsigned int 
		while(flag){
			if(n&flag) ++count;
			flag = flag << 1;
		}
		return count;
	}

	//very good method 
	int NumberOfOneOther(int n){
		int count =0;
		while(n){
			++count;
			n = (n-1) &n ;
		}
		return count;
	}


};


int main(){
	auto ret = Solution().NumberOfOne(30);
	cout << ret << endl;
	ret = Solution().NumberOfOneOther(30);
	cout << ret << endl;
	return 0;
	int a = -3;
	a = a >> 1;
	cout << a << endl;
	return 0;
}

