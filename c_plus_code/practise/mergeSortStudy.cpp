

#include<stdio.h>
#include<stdlib.h>

void Merge(int *ch , int begin ,int mid , int end ){
       int i = begin;
       int m = mid;
       int j = mid+1;
       int k = 0;
       int *p = ( int *)malloc( sizeof(int )*(end -begin +1));
       if (p == NULL) return ;
       while (i <= m&&j <= end ){
             if ( ch[i] < ch[j])p[k++] = ch[i++];
             else{
                  p[k++] = ch[j++];
            }
      }
       for (; i <= m; i++){
            p[k++] = ch[i];
      }
       for (; j <= end;j++){
            p[k++] = ch[j];
      }
       for (i = 0; i < ( end- begin +1); i++){
             ch[i+ begin] = p[i];
      }
      free(p);
}



void testMerge(){
    int arr[] = {3,5,3,2,4,6};
    Merge(arr,0,3,5);
    for(int i=0;i<6;i++)
        printf("%d\n",arr[i]);



}



//归并排序
void MSort(int *ch ,int begin ,int end ){
       int mid = ( begin + end ) / 2;
       if ( begin < end ){
            MSort( ch, begin, mid);
            MSort( ch, mid + 1, end);
            Merge( ch, begin, mid, end );
      }
}
void MergeSort(int *ch ,int n ){
      MSort( ch,0, n-1);
}
int main(void ){

       int ch[8] = {49,38,65,97,76,13,27,49};
      MergeSort(ch, 8);
       int i;
       for (i = 0; i < 8; i++){
            printf( "%d ", ch[i]);
      }
      printf( "\n");
      system( "pause");
}


// #include<iostream>
// #include<ctime>
// #include<cstdlib>
// using namespace std;
// const int N = 204800;
 
// void Merge(int arr[], int p, int q, int r){
//     int n1 = q - p + 1;
//     int n2 = r - q + 1;
//     int left[n1 + 1], right[n2];
 
//     for (int i = 0; i != n1; ++i){
//         left[i] = arr[p + i];
//     }
//     left[n1] = N;
 
//     for (int j = 0; j != n2 - 1; ++j){
//         right[j] = arr[q + j + 1];
//     }
//     right[n2 - 1] = N;
 
//     int i = 0, j = 0;
//     for(int k = p; k != r + 1; ++k){
//         if(left[i] > right[j]){
//             arr[k] = right[j];
//             ++j;
//         }
//         else{
//             arr[k] = left[i];
//             ++i;
//         }
//     }
// }
 
// void MergeSort(int arr[], int p, int r){
//     if(p < r){
//         int q = (p + r)/2;
//         MergeSort(arr, p, q);
//         MergeSort(arr, q + 1, r);
//         Merge(arr, p, q, r);
//     }
// }
 
// int main(){
//     int arr[10] = {300, 60, 22, 16, 85, 89, 30, 99, 103, 55};
//     MergeSort(arr, 0, 9);
//     for(int i = 0; i < 10; ++i){
//         cout<<arr[i]<<endl;
//     }
//     return 0;
// }