#include<iostream>
#include<vector>
#include<stack>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}

};

class Solution{
public:
	//using stack  cow net ac 
    ListNode* FindFirstCommonNodeUsingStack( ListNode* pHead1, ListNode* pHead2) {
    	if(!pHead2 || !pHead1) return nullptr;
    	stack<ListNode*> stk1;//save first link 
    	stack<ListNode*> stk2;//save second link
    	while(pHead1){
    		stk1.push(pHead1);
    		pHead1 = pHead1->next;
    	}
    	while(pHead2){
    		cout << pHead2->val << endl;
    		stk2.push(pHead2);
    		pHead2 = pHead2->next;
    	}
    	ListNode* commonNode = nullptr;
    	while(stk1.size() && stk2.size()){
    		if(stk1.top() == stk2.top()){
    			commonNode = stk1.top();
    			stk1.pop();
    			stk2.pop();
    		}else{
    			break;
    		}    		
    	}
    	return commonNode;
    }

    //using num count 
    ListNode* FindFirstCommonNodeUsingCount(ListNode* pHead1,ListNode* pHead2){
    	if(!pHead1 || !pHead2) return nullptr;
    	ListNode* pHead1Temp = pHead1,*pHead2Temp = pHead2;
    	int linkOneLen = 0,linkSecLen = 0;
    	while(pHead1Temp){
    		linkOneLen++;
    		pHead1Temp = pHead1Temp->next;
    	}
    	while(pHead2Temp){
    		linkSecLen++;
    		pHead2Temp = pHead2Temp->next;
    	}
    	int sub	= linkSecLen - linkOneLen;
    	pHead1Temp = pHead1;
    	pHead2Temp = pHead2;
    	if(sub > 0){
    		while(sub--)
    			pHead2Temp = pHead2Temp->next;
    			
    	}else{
    		while(sub++)
    			pHead1Temp = pHead1Temp->next;
    	}
    	while(pHead1Temp){
    		if(pHead1Temp != pHead2Temp){
    			pHead2Temp = pHead2Temp->next;
    			pHead1Temp = pHead1Temp->next;
    		}else{
    			break;
    		}
    	}
    	return pHead1Temp;


    }

};



int main(){
	ListNode* pHead1 = new ListNode(4);
	pHead1->next = new ListNode(6);
	ListNode* commonOne = new ListNode(8);
	pHead1->next->next = commonOne;
	ListNode* commonSec = new ListNode(9);
	pHead1->next->next->next = commonSec;

	////
	ListNode* pHead2 = new ListNode(7);
	pHead2->next = commonOne;
	auto ret = Solution().FindFirstCommonNodeUsingCount(pHead1,pHead2);
	cout << ret->val << endl;

	return 0;
}