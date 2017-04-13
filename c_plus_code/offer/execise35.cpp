#include<iostream>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int FirstNotRepeatingChar(string str) {
    	if(str.empty()) return -1;
    	unordered_map<char,int> charMap;
        for(char val:str){
        	if(charMap.find(val) == charMap.end()){
        		charMap[val] = 1;
        	}else{
        		charMap[val] += 1;
        	}
        }
        int strLen = str.size();
        for(int i=0;i<strLen;i++){
        	if(charMap[str[i]] == 1) return i;
        }
        return -1;
    }
};

int main(){
	string testStr = "google";
	auto ret = Solution().FirstNotRepeatingChar(testStr);
	cout << ret << endl;
 	return 0;
}