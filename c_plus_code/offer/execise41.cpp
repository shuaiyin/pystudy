#include<iostream>
#include<vector>
#include<limits.h>
using namespace std;

// class Solution {
// public:
// 	vector<vector<int> > FindContinuousSequence(int sum) {
// 		vector<vector<int>> result;
// 		vector<int> simSequence;
// 		int start = 1,next = start+1;
// 		while(next < sum){


// 		}

//     }
// };


int main(){
	string flag;
	while(cin >> flag){
		string firstQueue,SecondQueue;
		cin >> firstQueue >> SecondQueue;
		string seeQueue = firstQueue + SecondQueue;
		bool forward = false,backward=false,invalid=false,both=false;
		//positive test
		string::iterator flagIter = flag.begin(),queueIter = seeQueue.begin();
		while(flagIter!=flag.end() && queueIter!=seeQueue.end()){
			if(*flagIter == *queueIter)
				queueIter++;
			flagIter++;
		}

		if(queueIter == seeQueue.end()) forward = true;

		//negative
		string::reverse_iterator flagIterR = flag.rbegin();
		auto queueIterN = seeQueue.begin();
		while(flagIterR!=flag.rend() && queueIterN!=seeQueue.end()){
			if(*flagIterR == *queueIterN)
				queueIterN++;
			flagIterR++;
		}
		if(queueIterN == seeQueue.end()) backward = true;

		if(backward && forward) cout << "both" << endl;
		else if(backward) cout << "backward" << endl;
		else if(forward) cout << "forward" << endl;
		else cout << "invalid" << endl;


	}
 	return 0;
}



/*

//password
int main(){

	string firstLine;
	while(cin >> firstLine){
		string secondLine,thirdLine;
		cin >>  secondLine >> thirdLine;
		bool result = true;
		if(firstLine[0] != thirdLine[2] || firstLine[1] != thirdLine[1] || secondLine[0]!= secondLine[2] || thirdLine[0] != firstLine[2])
			result = false;
		if(result) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}

*/