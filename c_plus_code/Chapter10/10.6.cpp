#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	//only go into deep can we know if it is legal 
	vector<string> restoreIpAddress(const string& s){
		vector<string> result;
		vector<string> ip;//save center result
		dfs(s,ip,result,0);
		return result;
	}

	/*
	  parsing string 
	  ip: save center result 
	  result: save all possible ip address 
	  start :current index treat 
	*/
	void dfs(string s,vector<string>& ip,vector<string>& result,size_t start){
		if(ip.size() == 4 && start == s.size()){//find a legal result
			result.push_back(ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + ip[3]);
			return;
		}
		if(s.size() - start > (4 - ip.size()) * 3)
			return;//purning 
		if(s.size() - start < (4 - ip.size()))
			return;//purning 
		int num = 0;
		for(size_t i =start;i<start+3;i++){
			num = num*10 + (s[i] - '0');
			if(num < 0 || num > 255) continue;//purning 
			ip.push_back(s.substr(start,i-start+1));
			dfs(s,ip,result,i+1);
			ip.pop_back();
			if(num == 0) break;//prefix is 0 is not allowed ,but one 0 is allowed 
		}

	}

};

int main(){
	string inputString("25525511135");
	auto ret = Solution().restoreIpAddress(inputString);
	for(auto val:ret){
		cout << val << endl;
	}

	return 0;
}