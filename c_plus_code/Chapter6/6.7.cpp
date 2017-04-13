#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	int firstMissingPostive(vector<int>& nums){

		return 0;
	}
private:
	static void bucket_sort(vector<int>& A){
		const int n = A.size();
		for(int i=0;i<n;i++){
			while(A[i] != i+1){

			}
		}
	}
};
















/*
*Mergesort algorithm 
*/
template<typename Comparable>
void mergeSort(vector<Comparable>& a){
	vector<Comparable> tmpArray(a.size());
	mergeSort(a,tmpArray,0,a.size()-1);
}

template<typename Comparable>
void mergeSort(vector<Comparable>& a,vector<Comparable>& tmpArray,int left,int right){
	if(left < right){
		int center = (left + right)/2;
		mergeSort(a,tmpArray,left,center);
		mergeSort(a,tmpArray,center+1,right);
		merge(a,tmpArray,left,center+1,right);
	}
}

template<typename Comparable>
void merge(vector<Comparable>& a,vector<Comparable>& tmpArray,int leftPos,int rightPos,int rightEnd){
	int leftEnd = rightPos - 1;
	int tmpPos = leftPos;
	int numElements = rightEnd - leftPos + 1;
	//main loop 
	while(leftPos <= leftEnd && rightPos <= rightEnd){
		if(a[leftPos] <= a[rightPos])
			tmpArray[tmpPos++] = a[leftPos++];
		else
			tmpArray[tmpPos++] = a[rightPos++];
	}
	while(leftPos <= leftEnd)//copy rest of first half
		tmpArray[tmpPos++] = a[leftPos++];
	while(rightPos <= rightEnd)
		tmpArray[tmpPos++] = a[rightPos++];
	//copy 	tmparray back 
	for(int i=0;i<numElements;i++,rightEnd--)
		a[rightEnd] = tmpArray[rightEnd];

}







/**
simple insertion sort 
**/
template<typename Comparable>
void insertionSort(vector<Comparable>& a){
	int j;
	for(int p=1;p<a.size();p++){
		Comparable tmp = a[p];
		for(j = p;j > 0 && tmp < a[j-1];j--)
			a[j] = a[j - 1];
		a[j] = tmp;
	}
}








void MergeTwoSortArray(vector<int>& a,int aSize,vector<int>& b,int bSize,vector<int>& c){
	int i,j,k;
	i = j = k = 0;
	while(i < aSize && j < bSize){
		if(a[i] < b[j])
			c[k++] = a[i++];
		else
			c[k++] = b[j++];
	}
	while(i < aSize)
		c[k++] = a[i++];
	while(j < bSize)
		c[k++] = b[j++];
}


void QuickSort(int arr[],int first,int end){
	return;
}

void OnceSort(int arr[],int first,int end){
	return;
}


/*
void MergeTwoSortArray(int a[],int n,int b[],int m,int c[]){
	int i,j,k;
	i = j = k = 0;
	while(i < n && j < m){
		if(a[i] < b[j])
			c[k++] = a[i++];
		else
			c[k++] = b[j++];
	}
	while(i < n)
		c[k++] = a[i++];
	while(j < m)
		c[k++] = b[j++];
}


void testMergeTwoSortArray(){
	int a[] = {1,4,6,7,8};
	int b[] = {2,3,5,10,11};
	int aSize = sizeof(a)/sizeof(int);
	int bSize = sizeof(b)/sizeof(int);
	int c[] = {};
	MergeTwoSortArray(a,aSize,b,bSize,c);
	int cSize = sizeof(c)/sizeof(int);

	for(int i = 0;i<cSize;i++) cout << c[i] << endl;

}
*/



//bucket_sort 


int main(){
	// testMergeTwoSortArray();
	return 0;
}