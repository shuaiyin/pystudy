#include<iostream>
using namespace std;
#include<vector>
int find_my_kth(const vector<int> &A,const vector<int> &B,int k);
//leetcode,Median of two sorted arrays
class Solution{
public:
	double findMedianSortedArrays(const vector<int> &A,const vector<int> &B){
		const int m = A.size();
		const int n = B.size();
		int total = m + n;
		if(total & 0x1)//jishu
			return find_kth(A.begin(),m,B.begin(),n,total/2+1);
		else
			return 0.0;

	}
private:
	static int find_kth(vector<int>::const_iterator A,int m,
		vector<int>::const_iterator B,int n,int k){
		//always assume that m is equal or smaller than n 
		if(m == 0) return *(B+k-1);
		if(k == 1) return min(*A,*B);
		if(m > n) return find_kth(B,n,A,m,k);
	

		return 0;
	}
};
int main(){

	return 0;
    int arr1[] = {10,12,13,15,18};
    int arr2[] = {8,9,10,11,12,15};
	const vector<int> A(arr1,arr1+5);
	const vector<int> B(arr2,arr2+5);
	Solution so = Solution()
	so.findMedianSortedArrays(A,b,)
	return 0;
}

int find_my_kth(const vector<int> &A,const vector<int> &B,int k){
	vector<int>::const_iterator it;
	int sizeA = A.size();
	int sizeB = B.size();
	int total = sizeA + sizeB;
	vector<int>::const_iterator itera = A.begin();
	vector<int>::const_iterator iterb = B.begin();
	int mMax = 0;
	for(int i=0;i<total;i++){
		if(*itera < *iterb){
			itera++;
			mMax++;
		}else if(*itera > *iterb){
			continue;
		}
	}

}
