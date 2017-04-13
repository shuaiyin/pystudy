#include<iostream>
#include<stack>
#include<vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) :val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* KthNode(TreeNode* pRoot, int k){
        return KthNode(pRoot,k,0);

    }

    void inOrderTransfer(TreeNode* pRoot){
        if(!pRoot) return;
        if(!pRoot->left && !pRoot->right){
            cout << pRoot->val << endl;
            return ;
        }
        inOrderTransfer(pRoot->left);
        cout << pRoot->val << endl;
        inOrderTransfer(pRoot->right);
    }
    
};


int main(){
	TreeNode head(5);
	TreeNode* phead = &head;   
	phead->left = new TreeNode(4);
	phead->left->left = new TreeNode(3);
	phead->left->left->left = new TreeNode(2);

	return 0;
}