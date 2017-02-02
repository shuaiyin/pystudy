#include<iostream>
using namespace std;

struct ListNode{
  int val;
  ListNode * next;
  ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
	ListNode *swapPairs(ListNode *head){
		if(!head ||!head->next) return head;
		return head;
	}
};

int main(){
	ListNode dummy(-1);
	ListNode *tmp;
	tmp = &dummy;
	for(int i=1;i<5;i++){
		tmp->next = new ListNode(i);
		tmp = tmp->next;
	}
	return 0;
}