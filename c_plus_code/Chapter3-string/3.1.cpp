#include <iostream>
#include <string>
#include<algorithm>
using namespace std;
class Solution{
public:
	//self ac 0301
	bool isPalindrome(string s){
		bool result = true;
		if(s.empty()) return true;
		transform(s.begin(),s.end(),s.begin(),::tolower);
		string::iterator pBegin = s.begin(),pEnd = prev(s.end());
		while(pBegin < pEnd){
			if(!isalnum(*pBegin)) pBegin++;
			else if(!isalnum(*pEnd)) pEnd--;
			else if (*pBegin != *pEnd){
				result = false;
				break;
			}else{
				pBegin++;
				pEnd--;
			}
		}
		return result;

	}

};











int main(){
	string testString("A man  ,a plan, a canal:Panama");
	testString = "Live on evasions? No I save no evil.";
	auto ret = Solution().isPalindrome(testString);
	cout << ret << endl;
	return 0;
}



























/*



void test3(){
	string s = "god live no tips";
	for(string::iterator it=s.begin();it!=s.end();it++){
		cout << *it << endl;
	}
}


void test2(){
	string my_str = "Hello world";
	string::iterator it = my_str.begin();
	cout << *it << endl; //H
	cout << *(it+1) << endl;//e
	for(it=my_str.begin();it!=my_str.end();it++){
		cout << *it << endl;
	}
	//H e l l o w o r l d 
}

void test1(){
	string ss = "i am a bat, i am not battle";
	string sub = "bat";
	int n=0;//appear times;
	int pos;
	pos = ss.rfind(sub);//21
	while(pos != string::npos){
		++n;
		cout << "pos is " << pos << endl;
		pos = ss.rfind(sub,pos-1);
	}
	cout << "numer of appearance is " << n << endl;
}

void test4(){
	string s = "What a good day,But When to Cry";
	transform(s.begin(),s.end(),s.begin(),::tolower);
	cout << s << endl;//what a good day,but when to cry
	auto left = s.begin(),right=prev(s.end());
	cout << *left << endl;//w
	cout << *right << endl;//y
}

void test5(){
	string s = "what is the weather today";
	for(string::iterator it=s.begin();it!=s.end();it++){
		char tmp = *it;
		int result = isalnum(tmp);
		cout << result << endl;
	}
}


int main(){
	const string teststr = "this,is?si,sih?t";
	bool result = Solution().isPalindrome(teststr);
	cout << result << endl;
	return 0;
	string quip("hello world");
	cout << quip.size() << endl;//11
	quip.resize(12);
	cout << quip.size() << endl;//12
	return 0;
	string mymsg = "i am a batman and you battle?";
	int pos2 = mymsg.find("bat");
	while(pos2 != string::npos){
		mymsg.replace(pos2,3,"cat");
		pos2 = mymsg.find("bat",pos2+1);
	}
	cout << mymsg << endl;//i am a catman and you cattle?
	return 0;
	string msg = "It's a batwoman";
	int pos1 = msg.find("bat");
	msg.replace(pos1,3,"cat");
	cout << msg << endl;
	return 0;
	string name = "yin  shuai";
	string mid = "da";
	name.insert(4,mid);//yin da shuai
	cout << name << endl;
	return 0;
	string s = "bat man is a good battle this";
	string sub = "bat";
	int n =0;
	int pos = 0;
	sub = "man";
	pos = s.find(sub,5);//find first 
	cout << pos << endl; 
	return 0;
	while(pos != string::npos){
		++n;
		pos = s.find(sub,pos+1);//find next
	}
	cout << "Number of appearance is " << n << endl;

	return 0;
}


*/