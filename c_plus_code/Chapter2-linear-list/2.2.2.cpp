#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x) : val(x),next(nullptr){}
};

class Solution{
public:
	ListNode *reverseBetween(ListNode *head,int m,int n){
		if(head == nullptr ||head->next == nullptr) return head;
		ListNode dummy(-1);
		dummy.next = head;
		ListNode *prev = &dummy;
		for(int i=0;i<m-1;i++){
			prev = prev->next;
		}
		ListNode* const head2  = prev;//head insert head node 
		cout << head2->val << endl;
		ListNode* cur = prev->next;
		for(int i = m;i<n;i++){
			prev->next = cur->next;
			cur->next = head2->next;
			head2->next = cur;//head insert 
			cur = prev->next;
		}
		return dummy.next;


	}
};
int main(){
	ListNode dummy(-1);
	ListNode* prev = &dummy;
	int arr[] = {1,2,3,4,5,6};
	for(auto val:arr){
		prev->next = new  ListNode(val);
		prev = prev->next;
	}
	Solution so = Solution();
	ListNode ret = so.reverseBetween(dummy.next,3,6);
	while(ret != nullptr){
		cout << ret->val << endl;
		ret = ret->next;
	}
	return 0;
}