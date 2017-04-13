#include<iostream>
#include<vector> 
using namespace std;

class Solution{
public:
	//with O(N*N) time complexity
	int mininumTotal(vector<vector<int>>& triangle){
		for(int i = triangle.size()-2;i>=0;--i){
			for(int j=0;j<i+1;++j){
				triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]);
			}
		}	
		return triangle[0][0];
	}

	
};


int main(){
	vector<vector<int>> vec({{1},{2,3},{4,5,6},{7,8,9,10},{11,12,13,14,15}});
	auto ret = Solution().mininumTotal(vec);
	cout << ret << endl;
	return 0;
}