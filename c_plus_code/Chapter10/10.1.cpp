#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution{
public:
	vector<vector<string>> partition(string s){
		vector<vector<string>> result;
		vector<string> path;
		dfs(s,path,result,0,1);
		return result;
	}

	//prev means prev clapboard ,and start means current clapboard 
	void dfs(string& s,vector<string>& path,vector<vector<string>>& result,size_t prev,size_t start){
		if(start == s.size()){//if it is the last 
			if(isPalindrome(s,prev,start-1)){
				path.push_back(s.substr(prev,start-prev));
				result.push_back(path);
				path.pop_back();
			}
			return;
		}
		//if[prev,start-1] is palindrome.then can interrupt,and can also do not interrupt 
		dfs(s,path,result,prev,start+1);
		if(isPalindrome(s,prev,start-1)){
			//interupt
			path.push_back(s.substr(prev,start-prev));
			dfs(s,path,result,start,start+1);
			path.pop_back();

		}

	}




	bool isPalindrome(const string& s,int start,int end){
		while(start < end && s[start] == s[end]){
			start++;
			end--;
		}
		return start >= end;
	}
};


int main(){
	string s("bcaacb");
	vector<vector<string>> ret;
	ret = Solution().partition(s);
	for(auto vecval:ret){
		for(auto val:vecval){
			cout << val << ',';
		}
		cout << endl;
	}
	return 0;
}