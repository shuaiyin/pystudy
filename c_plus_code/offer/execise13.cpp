#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){};
};

class Solution{
public:
	//delete node with O(n) time  complex
	void DeleteSpecifyNode(ListNode* head,ListNode* toDeleteNode){
		if(!head || !toDeleteNode) return;
		if(head == toDeleteNode) delete head;//may exist some problem here 
		ListNode* temp = head;
		while(temp){
			if(temp->next == toDeleteNode){
				temp->next = toDeleteNode->next;
				delete toDeleteNode;
				break;
			}
			temp = temp->next;
		}
	}
	//delete node with O(1) time complex 
	void DeleteSpecifyNodeFastMethod(ListNode* head,ListNode* toDeleteNode){
		if(!head || !toDeleteNode) return;

	}

};


int main(){
	ListNode dummy(-1);
	ListNode* temp = &dummy;
	for(int i=0;i<6;i++){
		temp->next = new ListNode(i);
		temp = temp->next;
	}
	ListNode* head = dummy.next;
	Solution().DeleteSpecifyNode(head,head);
	// cout << temp->next->val << endl;
	temp = dummy.next;
	while(temp){
		cout << temp->val << endl;
		temp = temp->next;
	}
}