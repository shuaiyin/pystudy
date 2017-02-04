#include<iostream>
#include<stack>
#include<string>

using namespace std;


int main(){
	stack<string> stk;//init space for a stack 
	stk.push("hello");//push value into stack
	stk.push("beijing");
	stk.push("welcome");
	stk.push("to");
	cout << stk.size() << endl;
	string ss1 = "1234";
	string ss2 = "5678";
	int result = ss1.find('2');
	cout << ss1[result] << endl;
	return 0;

	cout << result << endl;

	return 0;
}