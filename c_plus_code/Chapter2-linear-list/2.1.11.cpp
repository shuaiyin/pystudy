#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution{
public:
	int removeElement(vector<int> &nums,int target){
		int index=0;
		for(int i=0;i<nums.size();++i){
			if(nums[i] != target){
				nums[index++] = nums[i];
			}
		}
		return index;
	}

	int removeElement2(vector<int> &nums,int target){
		int size = nums.size();
		int return_index = size;
		for(int i=0;i<size;++i){
			if(nums[i] == target) 
				return_index--;
		}
		return return_index;
	}

	int removeElement3(vector<int> &nums,int target){
		int index=0;
		auto iter_start = nums.begin();
		for(auto iter=iter_start;iter != nums.end(); ++iter){
			if(*iter != target){
				*(iter_start++) = *iter;
				index++;
			}
		}
		for(int i=0;i<nums.size();++i){
			cout << nums[i] << endl;
		}

		return index;

	}


};




int main(){
  int init_arr[] = {52,56,12,56,25,12,12};
  vector<int> vect(init_arr,init_arr+7);
  Solution so = Solution();
  int result = so.removeElement3(vect,12);
  cout << result << endl;
  cout << vect.size() << endl;



}
