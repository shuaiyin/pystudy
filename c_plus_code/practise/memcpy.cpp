#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<unordered_map>
#include<limits.h>
#include<list>
#include<stack>
#include<set>
#include<queue>
using namespace std;

struct ListNode{
   int val;
   ListNode* next;
   ListNode(int x):val(x),next(nullptr){}
};


struct TreeNode{
	int val;
	TreeNode* left,*right;
	TreeNode(int x):val(x),left(nullptr),right(nullptr){}
};

void * memcpy(void* dst,void* src,size_t n){
	if(dst == nullptr || src == nullptr) return nullptr;
	const char* psrc = static_cast<const char*>(src);
	char* pdst = static_cast<char *>(dst);
	if(pdst > psrc && pdst < (psrc+n)){
		for(int i=n-1;i>=0;i--)
			pdst[i] = psrc[i];
	}else{
		for(int i=0;i<n;i++)
			pdst[i] = psrc[i];
	}
	return dst;
}

char* strcpy(char* strDest,const char* strSrc){
    if(strDest == nullptr || strSrc == nullptr) return nullptr;
    char* address = strDest;
    while((*strDest++ = *strSrc++) != '\0');
    return address;
}





void bubbleSort(int a[],int n){
	if(n <=1) return;
    bool didSwap;
	for(int i=n-1;i>=0;i--){
        didSwap = false;
        for(int j=0;j<i;j++)
            if(a[j] > a[j+1]){
                didSwap = true;
                swap(a[j],a[j+1]);
            }
        if(didSwap == false) return;//best time complexity is O(n)
    }

}


void quickSort(int a[],int low,int high){
	if(high <= low) return;
	int first = low,last = high;
	int keyVal = a[first];
	while(first < last){
		while(first < last && a[last] >= keyVal) last--;
		a[first] = a[last];
		while(first < last && a[first] <= keyVal ) first++;
		a[last] = a[first];
	}
	a[first] = keyVal;
	quickSort(a,low,first-1);
	quickSort(a,first+1,high);
}// space postion is always available for the piviot value 
//and the most important position is the piviot position


void insertSort(int a[],int n){
	if(n <= 1) return;
	int i,j,k;
	for(i=1;i<n;i++){
		for(j = i-1;j>=0;j--){
			if(a[j] < a[i])
				break;
		}
	}
}



// void mergeArray(int a[],int n,int b[],int m,int c[]){
//     int i,j,k;
//     i = j = k = 0;
//     while(i < n && j < m){
//         if(a[i] < b[j]){
//             c[k++] = a[i++];
//         }else
//             c[k++] = b[j++];
//         while(i < n)
//             c[k++] = a[i++];
//         while(j < m)
//             c[k++] = b[j++];
//     }


// }

// vector<int> mergeArray(vector<int>& a,vector<int>& b){
//     size_t aSize = a.size(),bSize = b.size();
//     size_t aIndex,bIndex;
//     aIndex = bIndex = 0;
//     vector<int> c;
//     while(aIndex < aSize && bIndex < bSize){
//         if(a[aIndex] < b[bIndex])
//             c.push_back(a[aIndex++]);
//         else
//             c.push_back(b[bIndex++]);
//     }
//     if(aIndex < aSize)
//         c.push_back(a[aIndex++]);
//     if(bIndex < bSize)
//         c.push_back(b[bIndex++]);
//     return c;
// }


// void mergeSort(int a[],int first,int last,int temp[]){
//     if(first < last){
//         int mid = (first + last)/2;
//         mergeSort(a,first,mid,temp);
//         mergeSort(a,mid+1,last,temp);
//         mergeArray(a,first,mid,last,temp);
//     }
// }








// #include<limits.h>
// int maxSumSubArr(ve){
// 	int maxVal = INT_MIN;
// 	size_t size = sizeof(arr)/sizeof(arr[0]);
// 	return size;



// 	return maxVal;
// }



