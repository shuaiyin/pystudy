#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x) : val(x),next(NULL){}
};


ListNode *createList(int n){
	ListNode head(-1);
	ListNode *prev = &head;
	ListNode *prev2;
	prev2 = &head;
	int val;
	for(int i=0;i<n;++i){
		cin >> val;
		//allocate the memory space for new node 
		prev->next = new ListNode(val);
		prev = prev->next;
	}
	prev->next = NULL;
	// return head->next;
	return &head;
}

ListNode * partition(ListNode* head, int x){
	ListNode left_dummy(-1);//head node 
	ListNode right_dummy(-1);//head node 

	auto left_cur = &left_dummy;
	auto right_cur = &right_dummy;
	for(ListNode * cur=head;cur; cur=cur->next){
		continue;
	}
}
int main(){
	//create listnode test 
	ListNode head(-1);
	ListNode *prev = &head;
	int val;
	for(int i=0;i<4;i++){
		cin >> val;
		prev->next = new ListNode(val);
		prev = prev->next;
	}
	cout << "the listnode you input is " << endl;
	for(ListNode* cur = &head;cur;cur=cur->next){
		cout << "the value is " << cur->val << endl;
	}
	/*
		ListNode head(-1);
	ListNode *prev = &head;
	ListNode *prev2;
	prev2 = &head;
	int val;
	for(int i=0;i<n;++i){
		cin >> val;
		//allocate the memory space for new node 
		prev->next = new ListNode(val);
		prev = prev->next;
	}
	prev->next = NULL;
	// return head->next;
	return &head;

*/
	return 0;
	ListNode left_dummy(1);
	// cout << left_dummy.val << endl;
	ListNode next_node(100);
	ListNode third_node(101);
	left_dummy.next = &next_node;
	left_dummy.next->next = &third_node;
	int len = 0;
	for(ListNode *cur = &left_dummy;cur;cur=cur->next){
		cout << cur->val << endl;
		cout << cur->next << endl;
	}
	return 0;
}