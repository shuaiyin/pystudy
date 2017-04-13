#include<iostream>
#include<stack>
#include<vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) :val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
	//cow net ac 
    vector<vector<int> > Print(TreeNode* pRoot) {
    	vector<vector<int>> result;
    	if(pRoot == nullptr) return result;
    	stk1.push(pRoot);
    	vector<int> eachLayer;
    	eachLayer.push_back(pRoot->val);
    	result.push_back(eachLayer);
    	while(true){
    		eachLayer = vector<int>();
    		while(!stk1.empty()){//not odd 
    			TreeNode* topNode = stk1.top();
				if(topNode->right){
					eachLayer.push_back(topNode->right->val);
					stk2.push(topNode->right);
				}
				if(topNode->left){
					eachLayer.push_back(topNode->left->val);
					stk2.push(topNode->left);
				}
    			stk1.pop();
    		}
    		if(eachLayer.empty()) break;
			result.push_back(eachLayer);
			eachLayer = vector<int>();
    		while(!stk2.empty()){
    			TreeNode* topNodeStk2 = stk2.top();
    			if(topNodeStk2->left){
    				eachLayer.push_back(topNodeStk2->left->val);
    				stk1.push(topNodeStk2->left);
    			}
    			if(topNodeStk2->right){
    				eachLayer.push_back(topNodeStk2->right->val);
    				stk1.push(topNodeStk2->right);
    			}
    			stk2.pop();
    		}
    		if(eachLayer.empty()) break;
    		result.push_back(eachLayer);
    		
    	}
		return result;        
    }

private:
	stack<TreeNode*> stk1;
	stack<TreeNode*> stk2;
    
};


int main(){
	TreeNode head(5);
	TreeNode* phead = &head;
	phead->left = new TreeNode(4);
	phead->left->left = new TreeNode(3);
	phead->left->left->left = new TreeNode(2);
	auto ret = Solution().Print(&head);
	cout << "the size of ret is " <<  ret.size() << endl;
	for(auto vecVal:ret){
		for(auto val:vecVal) cout << val << " ";
		cout << endl;
	}

	return 0;
}