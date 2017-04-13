#include<iostream>
#include<vector> 
#include<limits.h>
#include<algorithm>
using namespace std;

class Solution{
public:
	int myAtoi(const string& str){
		int num = 0;
		int sign = 1;
		const int n = str.size();
		int i = 0;
		while(str[i] == ' ' && i < n) i++;
		if(str[i] == '+'){
			i++;
		}else if(str[i] == '-'){
			sign = -1;
			i++;
		}
		for(;i< n;i++){
			if(str[i] < '0' || str[i] > '9')
				break;
			cout << "the value of i is " << str[i] << endl;
			if(num > INT_MAX/10 && (str[i] - '0') > INT_MAX%10){
				return sign == -1 ? INT_MIN : INT_MAX;
			}
			num = num * 10 + str[i] - '0';
			cout << "the num is " << num << endl;
		}
		return num * sign;
	}


	
};
 



class Solution1 {
public:
   string addBinary(string a, string b) {
     	if(a.empty()) a = "0";
     	if(b.empty()) b = "0";   
     	int carry = 0;
     	string result;
     	auto pa = a.rbegin(),pb = b.rbegin();
     	while(pa < a.rend() && pb < b.rend()){
     		int numSum = *pa - '0' + *pb - '0' + carry;
 			carry = numSum/2;
 			numSum = numSum%2;
     		result.insert(result.begin(),numSum+'0');
     		pa++,pb++;
     	}
     	while(pa < a.rend()){
     		result.insert(result.begin(),*pa++);
     	}
     	while(pb < b.rend()){
     		result.insert(result.begin(),*pb++);
     	}
     	if(carry == 1) result.insert(result.begin(),'1');


     	return result;
    }



};








struct ListNode{
	int val;
	ListNode* prev,*next;
	ListNode(int x):val(x),prev(nullptr),next(nullptr){}
};




class DoubleLinkList{
public:
	ListNode* createLinkList(vector<int> vec){
		ListNode dummy(-1);
		ListNode* pLinkList = &dummy;
		for(auto val:vec){
			pLinkList->next = new ListNode(val); 
			pLinkList->next->prev = pLinkList;
			pLinkList = pLinkList->next;
		}
		dummy.next->prev = nullptr;
		return dummy.next;
	}
	void deleteNode(ListNode* head,int num){
		ListNode* phead = head;
		while(phead){
			if(phead->val == num){
				phead->prev->next = phead->next;
				phead->next->prev = phead->prev;
				delete phead;
				break;
			}
			phead = phead->next;
		}

	}

};




int main(){
	vector<int> linkNode({1,2,3,4,5,6});
	auto ret = DoubleLinkList().createLinkList(linkNode);
	ListNode* head = ret;
	DoubleLinkList().deleteNode(head,4);
	while(head){
		cout << head->val << endl;
		head = head->next;
	}




	return 0;
}