class Solution{//2.1.8
public:
	vector<int> twoSum(vector<int>& nums,int target){
		vector<int> result;
		unordered_map<int,int> hashTab;
		for(int i=0;i<nums.size();i++)
			hashTab[nums[i]] = i;
		for(int i=0;i<nums.size();i++){
			int gapVal = target -nums[i];
			if(hashTab.find(gapVal) != hashTab.end() && hashTab[gapVal] > i){
				result.push_back(i);
				result.push_back(hashTab[gapVal]);
				break;
			}
		}
		return result;
	}

	int removeElement(vector<int>& nums,int target){
		int index = 0;
		for(int i=0;i<nums.size();i++){
			if(nums[i] != target){
				nums[index++] = nums[i]; 
			}
		}
		return index;
	}

	vector<int> plusOne(vector<int>& digits){
		int carry = 1;
		for(int i=digits.size()-1;i>=0;i--){
			int currDigit =  (digits[i] + carry)%10;
			carry = (digits[i] + carry)/10;
			digits[i] = currDigit;
		}
		if(carry >0)
			digits.insert(digits.begin(),carry);
		return digits;
	}

	string addBinary(string a,string b){
		string result;
		reverse(a.begin(),a.end());
		reverse(b.begin(),b.end());
		int carry = 0;
		size_t aSize = a.size(),bSize = b.size();
		int n = max(aSize,bSize);
		for(int i=0;i<n;i++){
			int ai = i < aSize ? a[i] - '0' : 0;
			int bi = i < bSize ? b[i] - '0' :0;
			result.insert(result.begin(),(ai+bi+carry)%2 + '0');
			carry = (ai + bi + carry)/2;
		}
		if(carry)
			result.insert(result.begin(),carry + '0');
		return result;
	}


	ListNode* partition(ListNode* head,int x){//2.2.3
		if(head == nullptr) return head;
		ListNode leftDummy(-1);
		ListNode rightDummy(-1);
		ListNode* iter = head,*leftIter = &leftDummy,*rightIter = &rightDummy;
		while(iter){
			if(iter->val < x){
				leftIter->next = iter;
				leftIter = leftIter->next;
			}else{
				rightIter->next = iter;
				rightIter = rightIter->next;
			}
			iter = iter->next;
		}
		rightIter->next = nullptr;
		leftIter->next = rightDummy.next;
		return leftDummy.next;
	}


	ListNode* deleteDuplicates(ListNode* head){//2.2.5
		if(head == nullptr || head->next == nullptr) return head;
		ListNode dummy(INT_MIN);
		// dummy.next = head;
		ListNode* cur = head,*prev = &dummy;
		while(cur){
			bool duplicated = false;
			while(cur->next != nullptr && cur->val == cur->next->val){
				duplicated = true;
				ListNode* temp = cur;
				cur = cur->next;
				delete temp;
			}
			if(duplicated){//delete the last duplicate item
				ListNode* temp = cur;
				cur = cur->next;
				delete temp;
				continue;
			}
			prev->next = cur;
			prev = prev->next;
			cur = cur->next;
		}
		prev->next = nullptr;//cur means nullptr
		return dummy.next;
	}

	bool hasCycle(ListNode* head){//2.2.11
		if(head == nullptr) return false;
		ListNode* pFast = head,*pSlow = head;
		bool hasCycle = false;
		while(pFast && pFast->next){
			pFast = pFast->next->next;
			pSlow = pSlow->next;
			if(pFast == pSlow){
				hasCycle = true;
				break;
			}
		}
		return hasCycle;
	}





	ListNode* detectCycle(ListNode* head){//2.2.12  leetcode accepted 
		if(head == nullptr) return nullptr;
		ListNode* pFast = head,*pSlow = head;
		bool hasCycle = false;
		while(pFast && pFast->next){
			pFast = pFast->next->next;
			pSlow = pSlow->next;
			if(pFast == pSlow){
				hasCycle = true;
				break;
			}
		}
		if(!hasCycle) return nullptr;
		pSlow = pSlow->next;
		int nodeCntInCycle = 1;
		while(pSlow != pFast){
			nodeCntInCycle++;
			pSlow = pSlow->next;
		}
        //pfast pslow 
        pFast = head,pSlow = head;
        for(int i=0;i<nodeCntInCycle;i++) pFast = pFast->next;
        while(pFast != pSlow){
        	pFast = pFast->next;
        	pSlow = pSlow->next;
        }
        return pFast;
	}

