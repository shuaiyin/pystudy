#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

class Solution{
public:
	//leetcode ac 0305
	TreeNode* sortedArrayToBST(vector<int>& nums){
		return sortedArrayToBST(nums.begin(),nums.end());
	}

	template<typename RandomAccessIterator>
	TreeNode* sortedArrayToBST(RandomAccessIterator first,RandomAccessIterator last){
		const auto length = distance(first,last);
		if(length <= 0) return nullptr;//terminal 
		//combine three aspects 
		auto mid = first + length/2;
		TreeNode* root = new TreeNode(*mid);
		root->left = sortedArrayToBST(first,mid);
		root->right = sortedArrayToBST(mid+1,last);
		return root;
	} 	


};

int main(){
	vector<int> vec({1,2,3,4,5,6});
	Solution().sortedArrayToBST(vec);
	return 0;
}