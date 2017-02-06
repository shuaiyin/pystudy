#include<iostream>
#include<unordered_map>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(NULL){}
};

//no well done
class Solution{
public:
	bool hasCycle(ListNode* head){
		//set two pointer ,one fast ,other slow
		ListNode* slow = head,*fast = head;
		while(fast && fast->next){
			slow= slow->next;
			fast = fast->next->next;
			if(slow == fast) return true;
		}
		return false;
	}


};
int main(){
	//just test
	ListNode head(-1);
	auto tmp = &head;
	for(int i=0;i<5;i++){
		tmp->next = new ListNode(i);
		tmp = tmp->next;
	}

	//my way to find 
	for()
	return 0;
	tmp = &head;
	while(tmp){
		cout << tmp->val << endl;
		tmp = tmp->next;
	}

	return 0;
}