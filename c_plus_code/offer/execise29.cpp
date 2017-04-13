#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	int MoreThanHalfNum_Solution(vector<int> numbers) {
		auto size = numbers.size();
		if(!size) return 0;
		int middle = size >> 1;
		int start = 0;
		int end = size - 1;
		int index = Partition(numbers,start,end);
		while(index != middle){
			if(index > middle){
				end = index - 1;
				index = Partition(numbers,start,end);
			}else{
				start = index + 1;
				index = Partition(numbers,start,end);
			}
		}
		int result = numbers[middle];
		return result;
    }
private:
	int Partition(vector<int> numbers,int start,int end){

		while(start != end){

		}
		return 0;

	}


};


int main(){
	vector<int> inputVec({1,2,3,2,2,2,5,4,2});
	auto ret = Solution().MoreThanHalfNum_Solution(inputVec);

	return 0;
}

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
	//cow net ac 
	void Mirror(TreeNode *pRoot) {
		if(!pRoot) return;
		if(pRoot->left||pRoot->right){
			TreeNode* temp = pRoot->right;
			pRoot->right = pRoot->left;
			pRoot->left = temp;

		}
		Mirror(pRoot->left);
		Mirror(pRoot->right);
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
	Solution().Mirror(ret);
	Solution().preOrderTra(ret);





	return 0;
}
