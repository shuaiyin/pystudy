#include<iostream>
#include<unordered_map>
using namespace std;

struct RandomListNode{
	int label;
	RandomListNode* next,*random;
	RandomListNode(int x):label(x),next(nullptr),random(nullptr){}
};

class Solution {
public:
	//the method using extra space(unordered_map).  ac successed 
    RandomListNode* Clone(RandomListNode* pHead){
    	unordered_map<RandomListNode*,RandomListNode*> nodeMap;
    	RandomListNode* pHeadTemp = pHead;
    	RandomListNode cloneRandomList(-1);
    	RandomListNode* pCloneRandomList = &cloneRandomList;
    	while(pHeadTemp){
    		pCloneRandomList->next = new RandomListNode(pHeadTemp->label);
    		nodeMap.insert(make_pair(pHeadTemp,pCloneRandomList->next));
    		pCloneRandomList = pCloneRandomList->next;
    		pHeadTemp = pHeadTemp->next;
    	}

    	//second step 
    	pHeadTemp = pHead;
    	pCloneRandomList = cloneRandomList.next;
    	while(pHeadTemp){
    		if(pHeadTemp->random){
    			pCloneRandomList->random = nodeMap[pHeadTemp->random];
    		}
    		pHeadTemp = pHeadTemp->next;
    		pCloneRandomList = pCloneRandomList->next;
    	}
    	return cloneRandomList.next;
    }
    //the method do not use extra space (recommend) .still some problem ....but not found!!ac failed 
    RandomListNode* CloneOther(RandomListNode* pHead){
    	RandomListNode* pHeadTemp = pHead; 
    	while(pHeadTemp){
    		RandomListNode* node = new RandomListNode(pHeadTemp->label);
    		node->next = pHeadTemp->next;
    		pHeadTemp->next = node;
    		pHeadTemp = pHeadTemp->next->next;
    	}
    	pHeadTemp = pHead;
    	while(pHeadTemp){
    		if(pHeadTemp->random) pHeadTemp->next->random = pHeadTemp->random->next; 
    		pHeadTemp = pHeadTemp->next->next;
    	}
    	RandomListNode dummy(-1);//clone 
    	RandomListNode* pClone = &dummy;
    	pHeadTemp = pHead;
    	while(pHeadTemp){
    		pClone->next = pHeadTemp->next;
    		pHeadTemp = pHeadTemp->next->next;
    		pClone = pClone->next;
    	}
    	return dummy.next;

    	/*
    	RandomListNode* pCloneHead = pHead->next;
    	pHeadTemp = pHead->next->next;
    	while(pHeadTemp){
    		pCloneHead->next = pHeadTemp->next;
    		pHeadTemp = pHeadTemp->next->next;
    		pCloneHead = pCloneHead->next;
    	}
    	return pHead->next;
    	*/
    }
};






int main(){
	RandomListNode dummy(1);
	RandomListNode* temp = &dummy;
	temp->next = new RandomListNode(2);
	temp->next->next = new RandomListNode(3);
	temp->next->next->next = new RandomListNode(4);
	temp->next->next->next->random = temp;
	temp->next->random = temp->next->next;
	temp->random = temp->next;
	auto ret = Solution().CloneOther(temp);
	while(ret){
		cout << ret->label << endl;
		if(ret->random) cout << "the random value is " << ret->random->label << endl;
		ret = ret->next;
	}
	return 0;
	while(temp){
		cout << temp->label << endl;
		
		temp = temp->next;
	}
	return 0;
}