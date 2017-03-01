#include<iostream>
#include<vector>
#include<stack>
using namespace std;


class Solution{
public:
	//yinshuai self write cow net ac 0228
	bool IsPopOrder(vector<int> pushV,vector<int> popV) {
		bool result = false;
		if(pushV.size() != popV.size()) return result;
		stack<int> stackHelper;
		auto pushVBeg = pushV.begin();
		for(auto val:popV){
			if(stackHelper.empty() || stackHelper.top() != val){
				while(pushVBeg != pushV.end() && val != *pushVBeg){
					stackHelper.push(*pushVBeg);
					pushVBeg++;
				}
				if(pushVBeg != pushV.end()){
					pushVBeg++;
				}else{
					break;
				}
			}else{
				stackHelper.pop();
			}
		}
		if(pushVBeg == pushV.end() && stackHelper.empty()) result = true;
		return result;
    }
};


int main(){
	vector<int> pushV({1,2,3,4,5});
	cout << *pushV.end() << endl;
	return 0;
	vector<int> popV({4,5,3,2,1});
	auto ret = Solution().IsPopOrder(pushV,popV);
	cout << ret << endl;
	return 0;
}