#include<iostream>
#include<vector>
#include<limits.h>
#include<algorithm>
using namespace std;

class Solution{
public:
	int minPathSum(vector<vector<int>>& grid){
		const int m = grid.size();
		const int n = grid[0].size();
		this->f = vector<vector<int>> (m,vector<int>(n,-1));
		return dfs(grid,m-1,n-1);
	}
		vector<vector<int>> f;//cacheed 
private:

	int dfs(vector<vector<int>>& grid,int x,int y){
		if(x < 0 || y < 0) return INT_MAX;
		if(x ==0 && y == 0) return grid[0][0];
		return grid[x][y] + min(getOrUpdate(grid,x-1,y),getOrUpdate(grid,x,y-1));
	}

	int getOrUpdate(vector<vector<int>>& grid,int x,int y){
		if(x < 0 || y < 0) return INT_MAX;//NOT 0;
		if(f[x][y] > 0) return f[x][y];
		else return f[x][y] = dfs(grid,x,y);
	}


};





int main(){
	return 0;


	vector<vector<int>> grid = {{1,2,3,4,5},{1,2,3,4,5},{1,2,3,4,5}};
	auto so = Solution();
	auto ret = so.minPathSum(grid);
	// cout << ret << endl;
	vector<vector<int>> v = so.f;
	for(auto val:v){
		for(auto vvv:val) cout << vvv << "   ";
		cout << endl;
	}

	return 0;
}

