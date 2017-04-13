// http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1677&konwledgeId=135

#include <iostream>
#include<string>
using namespace std;



int main(){

	string history;
	while(cin >> history){
		string sky;
		cin >> sky;
		int sameCnt = 0;
		float size = sky.size();
		for(int i=0;i<size;i++){
			if((isalnum(history[i]) && sky[i] == '1') ||
				(!isalnum(history[i]) && sky[i] == '0'))
				sameCnt++;
		}
	    float val = (sameCnt/size)*100;
	    printf("%.2f%%",val);
	}

	return 0;
}