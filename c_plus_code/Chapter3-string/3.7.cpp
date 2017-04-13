#include<iostream>
using namespace std;

class Solution{
public:
	bool isMatch(const string& s,const string& p){
		return isMatch(s.c_str(),p.c_str());
	}

	bool isMatchYs(const char* s,const char* p){
		bool star = false;
		const char* str=s,*ptr=p;
		while(*ptr != '\0'){
			switch(*ptr){
				case '?':
					ptr++;
					str++;
					break;
				case '*':
					while(*ptr != '*') ptr++;

			}

		}

		return true;
	}



private:


	bool isMatchReverse(const char* s,const char* p){
		if(*p =='*'){
			while(*p == '*') p++;
			if(*p == '\0') return true;
			while(*s != '\0' && !isMatchReverse(s,p)) s++;
			return *s != '\0'; 
		}else if(*p == '\0' || )
		return true;
	}












	bool isMatch(const char *s, const char *p){
		bool star = false;
		const char* str,*ptr;
		for(str=s,ptr=p;*ptr!='\0';str++,ptr++){
			switch(*ptr){
				case '?':
					break;
				case '*':
					star = true;
					s = str,p=ptr;
					while(*p == '*') p++;//skip continus '*'
					if(*p == '\0') return true;
					str = s - 1;
					ptr = p - 1;
					break;
				default:
					if(*str != *ptr){
						//if there is no star before,match failed 
						if(!str) return false;
						s++;
						str = s - 1;
						ptr = p - 1;
					}
			}
		}
		while(*ptr == '*') ptr++;
		return (*ptr == '\0');
		return true;
	}
};

int main(){
	const char* tests = "abc";
	const char* testp = "*?c";
	Solution().isMatchYs(tests,testp);
	return 0;
	int a = 3;
	switch(a){
		case 0: 
			cout << "heheda" << endl;
			break;
		case 1:
			cout << "first day" << endl;
			break;
		default:
			cout << "defalut va" << endl;
	}
	return 0;


	// const char* test = "yinshuai";
	string test("yinshuai");
	Solution().isMatch(test,test);
	return 0;
}