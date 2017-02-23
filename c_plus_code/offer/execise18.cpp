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


class Solution {
public:
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2){
    	bool result = false;
    	if(pRoot1 && pRoot2){
    		if(pRoot1->val == pRoot2->val){
    			result = DoesTree1HaveTree2(pRoot1,pRoot2);
    		}
    		if(!result) result = HasSubtree(pRoot1->left,pRoot2);
    		if(!result) result = HasSubtree(pRoot1->right,pRoot2);

    	}
    	return false;

    }

    TreeNode* reConstructBinaryTree(vector<int>& pre,vector<int>& vin) {
    	if(pre.empty() && vin.empty()) return nullptr;
    	// if(pre.empty()||vin.empty()) return nullptr;//this sentence is not neccessy
    	return reConstructBinaryTree(pre.begin(),pre.end(),vin.begin(),vin.end());
    }

    void preOrderTra(TreeNode* head){
		if(!head) return;
		cout << head->val << endl;
		preOrderTra(head->left);
		preOrderTra(head->right);
	}	

private:
	bool DoesTree1HaveTree2(TreeNode* pRoot1,TreeNode* pRoot2){
		if(!pRoot2) return true;
		if(!pRoot1) return false;
		if(pRoot1->val != pRoot2->val) return false;
		return DoesTree1HaveTree2(pRoot1->left,pRoot2->left) &&
			   DoesTree1HaveTree2(pRoot1->right,pRoot2->right);
	}
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
	vector<int> preorder({1,2,4,5,7,10,8,3,6,9});
	vector<int> inorder({4,2,10,7,5,8,1,6,9,3});
	auto ret = Solution().reConstructBinaryTree(preorder,inorder);





	return 0;
}
