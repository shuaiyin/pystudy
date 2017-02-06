#include<iostream>
using namespace std;

void pri(int n){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(i==0||i==n-1||j==0||j==n-1) cout << "#";
			else cout << "*";
		}
		cout << "\n" << endl;
	}
}

int main(){
	pri(7);
	return 0;	
}