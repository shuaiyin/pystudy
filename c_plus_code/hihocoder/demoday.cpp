#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	int uniquePaths(int m,int n){
		f = vector<vector<int>>(m,vector<int>(n,0));
		f[0][0] = 1;
		return dfs(m-1,n-1);
	}
private:
	vector<vector<int>> f;
	int dfs(int x,int y){
		if(x < 0 || y < 0) return 0;//
		if(x == 0 || y == 0) return f[0][0];//return to origin...
		if(f[x][y] > 0)
			return f[x][y];
		else{
			return f[x][y] = dfs(x-1,y) + dfs(x,y-1);
		}
	}

}