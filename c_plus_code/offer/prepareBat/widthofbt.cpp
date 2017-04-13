#include<iostream>
#include<vector>
#include<deque>
using namespace std;
struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

class Solution{
public:
	int getWidthOfBinaryTree(TreeNode* head){
		if(!head) return 0;
		if(head->left == nullptr && head->right == nullptr) return 1;
		deque<TreeNode* > treeDeque;
		treeDeque.push_back(head);
		int maxWidth = 1;
		while(true){
			int length = treeDeque.size();
			if(length > maxWidth) maxWidth = length;
			if(length == 0) break;
			while(length){
				TreeNode* frontVal = treeDeque.front();
				if(frontVal->left) treeDeque.push_back(frontVal->left);
				if(frontVal->right) treeDeque.push_back(frontVal->right);
				treeDeque.pop_front();
				length--;
			}

		}
		return maxWidth;
	}

};

int main(){
	TreeNode* head = new TreeNode(-1);
	head->left = new TreeNode(1);
	head->right = new TreeNode(2);
	head->left->left = new TreeNode(3);
	head->left->right = new TreeNode(4);
	head->right->left = new TreeNode(5);

	int width = Solution().getWidthOfBinaryTree(head);
	cout << width << endl;

	return 0;
	deque<int> d;
	d.push_back(3);
	d.push_back(4);
	d.push_back(5);
	while(!d.empty()){
		auto val = d.front();
		cout << val << endl;
		d.pop_front();
	}
	return 0;
}


//http://blog.csdn.net/morewindows/article/details/6946811