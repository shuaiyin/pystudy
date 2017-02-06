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
		if(!head ||!head->next) return head;//if only single node or no node 
		ListNode dummy(-1);
		dummy.next = head;
		for(ListNode* prev=&dummy,*cur=prev->next,*next=cur->next;
			next;
			prev=cur,cur=cur->next,next=cur?cur->next:NULL){
			prev->next = next;
			next->next = cur;
		}
		return dummy.next;
	}
    //unallowed method,but easy know 
	ListNode* swapPairsSec(ListNode *head){
		ListNode *p = head;
		while(p && p->next){
			swap(p->val,p->next->val);
			p = p->next->next;
		}
		return head;
	}

};


void test1(){
	ListNode dummy(-1);
	auto temp = &dummy;
	temp->next = new ListNode(1);
	temp = temp->next;
	temp->next = new ListNode(2);
	temp = &dummy;
	swap(temp->val,temp->next->val);
	while(temp){
		cout << temp->val << endl;
		temp = temp->next;
	}
	/*
	orgin: -1 1  2
	after 1 -1 2 
	*/
}

void test2(){
	int testarr[] = {1,2,3,4,5};
	ListNode dummy(0);
	auto temp = &dummy;
	for(auto v:testarr){
		temp->next = new ListNode(v);
		temp = temp->next;
	}
	auto result = Solution().swapPairsSec(&dummy);
	for(temp=result;temp;temp=temp->next){
		cout << temp->val << endl;
	}
}

int main(){
	test2();
	return 0;
	char a = 'd';
	char *b = &a,*c=&a;
	cout << *c << endl;
	return 0;
	ListNode dummy(-1);
	ListNode *tmp;
	tmp = &dummy;
	for(int i=1;i<5;i++){
		tmp->next = new ListNode(i);
		tmp = tmp->next;
	}
	for(auto it=&dummy;it;it=it->next){
		cout << it->val << endl;
	}
	return 0;
}