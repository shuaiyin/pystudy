#include<iostream>
#include<vector>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){};
};

class Solution{
public:
	void reorderList(ListNode* head){
		if(!head || !head->next || !head->next->next) return;
		ListNode* pheadSlow = head,*pheadFast = head,*prev = nullptr;
		while(pheadFast && pheadFast->next){
			prev = pheadSlow;
			pheadSlow = pheadSlow->next;
			pheadFast = pheadFast->next->next;
		}
		prev->next = nullptr;//cut at middle 
		ListNode* nextPart = ReverseLink(pheadSlow);
		// nextPart = ReverseLink(nextPart);
		while(nextPart){
			cout << nextPart->val << endl;
			nextPart = nextPart->next;
		}
		ListNode* phead = head;
		while(nextPart){
			ListNode* tmp = nextPart->next;
			nextPart->next = phead->next;
			phead->next = nextPart;
			nextPart = tmp;
		}
	}

public: 
	ListNode* ReverseLink(ListNode* head){
		if(!head || !head->next) return head;
		ListNode* prevNode = head,*nextNode = head->next;
		while(nextNode->next){
			ListNode* tmp = nextNode->next;
			nextNode->next = prevNode;
			prevNode = nextNode;
			nextNode = tmp; 
		}	
		head->next = nullptr;
		nextNode->next = prevNode;
		return nextNode;


	}

};

int main(){
	vector<int> vec({1,2,3,4,5,6,7});
	ListNode dummy(-1);
	ListNode* pList = &dummy;
	for(auto val:vec){
		pList->next = new ListNode(val);
		pList = pList->next;

	}
	Solution().reorderList(dummy.next);
	return 0;
	ListNode* head = dummy.next;

	while(head){
		cout << head->val << endl;
		head = head->next;
	}
	// cout << head->next->val << endl;

	return 0;
}

