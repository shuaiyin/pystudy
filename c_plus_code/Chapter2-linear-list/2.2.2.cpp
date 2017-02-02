#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x) : val(x),next(NULL){}
};

class Solution{
public:
	ListNode *reverseBetween(ListNode *head,int m,int n){
		ListNode dummy(-1);
		dummy.next = head;

		ListNode *prev = &dummy;
		for(int i=0;i<m-1;i++)
			prev = prev->next;
		ListNode * const head2 = prev;

		prev = head2->next;
		ListNode *cur = prev->next;
		for(int i=m;i<n;++i){
			prev->next = cur->next;
			cur->next = head2->next;
			head2->next = cur;//head insert method 
			cur = prev->next;
		}
		return dummy.next;
	}
};
int main(){

	return 0;
}