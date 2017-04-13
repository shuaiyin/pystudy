#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution{
public:
	bool exist(const vector<vector<char>>& board,const string& word){
		const int m = board.size();
		const int n = board.size();
		vector<vector<bool>> visited(m,vector<bool>(n,false));
		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++){
				if(dfs(board,word,0,i,j,visited))
					return true;
			}
		}	
		return false;
	}

private:
	static bool dfs(const vector<vector<char>>& board,const string& word,int index,
					int x,int y,vector<vector<bool>>& visited){
		if(index == word.size()) 
			return true;//terminal 
		if(x < 0 || y < 0 || x > board.size() || y > board[0].size())
			return false;//exceed bonary, terminal 
		if(visited[x][y]) return false;//has visted ,purning 
		if(board[x][y] != word[index]) return false;//not equal,purning 
		visited[x][y] = true;
		bool ret = dfs(board,word,index+1,x-1,y,visited) || //top 
				   dfs(board,word,index+1,x+1,y,visited) ||//bottom 
				   dfs(board,word,index+1,x,y-1,visited) ||//left
				   dfs(board,word,index+1,x,y+1,visited);//right 	
		visited[x][y] = false;
		return ret;
	}

};







































int main(){
	return 0;
}