#include<iostream>
#include<vector>
using namespace std;


struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};

class Solution{
public:
	ListNode* reverse(ListNode* head){
		if(head == nullptr || head->next == nullptr) return head;
		ListNode* prev = head;
		for(ListNode* curr )
	}

};

int main(){
	return 0;
}