	//
	void merge(vector<int>& A,int m,vector<int>& B,int n){//6.1
		int ia =m-1,ib=n-1,iCur = m + n -1;
		while(ia >=0 && ib >= 0){
			A[iCur--] = A[ia] > B[ib] ? A[ia--] : B[ib--];
		}
		while(ib >=0){
			A[iCur--] = B[ib--];

		}

	}

	ListNode* mergeTwoLists(ListNode* l1,ListNode* l2){
		if(l1 == nullptr) return l2;
		if(l2 == nullptr) return l1;
		ListNode dummy(-1);
		ListNode* prev = &dummy;
		while(l1 && l2){
			if(l1->val < l2->val){
				prev->next = l1;
				l1 = l1->next;
			}else{
				prev->next = l2;
				l2 = l2->next;

			}
			prev = prev->next;
		}
		prev->next = l1 ? l1 :l2;
		return dummy.next;
	}


	struct RandomListNode {
      int label;
      RandomListNode *next, *random;
      RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
    };

    RandomListNode *copyRandomList(RandomListNode *head) {
        RandomListNode* pIter = head;
        while(pIter){
        	RandomListNode* pTemp = pIter->next;
        	pIter->next = new RandomListNode(pIter->label);
        	pIter->next->next = pTemp;
        	pIter = pIter->next->next;
        }
        pIter = head;
        while(pIter){
        	if(pIter->random){
        		pIter->next->random = pIter->random->next;
        	}
        	pIter = pIter->next->next;
        }
        RandomListNode dummy(-1);
        RandomListNode* prev = &dummy;
        pIter = head;
        while(pIter){
        	prev->next = pIter->next;
        	pIter->next = pIter->next->next;
        	pIter = pIter->next;
        	prev = prev->next;

        }
        return dummy.next;
    }

    ListNode* reverseBetweenOther(ListNode* head,int m,int n){//leetcode ac 2.2.2
    	if(m == n) return head;
    	ListNode dummy(-1);
    	dummy.next = head;
    	ListNode* prev = &dummy;
    	for(int i=1;i<m;i++){
    		prev = prev->next;
    	}
    	ListNode* ele = prev->next;//start node of reverse
    	ListNode* pReversePrev = prev->next,*pReverseNext = pReversePrev->next,*pTemp = nullptr;
    	for(int i=m;i<n;i++){
    		pTemp = pReverseNext->next;
    		pReverseNext->next = pReversePrev;
    		pReversePrev = pReverseNext;
    		pReverseNext = pTemp;
    	}
    	prev->next = pReversePrev;
    	ele->next = pTemp;
    	return dummy.next;

    }
    

    ListNode* reverseLinkList(ListNode* head){//just for fun
    	if(head == nullptr || head->next == nullptr) return head;
    	ListNode* prev = head,*next = head->next;
    	while(next){
    		ListNode* temp = next->next;
    		next->next = prev;
    		prev = next;
    		next = temp;
    	}
    	head->next = nullptr;
    	return prev;
    }


    int minDepth(TreeNode* root) {//5.4.1 leetcode ac 
    	if(root == nullptr) return 0;
    	if(root->left == nullptr && root->right == nullptr) return 1;
    	if(root->left && root->right)
    		return min(minDepth(root->left),minDepth(root->right)) + 1;
    	else if(root->left)
    		return minDepth(root->left) + 1;
    	else if(root->right)
    		return minDepth(root->right) + 1;
    }



    int maxDepth(TreeNode* root) {//5.4.2  leetcode ac 
    	if(root == nullptr) return 0;
    	if(root->left == nullptr && root->right == nullptr) return 1;
    	return max(maxDepth(root->left),maxDepth(root->right)) + 1;
        
    }



