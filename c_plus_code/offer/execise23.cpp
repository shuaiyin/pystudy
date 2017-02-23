#include<iostream>
#include<vector>
#include<deque>
#include<algorithm>
using namespace std;

struct TreeNode{
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

//cow net ac 
class Solution {
public:
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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
    	if(!root) return vector<int>();
    	vector<int> valVec;
    	deque<TreeNode*> dequeTreeNode; 
    	dequeTreeNode.push_back(root);

    	while(dequeTreeNode.size()){
    		auto popNode = dequeTreeNode.front();
    		dequeTreeNode.pop_front();
    		valVec.push_back(popNode->val);
    		if(popNode->left) dequeTreeNode.push_back(popNode->left);
    		if(popNode->right) dequeTreeNode.push_back(popNode->right);
    	}
    	return valVec;
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
	auto retVec = Solution().PrintFromTopToBottom(ret);
	for(auto val:retVec) cout << val << endl;
	return 0;

	deque<int> dequeTest({1,2,3,4,5});
	dequeTest.push_back(6);
	cout << "the size is  " << dequeTest.size() << endl;
	dequeTest.pop_front();
	cout << "the size is  " << dequeTest.size() << endl;
	while(dequeTest.size()){
		cout << dequeTest.front() << endl;
		dequeTest.pop_front();
	}
	// for(deque<int>::iterator it = dequeTest.begin();it!=dequeTest.end();it++) cout << *it << endl; 
	return 0;

}
