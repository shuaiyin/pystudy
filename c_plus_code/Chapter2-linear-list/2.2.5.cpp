#include<iostream>
using namespace std;

struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x) : val(x),next(NULL){}
};
//not well done 
class Solution{
public:
	ListNode *deleteDupicates(ListNode *head){
		if(!head||!head->next) return head;
		ListNode *p = head->next;
		if(head->val == p->val){
			while(p && head->val == p->val){
				ListNode* tmp = p;
				p = p->next;
				delete tmp;
			}
			delete head;
			return deleteDupicates(p);
		}else{
			head->next = deleteDupicates(head->next);
			return head;
		}

	}
};
int main(){
	ListNode head(0);
	int testarr[] = {1,2,3,4,5};
	auto temp = &head;
	for(auto val:testarr){
		temp->next = new ListNode(val);
		temp = temp->next;
	}
	auto result = Solution().deleteDupicates(&head);




	return 0;

}
