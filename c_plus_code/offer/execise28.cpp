#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution{
public:
    vector<string> Permutation(string str) {
        vector<string> result;
        Permutation(str.begin(),str.end(),result);
    }

    void Permutation(string::iterator begin,string::iterator end,vector<string>& result){
    	
    	for(auto tmp = next(begin);tmp != end;tmp++){
    	}


    }
};



int main(){
	string testStr("abcdefg");
	char* test = testStr.c_str();
	cout << test << endl;
	return 0;
	auto ret = Solution().Permutation(testStr);
	for(auto val:ret) cout << val << endl;

	return 0;
}