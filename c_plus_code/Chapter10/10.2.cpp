#include<iostream>
#include<vector> 
using namespace std;

class Solution{
public:
	//deep search method
	int uniquePathsDeepSearch(int m,int n){
		if(m < 1 || n < 1) return 0;//stop 
		if(m == 1 && n == 1) return 1;
		return uniquePathsDeepSearch(m-1,n) + uniquePathsDeepSearch(m,n-1);
	}

	//memorandum method combine with deep search method. cache center result
	int uniquePaths(int m,int n){
		//f[x][y] means path number from (0,0) to (x,y)
		f = vector<vector<int>>(m,vector<int>(n,0));
		f[0][0] = 1;
		return dfs(m-1,n-1);
	}  

	//dynamic programming ###some problem here 
	int uniquePathsDynamic(int m,int m){
		vector<int> f(n,0);
		f[0] = 1;
		for(int i=0;i<m;i++){
			for(int j=1;j<n;j++){
				f[j] = f[j] + f[j-1];
			}
		}
		return f[n-1];
	}
private:
	vector<vector<int>> f;//cache
	int dfs(int x,int y){
		if(x < 0 || y < 0) return 0;//illegal data,stop 
		if(x == 0 && y == 0) return f[0][0];//
		if(f[x][y] > 0) return f[x][y];
		else return f[x][y] = dfs(x-1,y) + dfs(x,y-1); 
	}

	
};


int main(){
	// auto ret = Solution().uniquePathsDeepSearch(100,100);
	// cout << "first deep search way: " << ret << endl;
	auto ret = Solution().uniquePaths(4,3);
	cout << "second deep search conbine memorandum: " << ret << endl;
	ret = 
	return 0;
}