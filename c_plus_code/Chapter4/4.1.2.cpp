#include<iostream>
#include<stack>
using namespace std;

class Solution{
public:
	int longestValidParentheses(const string &s){
		int max_len =0,last=-1;//the postion of the last ')'
		stack<int> lefts;//keep track of the positions of non-matching '(' s 
		for(int i=0;i<s.size();i++){
			if(s[i] == '('){
				lefts.push(i);
			}else{
				if(lefts.empty()){
					//no matching left
					last = i;
				}else{
					//find a matching pair 
					
				}
			}
		}
		return 0;
	}

};


int main(){
	string ss = "yinshuai";
	cout << ss.size() <<endl;
	return 0;
}