    bool hasPathSum(TreeNode* root, int sum) {//5.4.3 leetcode ac
    	if(root == nullptr) return false;
    	if(root->left == nullptr && root->right == nullptr){
    		if(root->val == sum) return true;
    		else return false;
    	}
    	int gap = sum - root->val;
    	return hasPathSum(root->left,gap) || hasPathSum(root->right,gap);
        
    }



    string reverseString(string s){//leetcode 344  ac 
    	reverse(s.begin(),s.end());
    	return s;
    }

    string reverseVowels(string s) {//leetcode 345 ac 
    	if(s.empty()) return s;
    	size_t last = s.size()-1,prev = 0;
    	string vowels = "aeiouAEIOU";
    	while(prev != last){
    		while(prev != last && vowels.find(s[prev]) == string::npos) prev++;
    		if(prev == last) break;
    		while(prev != last && vowels.find(s[last]) == string::npos) last--;
    		if(prev == last) break;
    		swap(s[prev],s[last]);
    		if(prev != last-1){
    			prev++;
    		    last--;
    		}else{
    			break;
    		}
    	}
    	return s;
    }


    vector<vector<int>> pathSum(TreeNode* root, int sum) {//5.4.4
    	if(root == nullptr) return vector<vector<int>>();
    	vector<vector<int>> result;
    	vector<int> temp;
    	return pathSum(root,temp,result,sum);
    }
    vector<vector<int>> pathSum(TreeNode* root,vector<int>& temp,vector<vector<int>>& result,int sum){
    	return vector<vector<int>>();

    }



    int climbStairs(int n){//the n is limited 
    	if(n == 1) return 1;
    	if(n == 2) return 2;
    	long long topVal = 0,oneVal=2,twoVal=1;
    	for(int i=3;i<=n;i++){
    		topVal = oneVal + twoVal;
    		twoVal = oneVal;
    		oneVal = topVal;
    	}
    	return oneVal;
    }




    string climbStairsNotLimit(int n){
    	if(n == 1) return "1";
    	if(n == 2) return "2";
    	string posLeft = "2",posRight = "1";
    	string total;
    	for(int i=3;i<=n;i++){
    		total = highAccuracyAddUsingString(posLeft,posRight);
    		posRight = posLeft;
    		posLeft = total;
    	}
    	return total;
    }

    string highAccuracyAddUsingString(string a,string b){
    	reverse(a.begin(),a.end());
    	reverse(b.begin(),b.end());
    	size_t aSize = a.size(),bSize = b.size();
    	size_t maxSize = max(aSize,bSize);
    	int carry = 0;
    	string result;
    	for(int i=0;i<maxSize;i++){
    		int ai = i < aSize ? a[i]-'0':0;
    		int bi = i < bSize ? b[i] -'0':0;
    		int cur = (ai + bi +  carry)%10 + '0';
    		carry = (ai + bi + carry)/10;
    		result.insert(result.begin(),cur);
    	}
    	if(carry)
    		result.insert(result.begin(),carry+'0');
    	return result;
    }





    int myAtoi(const string& str){
    	int i = 0;
    	int result,flag =1;
    	while(str[i] == ' ' && i < str.size()) i++;
    	if(str[i] == '-'){
    		flag = -1;
    		i++;
    	}else if(str[i] == '+'){
    		flag = 1;
    		i++;
    	}


    	while(i < str.size()){
    		if(str[i] < '0' || str[i] > '9'){
    			break;
    		}else{
    			////to this place  

    		}
    	}
    	cout << i << endl;
    	return 0;
    }


    string reverseStr(string s, int k) {//leetcode 541  ac 
    	if(s.empty() || k<=0) return s;
    	size_t size = s.size();
    	if(size < k){
    		reverse(s.begin(),s.end());
    	}else if(size >= k && size < (k << 1)){
    		reverse(s.begin(),s.begin()+k);
    	}else{
    		// cout << "get there " << endl;
    		int groupCnt = size/(k<<1);
    		cout << groupCnt << endl;
    		for(int i=0;i<groupCnt;i++){
    			reverse(s.begin()+ i*(k<<1),s.begin()+ i*(k<<1) + k);
    		}
    		size_t left = size - (groupCnt*(k<<1));
    		if(left < k)
    			reverse(s.begin()+ groupCnt*(k<<1),s.end());
    		else
    			reverse(s.begin() + groupCnt*(k<<1),s.begin() + groupCnt*(k<<1) + k);

    	}
    	return s;
    }

