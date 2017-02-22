#include<iostream>
using namespace std;


class Solution{
public:
	//recurse method 
	long long Fibonacci(unsigned int n){
		if(n <= 0) return 0;
		if(n == 1) return 1;
		return Fibonacci(n-1) + Fibonacci(n-2);
	}
	//iterator method 
	long long FibonacciIter(unsigned int n){
		if(n==0) return 0;
		if(n==1) return 1;
		long long firstPosVal=1,secondPosVal=0,total=0;
		for(unsigned int i=2;i<=n;i++){
			total = firstPosVal + secondPosVal;
			secondPosVal = firstPosVal;
			firstPosVal = total;

		}
		return total;
	}

	//frog step (two steps or one step)
	long long FrogStepRecurse(unsigned int steps){
		if(steps == 2) return 2;
		if(steps == 1) return 1;
		if(steps == 0) return 0;
		return FrogStepRecurse(steps-1) + FrogStepRecurse(steps-2);

	}

	//frog step
	long long FrogStepIterator(unsigned int steps){
		if(steps == 0) return 0;
		if(steps == 1) return 1;
		if(steps == 2) return 2;
		long long firstPosVal=2,secondPosVal=1,totalVal=0;
		for(unsigned int i=3;i<=steps;i++){//start from 3,end at n 
			totalVal = firstPosVal + secondPosVal;
			secondPosVal = firstPosVal;
			firstPosVal = totalVal;
		}
		return totalVal;
	}

};



int main(){
	auto ret = Solution().Fibonacci(4);
	cout << "recurse method result is " << ret << endl;
	ret = Solution().FibonacciIter(4);
	cout << "iterator method result is " << ret << endl;
	ret = Solution().FrogStepRecurse(5);
	cout << "frog step recurse method result is : " << ret << endl;
	ret = Solution().FrogStepIterator(5);
	cout << "frog step iterator method result is: " << ret << endl;
	return 0;
}