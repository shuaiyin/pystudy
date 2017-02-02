#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x) : val(x),next(NULL){}
};

class Solution{
public:
	ListNode *deleteDupicates(ListNode *head){
		if(!head||!head->next) return head;
		ListNode *p = head->next;

	}
};
int main(){
	ListNode head(-1);
	ListNode *tmp = &head;
	tmp->next = new ListNode(10);
	tmp = tmp->next;
	tmp->next = new ListNode(11);
	tmp = tmp->next;
	tmp->next = new ListNode(11);
	tmp = tmp->next;
	tmp->next = new ListNode(12);
	for(ListNode *prev=&head,*cur=prev->next;cur;cur=cur->next){
		if(prev->val == cur->val){
			prev->next = cur->next;
			cur->next = cur->next->next;

		}
	}


	for(ListNode *cur=&head;cur;cur=cur->next){
		continue;
	}

	return 0;

}
