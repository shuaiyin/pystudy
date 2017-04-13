#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	vector<vector<string>> solveNQueens(int n){
		vector<vector<string>> result;
		vector<int> C(n,-1);//C[i] means the column num in line i;
		dfs(C,result,0);
		return result;
	}

private:
	void dfs(vector<int>& C,vector<vector<string>>& result,int row){
		const int N = C.size();
		if(row == N){//terminal condition,which means we have found out a solution 
			vector<string> solution;
			for(int i=0;i<N;i++){
				string s(N,'.');
				for(int j=0;j<N;j++){
					if(j == C[i]) s[j] = 'Q';
				}
				result.push_back(solution);
				return;
			}
			for(int j=0;j<N;j++){//extend status ,try each column one by one 
				const bool ok = isValid(C,row,j);
				if(!ok) continue;//purniing. if illegal,try next column 
				//execute extend operation 
				C[row] = j;
				dfs(C,result,row+1);
				//cancel operation 
				C[row] = -1;

			}

		}
	}

	//if you can place a queen on (row,col )  
	//row is current treating row,the prev row has put queen 
	//col current column 
	bool isValid(const vector<int>& C,int row,int col){
		for(int i=0;i<row;i++){
			//in the same column
			if(C[i] == col) return false;
			//in the same duijiaoxian 
			if(abs(i - row) == abs(C[i] - col)) return false;
		}
		return true;
	}


};

int main(){
	vector<int> C(4,1);
	auto ret = Solution().isValid(C,0,0);
	cout << ret << endl;
	return 0;
}