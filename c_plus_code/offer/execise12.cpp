#include<iostream>
#include<string>
#include<memory.h>
using namespace std;

class Solution{
public:
	void PrintToMaxOfNDigits(int n){
		if(n <= 0) return;
		char * number = new char[n+1];
		memset(number,'0',n);
		number[n] = '\0';
	}

	bool Increment(char* number){
		bool isOverflow = false;
		int nTakeOver = 0;
		int nLength = strlen(number);
		cout << nLength << endl;
		for(int i=nLength-1; i>=0;i--){
			break;
		}

		return isOverflow;

	}
};

int main(){
	char* mychar = new char[4];
	memset(mychar,'9',3);
	mychar[3] = '\0';
	Solution().Increment(mychar);
	char a = '3';
	char b = a - 300;
	b = b & 0x7F;
	// int c  = int(b);
	cout << b << endl;
	return 0;
	// Solution().PrintToMaxOfNDigits(999);
	char* number = new char[999999999];
	memset(number,'0',3);
	number[3] = '\0';
	cout << number << endl;
	while(1);


	return 0;
}