#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
	void rotate(vector< vector<int> > &matrix){
		const int n = matrix.size();
		for(int i=0;i<n;++i)
			for(int j=0;j<n-i;++j)
				swap(matrix[i][j],matrix[n-1-j][n-1-i]);
		for(int i=0;i<n/2;++i)
			for(int j=0;j<n;++j){
				swap(matrix[i][j],matrix[n-1-i][j]);
			}
	}
};


int main(){
    int arr[] = {1,2,3};
    std::vector<int> vect(arr,arr+3);
    auto iter = vect.begin();
    swap(*iter,*next(iter,1));
    for(int i=0; i<3;i++){
    	cout << vect[i] << endl;
    }

    // for(auto iter = vect.begin();iter!=vect.end();++iter){
    // 	cout << *iter << endl;
    // }



	return 0;
}