    int MoreThanHalfNum_Solution(vector<int> numbers) { //offer 29
    	if(numbers.empty()) return 0;
    	size_t size = numbers.size()/2;
    	int maxVal = MoreThanHalfNum_Solution(numbers,0,numbers.size(),size);
    	return maxVal;
    }
    int MoreThanHalfNum_Solution(vector<int>& numbers,int low,int high,int size){
    	int first = low,last = high;
    	int keyVal = numbers[first];
    	while(first < last){
    		while(first < last && numbers[last] >= keyVal) high--;
    		swap(numbers[first],numbers[last]);
    		while(first < last && numbers[first] <= keyVal) low++;
    		swap(numbers[first],numbers[last]);
    	}
    	numbers[first] = keyVal;
    	if(low == size){
    		return keyVal;
    	}else if(low > size){
    		return MoreThanHalfNum_Solution(numbers,low,first-1,size);
    	}else{
    		return MoreThanHalfNum_Solution(numbers,first+1,high,size);
    	}
    }







    int FirstNotRepeatingChar(string str) {// nowcow   offer35 ac 
    	if(str.empty()) return -1;
    	vector<int> hashTab(256,0);
    	for(auto val:str){
    		hashTab[val]++;
    	}
    	size_t index;
    	for(index=0;index<str.size();index++){
    		if(hashTab[str[index]] == 1) break;
    	}
    	return index;
    }


  /*
    输入例子:I am a boy
	输出例子: boy a am I
  */
    void reverseSentence(){
    	stack<string> ss;
    	string s;
    	while(cin >> s){
    		ss.push(s);
    	}
    	while(!ss.empty()){
    		cout << ss.top();
    		ss.pop();
    		if(!ss.empty())
    			cout << ' ';
    	}
    	cout << endl;
    }


    vector<int> intersectionUsingSet(vector<int>& nums1, vector<int>& nums2) {//leetcode 349  ac usint set a
        set<int> s1,s2;
        vector<int> result;
        for(auto val:nums1){
            s1.insert(val);
        }
        for(auto val:nums2){
            if(s1.find(val) != s1.end())
                s2.insert(val);
        }
        for(auto iter = s2.begin();iter!=s2.end();iter++)
            result.push_back(*iter);
        return result;
    }



    vector<int> intersection(vector<int>& nums1,vector<int> nums2){//more faster  leetcode 349 ac using unorderedmap to 
        unordered_map<int,int> valMap;
        vector<int> result;
        for(auto val:nums1){
            if(valMap.find(val) == valMap.end())
                valMap[val] = 1;
        }
        for(auto val:nums2){
            if(valMap.find(val) != valMap.end() && valMap[val] == 1){
                valMap[val]++;
                result.push_back(val);
            }
        }
        return result;
    }


    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {//leetcode 160 ac 
        if(headA == nullptr || headB == nullptr) return nullptr;
        ListNode* pHeadA = headA,*pHeadB = headB;
        size_t aSize =0,bSize = 0;
        while(pHeadA){
            aSize++;
            pHeadA = pHeadA->next;
        }
        while(pHeadB){
            bSize++;
            pHeadB = pHeadB->next;
        }
        pHeadA = headA,pHeadB = headB;
        if(aSize >= bSize){
            for(int i=0;i<aSize-bSize;i++)
                pHeadA = pHeadA->next;
            
        }else{
            for(int i=0;i<bSize-aSize;i++)
                pHeadB = pHeadB->next;
        }
        while(pHeadA){
            if(pHeadA == pHeadB) break;
            else{
                pHeadA = pHeadA->next;
                pHeadB = pHeadB->next;
            }
        }
        return pHeadA;
    }


