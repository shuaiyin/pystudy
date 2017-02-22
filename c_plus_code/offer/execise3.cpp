#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	//first method start from the top right corner 
	bool Find(vector<vector<int>>& vec,int rows,int columns,int number){
		bool found = false;
		if(!vec.empty() && rows > 0 && columns > 0){
			int rowRecord = 0;
			int column = columns-1;
			while(rowRecord < rows && column >=0){
				if(vec[rowRecord][column] == number){
					found = true;
					break;
				}else if(vec[rowRecord][column] > number){
					--column;
				}else{
					++rowRecord;
				}
			}
		}
		return found;
	}
	//second method start from the lower left quarter 
	bool FindMethod(vector<vector<int>>& vec,int rows,int columns,int number){
		bool found = false;
		if(!vec.empty() && rows > 0 && columns > 0){
			int columnRecord = 0;
			int row = rows -1;
			while(columnRecord < columns && row >=0){
				if(vec[row][columnRecord] == number){
					found = true;
					break;
				}else if(vec[row][columnRecord] > number){
					--row;
				}else{
					++columnRecord;
				}
			}
		}
		return found;

	}

};


int main(){
	vector<vector<int>> vec({{1,2,3},{4,5,6},{7,8,9}});
	auto result = Solution().Find(vec,3,3,5);
	cout << "the method of top right corner:" << result << endl;
	result = Solution().FindMethod(vec,3,3,5);
	cout << "the method of lower left quarter:" << result << endl;



	return 0;
}