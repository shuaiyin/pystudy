#include<iostream>
#include<vector>
#include<string>
#include<unordered_map>
#include<algorithm>
using namespace std;
//well done 
class Solution{
public:
	vector<string> anagrams(vector<string> &strs){
		unordered_map<string,vector<string>> group;
		for(const auto &s : strs){
			string key = s;
			sort(key.begin(),key.end());
			group[key].push_back(s);
		}
		vector<string> result;
		for(auto it=group.cbegin();it!=group.cend();it++){
			if(it->second.size() > 1){
				result.insert(result.end(),it->second.begin(),it->second.end());
			}
		}

		return result;
	}
};


int main(){
	vector<string> vs{"yin","shuai","hello","tea","eat","dorm","mdor"};
	auto result = Solution().anagrams(vs);
	for(string str:result){
		cout << str << endl;
	}
	/*
	dorm
mdor
tea
eat
	*/
	return 0;

}