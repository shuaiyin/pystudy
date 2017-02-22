#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};

//cow net ac
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
    	if(!pHead) return nullptr;
    	if(!pHead->next) return pHead;
    	ListNode* pA = pHead,*pB = pHead->next;
    	ListNode* temp;
    	while(pB){//if have next ,i will execute ,util there is no next..stop at last 
    		temp = pB->next;
    		pB->next = pA;
    		if(pA == pHead) pA->next = nullptr;
    		pA = pB;
    		pB = temp;
    	}
    	return pA;

    }
};

int main(){
	ListNode dummy(-1);
	ListNode* temp = &dummy;
	for(int i=0;i<1;i++){
		temp->next = new ListNode(i);
		temp = temp->next;
	}
	auto ret = Solution().ReverseList(dummy.next);
	while(ret){
		cout << ret->val << endl;
		ret = ret->next;
	}

	return 0;
}