
#include <iostream>
#include <string>
using namespace std;
#include <ctype.h>
//look at c++ page 379

bool compareTwoString(string &str1,string &str2){
    return str1.compare(str2);
}

int main(){
    string ss1("hehe");
    string ss2("f");
    bool result = compareTwoString(ss1,ss2);
    cout << result << endl;


	// string numberics("0123456789");
	// string name("td2d2");
	// string::size_type pos = name.find_first_of(numberics);
	// cout << "found number at index: " << pos
	// 	 << " element is " << name[pos] << endl;

	return 0;
}