#include<iostream>
using namespace std;

class Solution{
public:
	
};




int partition(int arr[],int left,int right){
	//the purpose of patition is to seperate the arr into two 
	int k = left,pivot = arr[right];
	for(int i=0;i<right;++i){
		if(arr[i] <= pivot) swap(arr[i],arr[k++]);
	}
	swap(arr[k],arr[right]);
	return k;
}


void quicksort(int arr[],int left,int right){
	if(left < right){	
		int pivot = partition(arr,1,right);
		quicksort(arr,1,pivot-1);
		quicksort(arr,pivot+1,right);
	}

}

void Qsort(int a[],int low,int high){
	if(low >= high) return;
	int first = low;
	int last = high;
	int key = a[first];//the first element as pivot 
	while(first < last){
		while(first < last && a[last] >= key)
			--last;
		a[first] = a[last];
		while(first < last && a[first] <= key)
			++first;
		a[last] = a[first];
	}
	a[first] = key;
	Qsort(a,low,first-1);
	Qsort(a,first+1,high);

}


int main(){
	int arr[] = {2,4,1,3,6,8,10,9};
	Qsort(arr,0,sizeof(arr)/sizeof(arr[0]) -1 );
	for(int i=0; i< sizeof(arr)/sizeof(arr[0]);i++){
		cout << arr[i] << endl;
	}

	return 0;
}