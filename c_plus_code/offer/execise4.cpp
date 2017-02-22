#include<iostream>
#include<string>
using namespace std;

class Solution{
public:
	void ReplaceBlank(string str){
		cout << "d" << endl;
	}

	void ReplaceBlankC(char string[], int length){
		if(string == NULL || length < 0) return;
		//original length is the real length of the string 
		int originalLength = 0;
		int numberOfBlank = 0;
		int i =0 ;
		while(string[i] != '\0'){
			++originalLength;
			if(string[i] == ' ')
				++numberOfBlank;
			++i;
		}
		int newLength = originalLength + numberOfBlank * 2;
		if(newLength > length) return;
		int indexOfOriginal = originalLength;
		cout << indexOfOriginal << endl;
		int indexOfNew = newLength;
		while(indexOfOriginal >= 0 && indexOfNew > indexOfOriginal){
			if(string[indexOfOriginal] == ' '){
				string[indexOfNew--] = '0';
				string[indexOfNew--] = '2';
				string[indexOfNew--] = '%';
 			}else{
 				string[indexOfNew--] = string[indexOfOriginal];
 			}
 			--indexOfOriginal;
		}
	}
};

int main(){
	char string[30] = "yinshuai is a good boy";
	Solution().ReplaceBlankC(string,30);//22+4*2
	cout << string << endl;	
	return 0;

}