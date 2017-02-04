#include<iostream>
using namespace std;
struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x): val(x),next(NULL){}

};
//well done of one of the given method...
class Solution{
public:
	ListNode *deleteDuplicates(ListNode *head){//fisrt version 
		if(!head) return head;
		for(ListNode *prev=head,*cur=head->next;cur;cur->next){
			if(prev->val == cur->val){
				prev->next = cur->next;
				delete cur;
			}else{
				prev = cur;
			}
		}
		return head;
	}

};

int main(){


	ListNode head(-1);
	ListNode *headPointer = &head;
	headPointer->next = new ListNode(11);
	headPointer = headPointer->next;
	headPointer->next = new ListNode(12);
	headPointer = headPointer->next;
	headPointer->next = new ListNode(13);
	headPointer = headPointer->next;
	headPointer->next = new ListNode(13);
	headPointer = headPointer->next;
	headPointer->next = new ListNode(13);
	headPointer = headPointer->next;
	headPointer->next = new ListNode(14);
	Solution so = Solution();
	ListNode *headReturn = so.deleteDuplicates(&head);

	return 0;
	for(ListNode *prev=&head,*cur=prev->next;cur;cur=cur->next){
		if(prev->val == cur->val){
			delete cur;
			prev->next = cur->next;
		}else{
			prev = prev->next;
		}
	}

	for(ListNode * cur=&head;cur;cur=cur->next){
		cout << cur->val << endl;
	}
	return 0;

	for(ListNode *cur=&head;cur;cur=cur->next){
		if(cur->val == 11){
						delete cur;
			cout << "test cursor" << endl;
			cout << cur->val << endl;
			cout << cur << endl;
			cout << cur->next << endl;
			cout << cur->next->val << endl;
			break;
		}


		cout << cur->val << endl;
	}

	return 0;
}