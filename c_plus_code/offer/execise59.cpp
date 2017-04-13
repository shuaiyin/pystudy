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
    bool isSymmetrical(TreeNode* pRoot){
        return isSymmetrical(pRoot,pRoot);
    }

    bool isSymmetrical(TreeNode* pRoot1,TreeNode* pRoot2){
        if(pRoot1 == nullptr && pRoot2 == nullptr)
            return true;
        if(pRoot1 == nullptr || pRoot2 == nullptr)
            return false;
        if(pRoot1->val != pRoot2->val)
            return false;
        return isSymmetrical(pRoot1->left,pRoot2->right) && 
               isSymmetrical(pRoot1->right,pRoot2->left);
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