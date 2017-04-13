#include<iostream>
#include<vector>
#include<math.h>
using namespace std;



int solve(int n,int p,int w,int h,vector<int>& paragraphs){
	for(int i=min(w,h);i;i--){
		int row = w/i;
		int col = h/i;
		int require = 0;
		for(auto p:paragraphs)
			require += ceil(p/row);
		if(require <= p*col)
			return i;
	}
	return 1;
}



int main(){
   int tasks;
   cin >> tasks;
   for(int i=0;i<tasks;i++){
   	int n,p,w,h;
   	cin >> n >> p >> w >> h;
   	vector<int> paragraphs(n);
   	for(int i=0;i<n;i++)
   		cin >> paragraphs[i];
   	cout << solve(n,p,w,h,paragraphs) << endl;

   }
   return 0;
}