#include<iostream>
using namespace std;
struct ListNode{
  int val;
  ListNode *next;
  ListNode(int x) : val(x),next(NULL){}
};
//well done
class Solution{
public:
	ListNode* removeNthFromEnd(ListNode* head,int n){
		ListNode dummy(-1);
		dummy.next = head;
		ListNode *p = &dummy, *q=&dummy;
		for(int i=0;i<n;i++){//q first step n 
			q = q->next;
		}
		while(q->next){
			p = p->next;
			q = q->next;
		}
		ListNode *tmp = p->next;
		p->next = p->next->next;
		delete tmp;
		return dummy.next;



	}
};
int main(){
	ListNode head(-1);
	ListNode *tmp = &head;
	for(int i=0;i<5;i++){
		tmp->next = new ListNode(i);
		tmp = tmp->next;
	}
	Solution so = Solution();
	so.removeNthFromEnd(&head,2);
	tmp = &head;
	while(tmp){
		tmp = tmp->next;
		cout << tmp->val << endl;
	}
	return 0;
}