#include<iostream>
#include<vector>
using namespace std;

struct LinkNode{
	int val;
	LinkNode * next;
	LinkNode(int x):val(x),next(NULL){}
};
//well done
class Solution{
public:
	LinkNode* rotateRight(LinkNode* head,int k){
		if(head == NULL || k==0) return head;
		int len = 1;
		LinkNode* p = head;
		while(p->next){
			len++;
			p = p->next;
		}
		k = len - k%len;
		p->next = head;//head-tail connect
		for(int step=0;step<k;step++){
			p = p->next;//continue go right 
		}
		head = p->next;//new head
		p->next = NULL;//broke the linklist circle
		return head;
	}
};

int main(){
	int testarr[] = {1,2,3,4,5,6};
	LinkNode head(0);
	LinkNode* temp = &head;
	for(auto val:testarr){
		temp->next = new LinkNode(val);
		temp = temp->next;
	}
	LinkNode* rethead = Solution().rotateRight(&head,0);
	temp = rethead;
	while(temp){
		cout << temp->val << endl;
		temp = temp->next;
	}//0 1 2 3 4 5 6
	rethead = Solution().rotateRight(&head,3);
	temp = rethead;
	while(temp){
		cout << temp->val << endl;
		temp = temp->next;
	}//4 5 6 0 1 2 3
	return 0;
}