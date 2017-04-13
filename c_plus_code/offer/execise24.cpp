#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool VerifySquenceOfBST(vector<int> sequence) {
    	if(sequence.size() <= 1) return true;
    	return VerifySquenceOfBST(sequence.begin(),prev(sequence.end()));
    }

private:
	template<typename vecIter>
	bool VerifySquenceOfBST(vecIter begin,vecIter last){
		auto rootVal = *last;
		vector<int>::const_iterator centerIter;
		for(auto vecIterTemp=begin,vecIterTemp<last,vecIterTemp++){
			

		}

	}
};


int main(){
	vector<int> sequence({5,7,6,9,11,10,8});
	cout << sequence.back();
	return 0;
}