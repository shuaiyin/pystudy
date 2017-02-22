#include<iostream>
#include<stack>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};

class Solution{
public:
	//first method using stack
	void PrintListReverseIter(ListNode* head){
		if(!head) return;
		ListNode* node = head;
		stack<ListNode*> stk;
		while(node){
			stk.push(node);
			node = node->next;
		}
		while(!stk.empty()){
			node = stk.top();
			stk.pop();
			cout << node->val << endl;
		}
	}

	//second method using recurse..(in substance stack)
	void PrintListReverseIterRecurse(ListNode* head){
		if(!head) return;
		if(head->next){
			PrintListReverseIterRecurse(head->next);
		}
		cout << head->val << endl;

	}  

};


int main(){
	ListNode head(0);
	ListNode* temp = &head;
	for(int i=1;i<5;i++){
		temp->next = new ListNode(i);
		temp = temp->next;
	}
	Solution().PrintListReverseIterRecurse(&head);
	return 0;
}