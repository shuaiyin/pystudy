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
	ListNode* deleteDuplicationAllow(ListNode* pHead){
		if(!pHead || !pHead->next) return pHead;
		ListNode* prev = pHead,*nextNode = pHead->next;
		while(nextNode){
			if(prev->val == nextNode->val){
				ListNode* tmpNode = nextNode->next;
				prev->next = tmpNode;
				delete nextNode;
				nextNode = tmpNode;
			}else{
				prev = nextNode;
				nextNode = prev->next;

			}

		}
		return pHead;
	}

	ListNode* deleteDuplication(ListNode* pHead){
		if(pHead == nullptr || pHead->next == nullptr) return pHead;
		ListNode* pPreNode = nullptr,*returnHead = nullptr;
		ListNode* pNode = pHead;
		while(pNode){
			ListNode* pNextNode = pNode->next;
			if(pNextNode && pNode->val == pNextNode->val){
				ListNode* pToBeDel = pNode;
				int value = pNode->val;
				while(pToBeDel && pToBeDel->val == value){
					pNextNode = pToBeDel->next;
					delete pToBeDel;
					pToBeDel = pNextNode;
				}
				pNode = pToBeDel;
			}else{
				if(pPreNode == nullptr){
					pPreNode = pNode;
					returnHead = pPreNode;
				}else{
					pPreNode->next = pNode;
					pPreNode = pPreNode->next;
				}
				pNode = pNextNode;
			}
		}
		if(pPreNode) pPreNode->next = nullptr;//critical sentence 
		return returnHead;
	}













};

int main(){
	vector<int> vec({1,3,5,5,5,5,7,8,9,10});
	ListNode dummy(-1);
	ListNode* pList = &dummy;
	for(auto val:vec){
		pList->next = new ListNode(val);
		pList = pList->next;

	}
	auto ret = Solution().deleteDuplication(dummy.next);
	while(ret){
		cout << ret->val << endl;
		ret = ret->next;
	}

	return 0;
}