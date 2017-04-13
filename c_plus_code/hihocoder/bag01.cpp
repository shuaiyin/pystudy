#include<iostream>
using namespace std;
#define V 1500
unsigned int f[10][V];
unsigned int weight[10];
unsigned int value[10];
#define max(x,y) x > y ? x:y;

int main(){
	int N,M;
	cin >> N;//count of item 
	cin >> M;//count of bag 
	for(int i=1;i<=N;i++){
		cin >> weight[i] >> value[i];
	}
	for(int i=1;i<=N;i++){
		for(int j=1;j<=M;j++){
			if(weight[i] <= j){
				f[i][j] = max(f[i-1][j],f[i-1][j-weight[i]] + value[i]);
			}else{
				f[i][j] = f[i-1][j];
			}
		}
	}
	cout << f[N][M] << endl;
	return 0;
}
