#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};


//cow network ac 
class Solution {
public:
	ListNode* FindKthToTail(ListNode* pListHead, unsigned int k){
		if(!pListHead || k==0) return nullptr;
		ListNode* pAhead = pListHead;
		ListNode* pBehind = pListHead;
		k = k - 1;
		while(k && pAhead->next){
			pAhead = pAhead->next;
			k--;
		}
		if(k >0) return nullptr;
		while(pAhead->next){
			pAhead = pAhead->next;
			pBehind = pBehind->next;
		}
		return pBehind;

	}
};


int main(){
	ListNode dummy(-1);
	ListNode* temp = &dummy;
	for(int i=0;i<2;i++){
		temp->next = new ListNode(i);
		temp = temp->next;
	}
	auto ret = Solution().FindKthToTail(dummy.next,3);
	// cout << "Test case 1: " << ret->val << endl;


	return 0;
}