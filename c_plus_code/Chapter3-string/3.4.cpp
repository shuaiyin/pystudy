#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
//well done
class Solution{
public:
	string addBinary(string a,string b){
		string result;
		reverse(a.begin(),a.end());
		reverse(b.begin(),b.end());
		cout << a << endl;

		// const size_t n = a.size() > b.size() ? a.size():b.size();
		// cout << n << endl;
	}

};

void test1(){
	int a = 1;
	cout << sizeof('0') << endl;
	char b = a - '0' >> 4;
	cout << b << endl;
	// cout << sizeof(b) << endl;
}

int main(){
	string a = "1001";
	string b = "011";
	int ac = '0';
	int bc = 1;
	char rc = ac+bc;
	cout << rc << endl;
	return 0;
	string result;
	const size_t n = a.size() > b.size() ? a.size():b.size();
	reverse(a.begin(),a.end());
	reverse(b.begin(),b.end());
	int carry = 0;
	
	for(size_t i;i<n;i++){
		const int ai = i < a.size()? a[i]-'0':0;
		const int bi = i < b.size()? b[i]-'0':0;
		const int val = (ai+bi+carry)/2;
		carry = (ai+bi+carry)/2;
		result.insert(result.begin(),val+'0');
	}
	//the result is the final value 

	return 0;
}