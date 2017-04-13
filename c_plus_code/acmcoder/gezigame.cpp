// http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1662&konwledgeId=135
#include<iostream>
#include<vector>
#include<limits.h>
using namespace std;

int main(){
	int n,m;
	while(cin >> n >> m){
		vector<int> vec(n);
		for(int i=0;i<n;i++)
			cin >> vec[i];
		for(int i=0;i<m;i++){
			int oper,indexOne,indexSec;
			cin >> oper >> indexOne >> indexSec;
			if(oper == 1){
				vec[indexOne-1] = indexSec; 
			}else if(oper == 2){
				int sum = 0;
				for(int i=indexOne-1;i<indexSec;i++)
					sum += vec[i];
				cout << sum << endl;
			}else if(oper == 3){
				int maxVal = INT_MIN;
				for(int i=indexOne-1;i<indexSec;i++){
					if(vec[i] > maxVal) maxVal = vec[i];
				}
				cout << maxVal << endl;
			}
		}
	}
	return 0;
}