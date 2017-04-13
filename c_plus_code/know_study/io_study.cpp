#include<iostream>
#include<vector>
#include<string>
#include<unordered_map>
#include<algorithm>
using namespace std;


void test1(){
	cout << "Enter two numbers: " << endl;
	int v1,v2;
	cin >> v1 >> v2;//using space or '\n' to seperate 
	cout << "the sum of " << v1 << " and " << v2 
	     << " is " << v1 + v2 << endl;

}


void test2(){
	int wordCount;
	cin >> wordCount;
	vector<string> word(wordCount);
	for(int i=0;i<wordCount;i++){
		cin >> word[i];
	}
	unordered_map<string,vector<string>> um;
	for(auto str:word){
		string s = str;
		sort(s.begin(),s.end());
		um[s].push_back(str);
	}
 	for(auto iter = um.begin();iter != um.end();iter++){
 		if(iter->second.size() > 1){
 			for(auto val:iter->second){

 			}
 		}
 	}

}


class Solution {
public:
    bool detectCapitalUse(string word) {
        auto wordSize = word.size();
        if(wordSize <= 1) return true;
        if(isCapital(word[0])){

            if(isCapital(word[1]))
                for(int i=2;i<wordSize;i++)
                	
                    if(!isCapital(word[i])) return false;
            else
                for(int i =2;i<wordSize;i++)
                    if(isCapital(word[i])) return false;
        }else{
            for(int i=1;i<wordSize;i++){
                if(isCapital(word[i])) return false;
            }
        }
        return true;
        
    }
    
private:
    bool isCapital(char simChar){
        return (simChar >= 'A' && simChar <= 'Z') ? true:false; 
    }
};

int main(){
	// test1();
	// test2();
	auto ret = Solution().detectCapitalUse("YINSHUAI");
	cout << ret << endl;
	return 0;
}