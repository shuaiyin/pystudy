#include<iostream>
#include<vector>
using namespace std;

//well done 
class Solution{
public:
	string longestCommonPrefix(vector<string> &strs){
		if(strs.empty()) return "";
		for(int idx=0;idx<strs[0].size();idx++){
			for(int i=1;i<strs.size();++i){
				if(strs[i][idx] != strs[0][idx])
					return strs[0].substr(0,idx);
			}
		}
		return strs[0];
	}


};


int main(){
	string dd("yins");
	cout << dd.substr(1,2) << endl;
	return 0;
}