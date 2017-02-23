#include<iostream>
#include<vector>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};

class Solution{
public:
	ListNode* MergeLinkList(ListNode* pHead1,ListNode* pHead2){
		if(!pHead2) return pHead1;
		if(!pHead1) return pHead2;
		ListNode dummy(-1);
		ListNode* pIter = &dummy;
		while(pHead1 && pHead2){
			if(pHead1->val > pHead2->val){
				pIter->next = pHead2;
				pHead2 = pHead2->next;
			}else{
				pIter->next = pHead1;
				pHead1 = pHead1->next;
			}
			pIter = pIter->next;
		}
		if(pHead1){
			while(pHead1){
				pIter->next = pHead1;
				pHead1 = pHead1->next;
				pIter = pIter->next;
			}
		} 
		if(pHead2){
			while(pHead2){
				pIter->next = pHead2;
				pHead2 = pHead2->next;
				pIter = pIter->next;
			}
		}
		return dummy.next;
	}
};

int main(){
	// ListNode dummy(-1);
	ListNode* phead1 = new ListNode(100);
	ListNode* pHead2 = nullptr;
	auto ret = Solution().MergeLinkList(phead1,pHead2);
	if(ret) cout << ret->val << endl;
	else cout << "nullptr pointer" << endl;

	return 0;
}