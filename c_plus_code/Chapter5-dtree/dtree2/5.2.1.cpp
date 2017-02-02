#include<iostream>
using namespace std;

struct TreeNode{
  int val;
  TreeNode * left;
  TreeNode * right;
  TreeNode(int x): val(x),left(NULL),rigth(NULL){}
};

class Solution{
public:
	TreeNode * buildTree(vector<int>& preorder,vector<int> &inorder){
		return buildTree(begin(preorder),end(preorder),begin(inorder),end(inorder));
		
	}

};