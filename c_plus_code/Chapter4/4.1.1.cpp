#include<iostream>
#include<string>
#include<stack>
using namespace std;
class Solution{
public:
	bool isValid(string const &s){
		string left = "([{";
		string right= ")]}";
		stack<char> stk;
		for(int i=0;i<s.length;i++){
			if(left.find(s[i])){
				stk.push(s[i]);
			}else{
				continue;
			}
		}
		return true;
	}
};

int main(){
	stack<int> stk;
	stk.push(20);
	cout << stk.empty() << endl;
	return 0;
	Solution so = Solution();
	const string shuai = "heheda";
	so.isValid(shuai);
	return 0;
}