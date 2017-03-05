#include<iostream>
#include<vector>
using namespace std;

struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

class Solution{
public:
	vector<vector<int>> pathSum(TreeNode* root,int sum){
		vector<vector<int>> result;
		vector<int> temp;
		pathSum(root,result,temp,sum);
	}

private:
	void pathSum(TreeNode* root,vector<vector<int>>& result,vector<int>& temp,int sum){
		if(root == nullptr) return;
		temp.push_back(root->val);
		if(root->left == nullptr && root->right == nullptr){
			if(root->val == sum){
				result.push_back(temp);
			}
		}
		pathSum(root->left,result,temp,sum-root->val);
		pathSum(root->right,result,temp,sum-root->val);
		temp.pop_back();
	}

};

int main(){
	return 0;
}