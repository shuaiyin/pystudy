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
	bool IsBalanced_Solution(TreeNode* pRoot) {
		if(pRoot == nullptr) return true;
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


		//cow net ac 0225
	int TreeDepthRecurse(TreeNode* pRoot){
		if(!pRoot) return 0;
		if(!pRoot->left && !pRoot->right){//leaf node 
			return 1;
		}
		int leftDepth = TreeDepth(pRoot->left) + 1;
		int rightDepth = TreeDepth(pRoot->right) + 1;
		int maxLen = leftDepth > rightDepth ? leftDepth:rightDepth;
		return maxLen;
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
	vector<int> preorder({1,2,4,5,7,10,8,3,6,9});
	vector<int> inorder({4,2,10,7,5,8,1,6,9,3});
	auto ret = Solution().reConstructBinaryTree(preorder,inorder);
	// Solution().preOrderTra(ret);
	auto rett = Solution().TreeDepth(ret);
	cout << rett << endl;





	return 0;
}
