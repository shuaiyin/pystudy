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

	//cow net ac,but need very more attention 
	TreeNode* Convert(TreeNode* pRootOfTree){
		TreeNode* pLastNodeInList = nullptr;
		ConvertNode(pRootOfTree,&pLastNodeInList);
		//pLastNodeInList point to the end of double way linklist 
		//we need to return head node 
		TreeNode* pHeadOfList = pLastNodeInList;
		while(pHeadOfList != nullptr && pHeadOfList->left != nullptr){
			pHeadOfList = pHeadOfList->left;
		}
		return pHeadOfList;
	}

	void ConvertNode(TreeNode* pNode,TreeNode** pLastNodeInList){
		if(pNode == nullptr) return;
		TreeNode* pCurrent = pNode;
		if(pCurrent->left != nullptr){
			ConvertNode(pCurrent->left,pLastNodeInList);
		}
		pCurrent->left = *pLastNodeInList;
		if(*pLastNodeInList != nullptr)
			(*pLastNodeInList)->right = pCurrent;
		*pLastNodeInList = pCurrent;
		if(pCurrent->right){
			ConvertNode(pCurrent->right,pLastNodeInList);
		}



	}


    TreeNode* reConstructBinaryTree(vector<int>& pre,vector<int>& vin) {
    	if(pre.empty() && vin.empty()) return nullptr;
    	// if(pre.empty()||vin.empty()) return nullptr;//this sentence is not neccessy
    	return reConstructBinaryTree(pre.begin(),pre.end(),vin.begin(),vin.end());
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
	Solution().Convert(ret);


	return 0;
}