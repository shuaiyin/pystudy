#include<iostream>
#include<string>
#include<memory.h>
using namespace std;

class Solution{
public:
	void PrintToMaxOfNDigits(int n){
		return;
	}

};

int main(){
	const char* s = "this is a good school ";
	while(*s != '\0'){
		cout << *s << endl;
		s++;
	}
	// cout << s << endl;

	return 0;
}



/*

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
			int nSum = number[i] - '0' + nTakeOver;
			if(i == nLength -1) nSum++;
		}

		return isOverflow;

	}


*/