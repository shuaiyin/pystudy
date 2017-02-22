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
	TreeNode* ConstructTreeRecurse(vector<int>& preorder,vector<int>& inorder){
		return ConstructTreeRecurse(preorder.begin(),preorder.end(),inorder.begin(),inorder.end());
	}
	template<typename InputIterator> 
	TreeNode* ConstructTreeRecurse(InputIterator preFirst,InputIterator preLast,InputIterator inFirst,InputIterator inLast){
		if(preFirst == preLast || inFirst == inLast) return nullptr;
		auto head = new TreeNode(*preFirst);
		auto inRootPos = find(inFirst,inLast,*preFirst);
		auto leftLength = distance(inFirst,inRootPos);
		head->left = ConstructTreeRecurse(next(preFirst),next(preFirst,leftLength+1),inFirst,inRootPos);
		head->right = ConstructTreeRecurse(next(preFirst,leftLength+1),preLast,next(inRootPos),inLast);
		return head;
	}

	void preOrder(TreeNode* head){
		if(!head) return;
		cout << head->val << endl;
		preOrder(head->left);
		preOrder(head->right);
	}
};

int main(){
	vector<int> preorder({1,2,4,7,3,5,6,8});
	vector<int> inorder({4,7,2,1,5,3,8,6});
	auto ret = Solution().ConstructTreeRecurse(preorder,inorder);
	Solution().preOrder(ret);

	return 0;
}