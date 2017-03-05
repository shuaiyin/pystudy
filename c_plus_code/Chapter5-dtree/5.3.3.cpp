#include<iostream>
#include<vector>
#include<algorithm>
#include<limits.h>
using namespace std;

struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};


class Solution{
public:
    bool isValidBST(TreeNode* root){
        return isValidBST(root,INT_MIN,INT_MAX);
    }

    bool isValidBST(TreeNode* root,int lower,int upper){
        if(root == nullptr) return true;
        return root->val > lower && root->val < upper && 
               isValidBST(root->left,lower,root->val) && 
               isValidBST(root->right,root->val,upper);  

    }
};

int main(){
    cout << INT_MAX << endl;
	return 0;
}