#include<iostream>
#include<algorithm>
using namespace std;


class Solution{
public:
	int strStr(string haystack, string needle) {
		if(needle.empty()) return 0;
		if(haystack.size() < needle.size()) return -1; 
		auto pHaystack = haystack.begin();
		auto pneedle = needle.begin();
		for(;pHaystack != haystack.end();pHaystack++){
			if(*pHaystack == *pneedle){
				for(auto needleRecord=pneedle+1,haystackRecord=pHaystack+1;needleRecord!=needle.end();needleRecord++){
					if(needleRecord)
				}
			}
		}
		while(pHaystack != haystack.end()){
			if(*pneedle != *pHaystack){
				pHaystack++;
				continue;
			}
			string::const_iterator haystackRecord,needleRecord;
			for(haystackRecord=pHaystack+1,needleRecord=pneedle+1;needleRecord != needle.end();haystackRecord++,needleRecord++){
				if(*haystackRecord != *needleRecord) break;
			}
			if(needleRecord == needle.end())
				return distance(haystack.begin(),pHaystack);

		}
		return ret;
        
    }
};

int main(){ 

	string haystack = "mississippi";
	string needle = "issip";
	auto ret = Solution().strStr(haystack,needle);
	cout << ret << endl;
	return 0;
}