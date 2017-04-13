#include<iostream>
#include<math.h>
using namespace std;


struct TreeNode{
	int itemCnt;
	int weight;
	TreeNode* left,*right;
	TreeNode(int itemCnt,int weight):itemCnt(itemCnt),weight(weight),
	         left(nullptr),right(nullptr){}
};


class Solution{
private:
	int p;
	int q;
public:
	Solution(int p,int q){
		p = p;
		q = q;
	}
	void reachEnd(TreeNode* root,int weight,int itemCnt,bool hasItem){
		TreeNode* tmp = root;
		if(hasItem) return weight/100.0*
		reachEnd(root->left,weight-p,itemCnt++) 
		reachEnd(root->right,weight-p,itemCnt);


}

}


int main(){
	int p,q,n;
	while(cin >> p >> q >> n){
       TreeNode root(0,100);
       reachEnd(root->left,p,1,true);//left reach end 
       reachEnd(root->right,100-p,0,false);


	}
	return 0;
}