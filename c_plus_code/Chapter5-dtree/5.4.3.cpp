#include<iostream>
using namespace std;

struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

class Solution{
public:
	//yes ,ac 
	bool hasPathSum(TreeNode* root,int sum){
		if(root == nullptr) return 0;
		if(root->left == nullptr && root->right == nullptr) return root->val == sum;
		return hasPathSum(root->left,sum-root->val) || hasPathSum(root->right,sum-root->val);
	}
};

int main(){
	return 0;
}