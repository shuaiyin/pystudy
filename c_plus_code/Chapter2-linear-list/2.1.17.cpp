#include<iostream>
#include<vector>
using namespace std;

//well done 
class Solution{
public:
	vector<int> plusOne(vector<int>& digits){
		add(digits,1);
		return digits;
	}
private:
	//0<=digit<=9
	void add(vector<int>& digits,int digit){
		int c = digit;//carry
		for(auto it= digits.rbegin();it!=digits.rend();++it){
			*it += c;
			c = *it/10;
			*it %= 10;
			//yinshuai maybe add,not test with leetcode
			if(!c) break;//if c is 0,then break


		}
		if(c>0) digits.insert(digits.begin(),1);
	}
};

int main(){
	vector<int> digits{1,2,9,9};
	Solution().plusOne(digits);
	for(auto val:digits){
		cout << val << ":";
	}
	return 0;

	digits.insert(digits.begin(),0);
	digits.insert(digits.begin(),-1);
	for(auto iter=digits.rbegin();iter!=digits.rend();++iter){
		cout << *iter << endl;
	}
	return 0;
}