#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
using namespace std;

struct TreeNode{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x):val(x),left(NULL),right(NULL){}

};


class Solution{
public:
	TreeNode* buildTree(vector<int> &preorder,vector<int>&inorder){
		return buildTree(preorder.begin(),preorder.end(),inorder.begin(),inorder.end());
	}

	template<typename InputIterator> 
	TreeNode* buildTree(InputIterator
	pre_first,InputIterator pre_last,InputIterator
	in_first,InputIterator in_last)
	{ if(pre_first==pre_last) return NULL;
	if(in_first==in_last) return NULL; 
	auto root = new TreeNode(*pre_first);//same as TreeNode* root = new TreeNode(*pre_first);
	auto inRootPos = find(in_first,in_last,*pre_first);
	auto leftSize = distance(in_first,inRootPos); // root->left = buildTree(next(pre_first))

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

};


int main(){

	/*
int[] preOrder = { 6, 10, 4, 3, 1, 0, 7, 12 };
中序遍历：
int[] inOrder = { 4, 10, 3, 1, 6, 12, 7, 0 };
	*/
	// stack<int> stk;
	// auto ie = stk.empty();
	// cout << ie << endl;
	vector<int> prevec{6,10,4,3,1,0,7,12};
	vector<int> invec{4,10,3,1,6,12,7,0};
	//auto ctree = Solution().buildTree(prevec,invec);
	//preorder 
	//vector<int> retvec = Solution().preorderTraveral(ctree);
	return 0;

/*
	const TreeNode * tn = new TreeNode(25);
	return 0;

	auto root = new TreeNode(*prevec.begin());
	auto inRootPos = find(invec.begin(),invec.end(),*prevec.begin());
	auto leftSize = distance(invec.begin(),inRootPos);

	return 0;
	vector<int> vec{1,2,3,4};
	vector<int>::iterator it = find(vec.begin(),vec.end(),2);
	auto dis = distance(vec.begin(),vec.begin()+2);
	cout << dis << endl;
	cout << *it << endl;
	return 0;
	TreeNode* newnode = new TreeNode(9);

*/
}