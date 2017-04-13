#include <iostream>
#include<string>
using namespace std;

void reverse(char* str){
	char* end = str;
	char tmp;
	if(str){
		while(*end){
			++end;//find the end of the str 
		}
	}
	end--;
	while(str < end){
		tmp = *str;
		*str++ = *end;
		*end-- = tmp;
	}
}

void reverseTest(){
	char s[] = "abcdefghijk";
	reverse(s);
	puts(s);

}

int main(){
	reverseTest();
}