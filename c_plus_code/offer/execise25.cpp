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

	bool hasPathSum(TreeNode *root, int sum){
		if(!root) return false;
		if(!root->left && !root->right) return root->val == sum;
		return hasPathSum(root->left,sum-root->val) || hasPathSum(root->right,sum-root->val);
	}
	//cow net ac .but need more focus 
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
    	vector<vector<int>> result;
    	vector<int> cur;//center result
    	FindPath(root,expectNumber,cur,result);
    	return result;
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

	void FindPath(TreeNode* root,int expectNumber,vector<int>& cur,vector<vector<int>>& result){
		if(root == nullptr) return;
		cur.push_back(root->val);
		if(root->left == nullptr && root->right == nullptr && root->val == expectNumber) result.push_back(cur);
		FindPath(root->left,expectNumber-root->val,cur,result);
		FindPath(root->right,expectNumber-root->val,cur,result);
		cur.pop_back();
	}


};


void testRecurse(int val){
	if(!val) return;
	val--;
	cout << val << endl;

	testRecurse(val);
	testRecurse(val);
	cout << endl;

}

int main(){
	testRecurse(4);
	return 0;



	vector<int> preorder({1,2,4,8,12,3,6,11});
	vector<int> inorder({8,4,2,12,1,6,3,11});
	auto ret = Solution().reConstructBinaryTree(preorder,inorder);
	auto vecRet = Solution().FindPath(ret,15);
	for(auto vecval:vecRet){
		for(auto val:vecval) cout << val << ' ';
		cout << endl;
	}
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
