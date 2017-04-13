#include<iostream>
#include<string>
using namespace std;


class Solution{
private:
	string str;
	int count[256] = {0};

public:
	//insert one char from stringstream 
	void Insert(char ch){
		str += ch;
		count[ch]++;
	}

	//return the first appearence once char in current stringstream
	char FirstAppearingOnce(){
		int len = str.size();
		for(int i=0;i<len;i++){
			if(count[str[i]] == 1)
				return str[i];
		}
		return '#';
	}
};

int main(){
	string testStr = "googll";
	Solution s = Solution();
	for(auto val:testStr){
		s.Insert(val);
	}
	char ret = s.FirstAppearingOnce();
	cout << ret << endl;
	return 0;
}

