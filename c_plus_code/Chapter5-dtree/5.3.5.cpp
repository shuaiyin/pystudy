#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};

class Solution{
public:
	//leetcode some error 
	TreeNode* sortedListToBST(ListNode* head) {
		return sortedListToBST(head,listLength(head));
    }

    TreeNode* sortedListToBST(ListNode* head,int len){
    	if(len == 0) return nullptr;
    	if(len == 1) return new TreeNode(head->val);
    	TreeNode* root = new TreeNode(nth_node(head,len/2+1)->val);
    	root->left = sortedListToBST(head,len/2);
    	root->right = sortedListToBST(nth_node(head,len/2+2),(len-1)/2);
    	return root;
    }

    int listLength(ListNode* head){
    	int len;
    	while(head){
    		len++;
    		head = head->next;
    	}
    	return len;
    }

    ListNode* nth_node(ListNode* head,int num){
    	while(num--){
    		head = head->next;
    	}
    	return head;
    }




};

int main(){
	return 0;
}