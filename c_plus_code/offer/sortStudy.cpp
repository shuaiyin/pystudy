#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:

	void bubbleSort(vector<int>& vec){
		for(int i= vec.size()-1;i>=0;i--){
			for(int j=0;j<i;j++){
				if(vec[j] > vec[j+1]) 
					swap(vec[j],vec[j+1]);
			}
		}	
	}

//main http://baike.baidu.com/link?url=O4E2zK9_HNDC7ee7A8zQKORoeHlFibwjMLlKGgZ88B1vovsu6UCsZ2JFaxhLXj4HKnMcLgjr_WVTmJ1jEHHVfOh3OAcrL_aDA-4ePdlj4_kBSOrZi_aW0HKhSLKW05qzRTtQ-WMOPbNQ9b4-OghtGZs57JNKH63iJmcYz9vWTw0ywsZ5TT2HiVOvVM8I0hnvKT7xpCDTeSTmsCt-1snT94GQo0qUF_jey_VR2TdIspW

	// void quickSort(vector<int>& vec,int low,int high){
	// 	if(low >= high) return;
	// 	int piviotVal = vec[0];
	// 	int first = low,last = high;
	// 	while(first < last){
	// 		while(first < last && vec[last] >= piviotVal) last--;
	// 		vec[first] = vec[last];
	// 		while(first < last && vec[first] <= piviotVal) first++;
	// 		vec[last] = vec[first];
	// 	}
	// 	vec[first] = piviotVal;
	// 	quickSort(vec,low,first-1);
	// 	quickSort(vec,first+1,high);
	// }


	void bubbleSort(int a[],int len){
		for(int i=len-1;i>=0;i--){
			for(int j=0;j<i;j++)
				if(a[j] > a[j+1]) 
					swap(a[j],a[j+1]);
		}
	}

	void Qsort(int a[], int low, int high){
	    if(low >= high)
	    	return;
	    int first = low;
	    int last = high;
	    int key = a[first];/*用字表的第一个记录作为枢轴*/
	    while(first < last)
	    {
	        while(first < last && a[last] >= key)
	        	last--;
	        a[first] = a[last];/*将比第一个小的移到低端*/
	        while(first < last && a[first] <= key)
	        	first++;
	        a[last] = a[first];    
	    }
	    a[first] = key;/*枢轴记录到位*/
	    Qsort(a, low, first-1);
	    Qsort(a, first+1, high);
	}

//http://blog.csdn.net/morewindows/article/details/6665714
	void insert_sort(int a[],int n){
		int i,j,k;
		for(i=1;i<n;i++){
			for(j=i-1;j>=0;j--){
				if(a[j] < a[i]) break;
			}
			if(j != i-1){
				int temp = a[i];
				for(k = i-1;k>j;k--)
					a[k+1] = a[k];
				a[k+1] = temp;
		    }

		}

	}





//guibingpaixu 
	// void Merge(int sourceArr[],int tempArr[],int startIndex,int midIndex,int endIndex){

	// }

	void MergeSort(int sourceArr[],int tempArr[],int startIndex,int endIndex){
		int midIndex;
		if(startIndex < endIndex){
			midIndex = (startIndex + endIndex)/2;
			MergeSort(sourceArr,tempArr,startIndex,midIndex);
			MergeSort(sourceArr,tempArr,midIndex+1,endIndex);
		}

	}





};

void test_insert_sort(){
	int arr[] = {1,2,5,4,9,3};
	int size = sizeof(arr)/sizeof(arr[0]);
	Solution().insert_sort(arr,size);
	for(int i=0;i<size;i++)
		cout << arr[i] << endl;
}

void test_merge_sort(){
	int arr[] = {1,2,5,4,9,3};
	int size = sizeof(arr)/sizeof(arr[0]);
	int i,b[size];
	MergeSort(arr,b,0,size-1);
}


int main(){
	test_insert_sort();
	return 0;
	int arr[] = {1,5,4,3,2,1};
	int arr_size = sizeof(arr)/sizeof(int);
	Solution().Qsort(arr,0,arr_size-1);
	// Solution().bubbleSort(arr,arr_size);
	for(int i=0;i<arr_size;i++)
		cout << arr[i] << endl;
	// return 0;
	return 0;
}