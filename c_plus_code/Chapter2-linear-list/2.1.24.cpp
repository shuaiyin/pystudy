#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

class Solution{
public:
	int singleNumber(vector<int> &nums){
		const int W = sizeof(int)*8;//get the bit number of the integer 
		int count[W];
		fill_n(count,W,0);//the first param is the pointer 
		for(auto iter=nums.begin();iter!=nums.end();++iter){
			for(int j=0;j<W;j++){
 				count[j] += (*iter >> j) & 1;
 				count[j] %= 3;
			}
			cout << "[";
			for(int k=0;k<W;k++){
				cout << count[k] << ",";
			}
			cout << "]" << endl;
			

		}
		int result=0;
		for(int i=0;i<W;i++){
			result += (count[i] << i);
		}
		return result;

	}

};


int main(){

int arr[] = {30,15,30,30};
Solution so = Solution();
std::vector<int> vect(arr,arr+4);
int result = so.singleNumber(vect);
return 0;
int count[5];
fill_n(count,5,1);
for(int i=0;i<5;i++){
	cout << count[i] << endl;
}
cout << endl;
int a = 7;
// int b = a >> 1;
int b = a & 1;
cout << b << endl;
// cout << sizeof(count)/sizeof(int) << endl;
return 0;
}
