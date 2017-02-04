#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
class Solution{
public:
	int lengthOfLastWord(const string &s){//first easy eay
		auto first = find_if(s.rbegin(),s.rend(),::isalpha);
		auto last = find_if_not(first,s.rend(),::isalpha);
		return distance(first,last);
	}

	int lengthOfLastWordSec(const string &s){
		return lengthOfLastWordSec(s.c_str());//s.c_str return const pointer.
	}
private:
	int lengthOfLastWordSec(const char *s){
		int len =0;
		while(*s){
			if(*s++ != ' ')
				++len;
			else if(*s && *s != ' ')
				len =0;
		}
		return len;
	}
};

int main(){
	string testString = "what a good day";
	int len = Solution().lengthOfLastWord(testString);
	cout << len << endl;//3
	len = Solution().lengthOfLastWordSec(testString);
	cout << len << endl;//3

	return 0;
	string d = "hello world";
	int dis = distance(d.begin(),d.begin()+1);//the function of distance is just address sub 
	cout << dis << endl;//1
	int dis2 = distance(d.rbegin(),d.rbegin()+1);
	cout << dis2 << endl;//1
	return 0;
	auto result = find_if(d.rbegin(),d.rend(),::isalpha);
	auto result1 = find_if_not(d.rbegin(),d.rend(),::isalpha);
	cout << *result1 << endl;
	cout << *result << endl;
	return 0;
}