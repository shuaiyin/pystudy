#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void reOrderArrayBad(vector<int> &array) {
    	auto size = array.size();
    	if(size <= 1) return;
    	auto pIter = array.begin();
    	while(size){
			if(!(*pIter & 0x1)){
				auto val = *pIter;
				auto pTemp = pIter;
				while(next(pTemp)!= array.end()){
					*pTemp = *next(pTemp);
					pTemp++;
				}
				*pTemp = val;
			}else{
				pIter++;
			}
			size--;
	    }
   }

    void reOrderArrayGood(vector<int> &array){
   		if(array.size() <= 1) return;
   		auto pHead = array.begin(),pTail = array.end()-1;
   		while(pHead < pTail){
   			if((*pHead & 0x1) && !(*pTail & 0x1)){
   				pHead++;
   				pTail--;
   			}else if(*pHead & 0x1){
   				pHead++;
   			}else if(!(*pTail & 0x1)){
   				pTail--;
   			}else{
   				swap(*pHead,*pTail);
   				pHead++;
   				pTail--;
   			}
   		}

   }

   void reOrderArrayOther(vector<int>& array){
       if(array.size() <= 1) return;
       auto pHead = array.begin(),pTail = array.end()-1;
       while(pHead < pTail){
       	   while(*pHead & 0x1) pHead++;
       	   while(!(*pTail & 0x1)) pTail--;
       	   if(pHead < pTail){
       	   	  swap(*pHead,*pTail);
       	   	  pHead++;
       	   	  pTail--;
       	   }
       }

   }
};


int main(){
	vector<int> vec({1,4,5,8,10,7});


	Solution().reOrderArrayOther(vec);
	for(auto val:vec) cout << val << endl;

	return 0;
}