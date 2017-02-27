#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


struct TreeNode{
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

class Solution{
public:
	TreeNode* Convert(TreeNode* pRootOfTree){
		return new TreeNode(0);
        
    }

    TreeNode* reConstructBinaryTree(vector<int>& pre,vector<int>& vin) {
    	if(pre.empty() && vin.empty()) return nullptr;
    	// if(pre.empty()||vin.empty()) return nullptr;//this sentence is not neccessy
    	return reConstructBinaryTree(pre.begin(),pre.end(),vin.begin(),vin.end());
    }

    void inOrderTraverse(TreeNode* root){
    	if(!root) return;
    	inOrderTraverse(root->left);
    	cout << root->val << endl;


    }

private:
	template<typename pIterator>
	TreeNode* reConstructBinaryTree(pIterator preFirst,pIterator preLast,pIterator inFirst,pIterator inLast){
		if(preFirst == preLast) return nullptr;
		TreeNode* head = new TreeNode(*preFirst);
		auto leftValPos = find(inFirst,inLast,*preFirst);
		auto leftLen = distance(inFirst,leftValPos);
		if(preFirst != preLast){
			head->left = reConstructBinaryTree(next(preFirst),next(preFirst,leftLen+1),
											   inFirst,leftValPos);
			head->right = reConstructBinaryTree(next(preFirst,leftLen+1),preLast,
											   next(leftValPos),inLast);
		}
		return head;
	}
};


int main(){
	vector<int> preorder({10,6,4,8,14,12,16});
	vector<int> inorder({4,6,8,10,12,14,16});
	auto ret = Solution().reConstructBinaryTree(preorder,inorder);
	Solution().inOrderTraverse(ret);


	return 0;
}