    vector<int> intersectTwo(vector<int>& nums1, vector<int>& nums2) {//very good  leetcode 350 very good ac 
        unordered_map<int,int> valMap;
        vector<int> result;
        for(auto val:nums1){
            if(valMap.find(val) == valMap.end())
                valMap[val] = 1;
            else 
                valMap[val]++;
        }
        for(auto val:nums2){
            if(valMap.find(val) != valMap.end()){
                result.push_back(val);
                valMap[val]--;
                if(valMap[val] == 0)
                    valMap.erase(val);
            }
        }
        return result;
        
    }


    vector<vector<int> > FindContinuousSequence(int sum) {//offer 41
        for(int val = 1;val<sum;val++){
            
        }   
    }


    int lengthOfLastWord(string s) {
        if(s.empty()) return 0;
        string::reverse_iterator first = find_if(s.rbegin(),s.rend(),::isalpha);
        string::reverse_iterator last = find_if_not(first,s.rend(),::isalpha);
        return distance(first,last);
    }








};

void lengthOfLastWordTest(){
    string s = "yin shuai good   ";
    int res = Solution().lengthOfLastWord(s);
    cout << res << endl;

}

void intersectionTest(){
    vector<int> nums1({2,5,8,9});
    vector<int> nums2({2,5,6,3});
    auto ret = Solution().intersection(nums1,nums2);
    for(auto val:ret) cout << val << endl;
}

void FirstNotRepeatingCharTest(){
	string s = "abcdefga";
	auto ret = Solution().FirstNotRepeatingChar(s);
	cout << ret << endl;
}

void MoreThanHalfNumTest(){
	vector<int> vec({1,2,2,2,3});
	Solution().MoreThanHalfNum_Solution(vec);

}

void reverseStrTest(){
	string s = "abcd"; int k = 2;
	auto res = Solution().reverseStr(s,k);
	cout << res << endl;
}

void myAtoiTest(){
	Solution().myAtoi("   abc");

}

void pathSumTest(){
	TreeNode* head = nullptr;
	Solution().pathSum(head,0);

}


void hasPathSumTest(){
	TreeNode head(1);
	TreeNode* pHead = &head;
	pHead->left = new TreeNode(2);
	bool ret = Solution().hasPathSum(pHead,3);
	cout << ret << endl;
}


void reverseLinkListTest(){
	ListNode dummy(-1);
	ListNode* prev = &dummy;
	for(int i=0;i<6;i++){
		prev->next = new ListNode(i);
		prev = prev->next;
	}
	auto ret = Solution().reverseBetweenOther(dummy.next,2,4);
	while(ret){
		cout << ret->val << endl;
		ret = ret->next;
	}


}


//big boss execise 
class LRUCache{//2.2.14	
private:
	struct CacheNode{
		int key;
		int value;
		CacheNode(int k,int v):key(k),value(v){}
	};
	int capacity;
	list<CacheNode> cacheList;
	unordered_map<int,list<CacheNode>::iterator> cacheMap;


public:
	LRUCache(int capacity){
		this->capacity = capacity;
	}

	int get(int key){
		if(cacheMap.find(key) == cacheMap.end()) return -1;
		//move the current visit node to the head of the link,and update the address of this node in cacheMap
		cacheList.splice(cacheList.begin(),cacheList,cacheMap[key]);//将x的元素移动到目的list的指定位置，高效的将他们插入到目的list并从x中删除。
		cacheMap[key] = cacheList.begin();
		return cacheMap[key]->value;
	}

	void set(int key,int value){
		if(cacheMap.find(key) == cacheMap.end()){
			if(cacheList.size() == capacity){//delete the tail node of the linklist
				cacheMap.erase(cacheList.back().key);
				cacheList.pop_back();
			}
			//insert new node into the head of list 
			cacheList.push_front(CacheNode(key,value));
			cacheMap[key] = cacheList.begin();
		}else{
			//update the value of the node,move the current visit node to the head of the list . and update the address of this node in map
			cacheMap[key]->value = value;
			cacheList.splice(cacheList.begin(),cacheList,cacheMap[key]);
			cacheMap[key] = cacheList.begin();
		}
	}
};






