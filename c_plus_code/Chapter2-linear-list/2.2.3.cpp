#include<iostream>
#include<vector>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x): val(x),next(NULL){}
};
//well done  const space used,for that it not new ListNode
class Solution{
public:
	ListNode* partition(ListNode* head,int x){
		ListNode left_dumpy(-1);//head node 
		ListNode right_dummy(-1);//head node 
		auto left_cur = &left_dumpy;
		auto right_cur = &right_dummy;
		for(ListNode* cur=head;cur;cur=cur->next){
			if(cur->val < x){
				left_cur->next = cur;
				left_cur = cur;
			}else{
				right_cur->next = cur;
				right_cur = cur;
			}
		}
		left_cur->next = right_dummy.next;
		right_cur->next = NULL;
		return left_dumpy.next;
	}
};

int main(){
	int testarr[] = {1,3,4,5,2,2,6};
	ListNode dummy(-1);
	ListNode* tmp = &dummy;
	for(auto val:testarr){
		tmp->next = new ListNode(val);
		tmp = tmp->next;
	}
	tmp = &dummy;
	auto ret = Solution().partition(tmp->next,5);
	for(tmp=tmp->next;tmp;tmp=tmp->next){
		cout << tmp->val << endl;
	}// 1 3 4 2 2 5 6 

	return 0;
	ListNode dummyA(-1);
	ListNode dummyB(-1);
	ListNode* tmp = &dummyA;
	for(int i=0;i<3;i++){
		tmp->next = new ListNode(i);
		tmp = tmp->next;
	}
	tmp = &dummyA;
	ListNode* tmpB = &dummyB;
	tmpB->next = tmp->next;
	cout << tmpB->val << endl;
	cout << tmpB->next->val << endl;



}