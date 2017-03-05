#include<iostream>
#include<vector>
using namespace std;

struct TreeLinkNode{
	int val;
	TreeLinkNode* left,*right,*next;
	TreeLinkNode(int x):val(x),left(nullptr),right(nullptr),next(nullptr){}
	
};


class Solution{
public:
	void connect(TreeLinkNode* root){
		connect(root,null);
	}

private:
	void connect(TreeLinkNode* root,TreeLinkNode* sibling){
		if(root == nullptr) return;
		root->next = sibling;
		connect(root->left,root->right);


	}
};