class MyQueue {//leetcode 232 ac 
private:
    stack<int> stk1;
    stack<int> stk2;
public:
    /** Push element x to the back of queue. */
    void push(int x) {
        while(!stk1.empty()){
            stk2.push(stk1.top());
            stk1.pop();
        }
        stk1.push(x);
        while(!stk2.empty()){
            stk1.push(stk2.top());
            stk2.pop();
        }

    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int val = stk1.top();
        stk1.pop();
        return val;
    }
    
    /** Get the front element. */
    int peek() {
        return stk1.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return stk1.empty();
        
    }
};



//https://leetcode.com/problems/min-stack/#/description
class MinStack {
private:
    stack<int> s1;
    stack<int> s2;//s2 always keep the min value of current time .
public:
    void push(int x) {
        s1.push(x);
        if (s2.empty() || x <= getMin())  s2.push(x);       
    }
    void pop() {
        if (s1.top() == getMin())  s2.pop();
        s1.pop();
    }
    int top() {
        return s1.top();
    }
    int getMin() {
        return s2.top();
    }
};



class MyStack {//leetcode 225  ac 
private:
    queue<int> que;
public:
    /** Push element x onto stack. */
    void push(int x) {
        size_t size = que.size();
        que.push(x);
        for(int i=0;i<size;i++){
            que.push(que.front());
            que.pop();
        }

    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int val = que.front();
        que.pop();
        return val;
    }
    
    /** Get the top element. */
    int top() {
        return que.front();
        
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return que.empty();
        
    }
};




void MinStackTest(){
    MinStack obj = MinStack();
    obj.push(4);
    obj.push(5);
    obj.push(6);

    auto val = obj.getMin();
    cout << val << endl;
    obj.pop();
    val = obj.getMin();
    cout << val << endl;
    // obj.push(x);
    // obj.pop();
    // int param_3 = obj.top();
    // int param_4 = obj.getMin();
}

void TestClassTest(){
	struct MyNode{
		int key;
		int value;
		MyNode(int k,int v):key(k),value(v){}
	};

	list<MyNode> myList;
	myList.push_back(MyNode(10,50));
	cout << myList.begin()->key << endl;//10
	cout << myList.front().key << endl;//10
	cout << myList.back().key << endl;//10
}

void twoSumTest(){
	vector<int> vec({1,4,2,5,6,8});
	auto ret = Solution().twoSum(vec,10);
	for(auto val:ret) cout << val << endl;
}

void removeElementTest(){
	vector<int> vec({1,2,3,3,3,4,5,6,6});
	auto ret = Solution().removeElement(vec,5);
	cout << ret << endl;
}

void plusOneTest(){
	vector<int> digits({9,9,9});
	Solution().plusOne(digits);
	for(auto val:digits) cout << val;
    cout << endl;
}
void addBinaryTest(){
	string a = "110";
	string b = "11100";
	auto ret = Solution().addBinary(a,b);
	cout << ret << endl;
}

void partitionTest(){
	vector<int> vec({1,4,3,2,5,2});
	ListNode dummy(-1);
	ListNode* iter = &dummy;
	for(auto val:vec){
		iter->next = new ListNode(val);
		iter = iter->next;
	}

	ListNode* ret = Solution().partition(dummy.next,3);
	while(ret){
		cout << ret->val << endl;
		ret = ret->next;
	}
}

void deleteDuplicatesTest(){
	vector<int> vec({4,4,3,2,2,2,1});
	ListNode dummy(-1);
	ListNode* iter = &dummy;
	for(auto val:vec){
		iter->next = new ListNode(val);
		iter = iter->next;
	}
	auto ret = Solution().deleteDuplicates(dummy.next);
	while(ret){
		cout << ret->val << endl;
		ret = ret->next;
	}

}

