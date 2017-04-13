#include<iostream>
#include<vector>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};


class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead){
    	if(!pHead) return nullptr;
    	int cirNodeCount = GetnodeCountInCir(pHead);
    	if(!cirNodeCount) return nullptr;
    	ListNode* pFast = pHead,*pSlow = pHead;
    	while(cirNodeCount){
    		pFast = pFast->next;
    		cirNodeCount--;
    	}
    	while(pFast != pSlow){
    		pFast = pFast->next;
    		pSlow = pSlow->next;
    	}
    	return pSlow;

    }

    int GetnodeCountInCir(ListNode* pHead){
    	ListNode* pFast = pHead,*pSlow = pHead,*nodeInCir = nullptr;
    	int nodeCount = 0;
    	//get together in three times 
    	int meetCount = 0;
    	while(meetCount <= 2 && pFast && pFast->next){
    		if(pFast == pSlow) meetCount++;
    		if(meetCount == 2){
    			nodeInCir = pSlow;
    			break;
    		}
    		pFast = pFast->next->next;
    		pSlow = pSlow->next;
    	}
    	if(meetCount  <= 1) return nodeCount;
    	pSlow = pSlow->next;
    	nodeCount = 1;
    	while(pSlow != nodeInCir){
    		nodeCount++;
    		pSlow = pSlow->next;
    	}

    	return nodeCount;
    }
};


int main(){
	ListNode dummy(-1);
	ListNode* pHead = &dummy;
	pHead->next = new ListNode(1);
	pHead->next->next = new ListNode(2);
	pHead->next->next->next = &dummy;	
	auto ret = Solution().EntryNodeOfLoop(&dummy);
	if(!ret) cout << "nullptr" << endl;
	else cout << ret->val << endl;
	return 0;
}

