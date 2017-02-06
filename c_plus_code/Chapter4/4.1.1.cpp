#include<iostream>
#include<string>
#include<stack>
using namespace std;
//well done 
class Solution{
public:
	bool isValid(string const &s){
		string left = "([{";
		string right= ")]}";
		stack<char> stk;
		for(auto c:s){
			if(left.find(c) != string::npos){
				stk.push(c);
			}else{
				if(stk.empty()||stk.top()!=left[right.find(c)])
					return false;
				else
					stk.pop();
			}
		}

		return stk.empty();
	}
};

int main(){
	Solution so = Solution();
	const string shuai = "([])";
	auto res = so.isValid(shuai);
	cout << res << endl;
	return 0;
	stack<int> stk;
	stk.push(20);
	cout << stk.empty() << endl;
	string yinshuai("yinshuai");
	auto result = yinshuai.find("yin");
	cout << result << endl;
	return 0;

}