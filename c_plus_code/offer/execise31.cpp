#include<iostream>
#include<vector>
using namespace std;


class Solution{
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
    	int greatestSum = 0;
    	int beforeAddSum = 0;
    	for(int val:array){
    		beforeAddSum = greatestSum;
    		greatestSum += val;
    		if(beforeAddSum > greatestSum){
    			greatestSum = val;
    		}

    	}
    	return 0;
    }
};


int main(){
	int num1,num2;
	vector<int> data({1,1,3,4,4,3,2,6});
	auto ret = FindGreatestSumOfSubArray(data);

	return 0;
}