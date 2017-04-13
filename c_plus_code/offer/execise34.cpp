#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
	//not the goodest way
    int GetUglyNumber_SolutionHard(int index) {
    	if(index <=0) return 0;
    	int num =1;
    	int i=0;
    	while(i<index){
    		if(isUgly(num)) i++;
    		num++;   			
    	}
    	return num;
    }


    //better method 
    int GetUglyNumber_Solution(int index){
    	unordered_map<
    }

private:
	bool isUgly(int val){
		while(val%2 == 0) val /= 2;
		while(val%3 == 0) val /= 3;
		while(val%5 == 0) val /= 5;
		return val == 1 ? true:false;
	}
};



int main(){
	// vector<int> vec({1,2,3,4,5,6,7,0});
	int a = 150;
	auto ret = Solution().GetUglyNumber_SolutionHard(a);
	cout << "the result using hardest way is " << ret << endl;
	ret = Solution().GetUglyNumber_Solution(a);
	cout << "the result using better way is " << ret << endl;

	return 0;
}
