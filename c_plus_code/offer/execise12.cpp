#include<iostream>
#include<string>
#include<memory.h>
using namespace std;

class Solution{
public:

	//method one 
	void PrintToMaxOfNDigits(int n){
		if(n <= 0) return;
		string retString(n,'0');
		while(!Increment(retString)){
			// cout << retString << endl;
			printNumber(retString);
		}
	}

	// //method two,using recurse 
	// void PrintToMaxOfNDigitsRecurse(int n){
	// 	if(n <= 0) return;
	// 	string retString(n);
	// 	for(int i=0;i<10;i++){
	// 		number[0] = i + '0';
	// 		Print1ToMaxOfNDigitsRecursively(number,n,0);
	// 	}
	// }


	// void Print1ToMaxOfNDigitsRecursively(string number,int length,int index){
	// 	if(index == length - 1){
	// 		printNumber(number);
	// 		return;
	// 	}
	// }

	bool Increment(string& str){
		auto strLen = str.size();
		int isOverflow = false;
		int nTakeOver = 0;
		for(int i = strLen-1;i>=0;i--){
			int sum = str[i] - '0' + nTakeOver;
			if(i ==(strLen - 1)){
				sum++;
			}
			if(sum >= 10){
				sum = sum - 10;
				nTakeOver = 1;
				str[i] = sum + '0';
				if(i == 0)
					isOverflow = true;
			}else{
				str[i] = sum + '0';
				break;
			}


		}
		return isOverflow;
	}

	void printNumber(string strPrint){
		bool isBeginZero = true;
		for(auto schar:strPrint){
			if(isBeginZero && schar != '0'){
				isBeginZero = false;
			}
			if(!isBeginZero){
				cout << schar;
			}
		}
		cout << endl;
	}


};

int main(){
	Solution().PrintToMaxOfNDigits(2);
	return 0;
	string test("00000");
	Solution().Increment(test);
	Solution().Increment(test);
	cout << test << endl;


	return 0;
}










/*

	void PrintToMaxOfNDigits(int n){
		if(n <= 0) return;
		char * number = new char[n+1];
		memset(number,'0',n);
		number[n] = '\0';
		while(!Increment(number)) 
			printNumber(number);
		delete number;
	}



	bool Increment(char* number){
		bool isOverflow = false;
		int nTakeOver = 0;
		int nLength = strlen(number);
		for(int i=nLength-1; i>=0;i--){
			int nSum = number[i] - '0' + nTakeOver;
			if(i == nLength - 1)
				nSum++;
			if(nSum >= 10){
				if(i == 0)
					isOverflow = true;
				else{
					nSum -= 10;
					nTakeOver = 1;
					number[i] = '0' + nSum;
				}

			}else{
				number[i] = '0' + nSum;
				break;
			}
			
		}

		return isOverflow;

	}

	void printNumber(const char* number){
		int nLength = strlen(number);
		bool isBeginZero = true;
		for(int i = 0;i<nLength;i++){
			if(isBeginZero && number[i] != '0')
				isBeginZero = false;
			if(!isBeginZero)
				cout << number[i];
		}
		cout << endl;

	}

*/




















