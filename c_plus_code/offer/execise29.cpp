#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
	int MoreThanHalfNum_Solution(vector<int> numbers) {
		auto size = numbers.size();
		if(!size) return 0;
		int middle = size >> 1;
		int start = 0;
		int end = size - 1;
		int index = Partition(numbers,start,end);
		while(index != middle){
			if(index > middle){
				end = index - 1;
				index = Partition(numbers,start,end);
			}else{
				start = index + 1;
				index = Partition(numbers,start,end);
			}
		}
		int result = numbers[middle];
		return result;
    }
private:
	int Partition(vector<int> numbers,int start,int end){
		while(start != end){
			
		}
		return 0;

	}


};


int main(){
	vector<int> inputVec({1,2,3,2,2,2,5,4,2});
	auto ret = Solution().MoreThanHalfNum_Solution(inputVec);

	return 0;
}