void highAccuracyAddTest(){
	vector<int> vec({1,2,3,4,5});
	long long addNum = 1897;
	int carry = 0;
	for(int i=vec.size()-1;i>=0;i--){
		int curVal = (vec[i] + addNum%10 + carry) % 10;
		carry = (vec[i] + addNum%10 + carry)/10;
		addNum = addNum/10;
		vec[i] = curVal;
		if(carry == 0) break;
	}
	if(carry) vec.insert(vec.begin(),carry);
	for(auto val:vec) cout << val;

}


void climbStairsTest(int x){
	auto res1 = Solution().climbStairs(x);
	cout << res1 << endl;
	auto res2 = Solution().climbStairsNotLimit(x);
	cout << res2 << endl;
}

void reverseStringTest(){
	string s = "yin shuai good day";
	string res = Solution().reverseString(s);
	cout << res << endl;
}






void inStreamTest(){
	int a,b;
	cin >> a >> b;
	cout << a << endl;
	cout << b << endl;
}

void  stringMatchTest(){
	string a = "abcdefg";
	if(a.find("c") == string::npos)
		cout << "not found " << endl;
	else
		cout << "has found " << endl;
}


void testCase(){
    int b = 10,d=11;
    int &c = b;
    const char* a  = "abcdefghijk";
    cout << sizeof(a) << endl;
    char arr[] = "abcdefghijk";
    cout << sizeof(arr) << endl;//12
    cout << endl << endl;

    struct A{
        short a1;
        short a2;
        short a3;
    };
    struct B{
        long a1;
        short a2;
    };
    struct C{
        int a1;
        short a2;
    };

    cout << sizeof(A) << endl;//6
    cout << sizeof(B) << endl;//16
    cout << sizeof(C) << endl;//8
    cout << endl << endl;
    char *str1 = (char*)malloc(100);
    void *str2 = (void*)malloc(100);
    cout << sizeof(str1) << endl;//8
    cout << sizeof(str2) << endl;//8
}


int staticCase(int a){
    auto  c = 0;
    static int b = 3;
    c += 1;
    b += 2;
    return (a+b+c);
}

void staticTest(){
    cout << staticCase(1) << endl;//7
    cout << staticCase(1) << endl;//9
    cout << staticCase(1) << endl;//11
}


class staticClass{
public:
    static int a;
    void funcOne(){
        cout << a << endl;
    }
};
int staticClass::a = 33;
void staticClassTest(){
    staticClass().funcOne();
}



int main(){
    lengthOfLastWordTest();
    return 0;
    staticClassTest();
    return 0;
    staticTest();
    return 0;
    testCase();
    return 0;
    MinStackTest();
    return 0;
    intersectionTest();
    return 0;
	string pattern = "what";
	string testStr = "w";
	auto res = pattern.find(testStr);
	if(res == string::npos) cout << "not found";
	else cout << "has found";

	return 0;
	stack<string> ss ;
	string s;
    while(getline(cin,s)){

    }

	return 0;

			while(!ss.empty()){
			cout << ss.top();
			ss.pop();
			if(!ss.empty()) cout << ' ';
		}
		cout << endl;


	Solution().reverseSentence();
	return 0;
	stringMatchTest();
	return 0;
	FirstNotRepeatingCharTest();
	return 0;
	MoreThanHalfNumTest();
	return 0;
	reverseStrTest();
	return 0;
	reverseStringTest();
	return 0;
	inStreamTest();
	return 0;
	myAtoiTest();
	return 0;
	climbStairsTest(100);
	return 0;
	pathSumTest();
	return 0;
	hasPathSumTest();
	return 0;
	reverseLinkListTest();
	return 0;
	TestClassTest();
	return 0;
	deleteDuplicatesTest();
	return 0;
	partitionTest();
	return 0;
	addBinaryTest();
	return 0;
	plusOneTest();
	return 0;
	int arr[] = {5,4,3,2,1,6,6,4};
	// bubbleSort(arr,sizeof(arr)/sizeof(int));
	quickSort(arr,0,sizeof(arr)/sizeof(int)-1);
	for(int i=0;i<sizeof(arr)/sizeof(int);i++)
		cout << arr[i] << endl;

}
