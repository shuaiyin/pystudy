#include<iostream>
#include<vector>
using namespace std;

//well done 
class Solution{

public:
	//self ac 0301 
	string longestCommonPrefix(vector<string> &strs){
		if(strs.empty()) return string();
		auto firstStringSize = strs[0].size();
		auto vecSize = strs.size();
		int i,j;
		for(i=0;i<firstStringSize;i++){
			for(j=0;j<vecSize;j++){
				if(strs[j][i] != strs[0][i]){	
 					break;
				}
			}
			if(j != vecSize) break;

		}
		return strs[0].substr(0,i);
	}

};


int main(){
	vector<string> vec({"yinshuai","yinshuang","yinna"});
	auto ret = Solution().longestCommonPrefix(vec);
	cout << ret << endl;
	return 0;
}