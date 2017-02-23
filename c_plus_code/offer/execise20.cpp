#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> printMatrix(vector<vector<int>> matrix) {
		if(matrix.empty()) return vector<int>();
		auto matrixSize = matrix.size();//row num 
		auto matrixColumn = matrix[0].size();
		int circleCount = 0;
		while()
		// int circleCount = abs()
		return vector<int>();

    }
};



int main(){
	vector<vector<int>> vec({{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}});
	Solution().printMatrix(vec);
	return 0;
	for(auto vecEle:vec){
		for(auto val:vecEle)
			cout << val << " ";
		cout << endl;
	}
	return 0;
}