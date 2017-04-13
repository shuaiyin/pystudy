#include<iostream>
#include<vector> 
using namespace std;

class Solution{
public:
	int maximalRectangle(vector<vector<char>>& matrix){
		if(matrix.empty()) return 0;
		const int m = matrix.size();
		const int n = matrix[0].size();
		vector<int> H(n,0);
		vector<int> L(n,0);
		vector<int> R(n,n);
		for(auto val:R) cout << val << endl;
		int ret = 0;
		for(int i=0;i<m;i++){
			int left = 0,right = n;
			//calculate L(i,j) from left to right 
			for(int j=0;j<n;j++){
				if(matrix[i][j] == '1'){
					++H[j];
					L[j] = max(L[j],left);
				}else{
					left = j + 1;
					H[j] = 0;
					L[j] = 0;
					R[j] = n;
				}
			}
		}
	}

	
};


int main(){
	vector<vector<char>> matrix({{1,0,1},{0,1,0},{0,1,1},{1,0,1}});
	Solution().maximalRectangle(matrix);
	return 0;
}