#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<string>
using namespace std;

struct TreeNode{
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x):val(x),left(NULL),right(NULL){}
};



class SolutionDg{
public:
	void preOrder(TreeNode* root){
		if(!root) return;
		cout << root->val << endl;
		preOrder(root->left);
		preOrder(root->right);
	}
	void inOrder(TreeNode* root){
		if(!root) return;
		inOrder(root->left);
		cout << root->val << endl;
		inOrder(root->right);
	}
	void postOrder(TreeNode* root){
		if(!root) return;
		postOrder(root->left);
		postOrder(root->right);
		cout << root->val << endl;
	}
};


class Solution{
public:
	TreeNode* buildTree(vector<int> &preorder,vector<int>& inorder){
		return buildTree(preorder.begin(),preorder.end(),inorder.begin(),inorder.end());
	}

	template<typename InputIterator>
	TreeNode* buildTree(InputIterator pre_first,InputIterator pre_last,
						InputIterator in_first,InputIterator in_last){
		if(pre_first == pre_last) return NULL;
		if(in_first == in_last) return NULL;
		auto root = new TreeNode(*pre_first);
		auto inRootPos = find(in_first,in_last,*pre_first);
		auto leftSize = distance(in_first,inRootPos);
		// cout << leftSize << endl;
		root->left = buildTree(next(pre_first),next(pre_first,leftSize+1),
							in_first,next(in_first,leftSize));
		root->right = buildTree(next(pre_first,leftSize+1),pre_last,next(inRootPos),in_last);
		return root;
	}
	vector<int> preorderTraveral(TreeNode* root){
		vector<int> result;
		stack<const TreeNode*> s;
		if(root != NULL) s.push(root);
		while(!s.empty()){//if is empty return 1 
			const TreeNode*p = s.top();
			s.pop();
			result.push_back(p->val);
			if(p->right != NULL) s.push(p->right);
			if(p->left != NULL) s.push(p->left);
		}
		return result;
	}

	vector<int> inorderTraveral(TreeNode* root){
		vector<int> result;
		stack<const TreeNode*> s;
		const TreeNode* p = root;
		while(!s.empty()||p!=NULL){//if is empty,then return 1 else return 0
			if(p!= NULL){
				s.push(p);
				p = p->left;
			}else{
				p = s.top();
				s.pop();
				result.push_back(p->val);
				p = p->right;
			}
		}
		return result;
	}

	int getNodeNum(TreeNode* root){//get node num of the specify tree
		if(!root) return 0;//NULL TREE
		cout << root->val << ":";
		return getNodeNum(root->left) + getNodeNum(root->right) + 1; 
		return 0;
	}

	int getDepth(TreeNode* root){
		if(!root) return 0;
		int depthLeft = getDepth(root->left);
		int depthRight = getDepth(root->right);
		return depthLeft > depthRight ? (depthLeft+1):(depthRight+1);
	}





};

int main(){
	//construct a treenode and push into a stack
	TreeNode* root = new TreeNode(10);
	root->left = new TreeNode(9);
	root->right = new TreeNode(11);
	stack<const TreeNode*> stk;
	stk.push(root);
	stk.push(root->left);
	stk.push(root->right);
	while(!stk.empty()){
		const TreeNode* tn = stk.top();
		cout << tn->val << endl;
		stk.pop();

	}
	return 0;
    vector<int> vvv{1,2,3,4};
    auto ret = find(vvv.begin(),vvv.end(),3);
    cout << *ret << endl;
	return 0;
	vector<int> vec1 = {6,10,4,3,1,0,7,12};
	vector<int> vec2 = {4,10,3,1,6,12,7,0};
	auto treeRoot = Solution().buildTree(vec1,vec2);
	int num = Solution().getNodeNum(treeRoot);
	cout << num << endl;


	return 0;
}