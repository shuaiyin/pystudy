#include<iostream>
#include<vector>
using namespace std;


class Solution{
public:
	//cow net ac 
	void FindNumsAppearOnce(vector<int> data,int* num1,int *num2) {
		if(data.size() <= 1) return;
		int xorResult = 0;
		for(auto val:data){
			xorResult ^= val;
		}
		*num1 = 0;
		*num2 = 0;
		for(auto val:data){
			if(xorResult & val){
				*num1 ^= val;
			}else{
				*num2 ^= val;
			}
		}

    }
};


int main(){
	int num1,num2;
	vector<int> data({1,1,3,4,4,3,2,6});
	Solution().FindNumsAppearOnce(data,&num1,&num2);
	cout << num1 << endl;
	cout << num2 << endl;

	return 0;
}