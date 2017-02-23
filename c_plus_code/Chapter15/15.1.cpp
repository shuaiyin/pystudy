#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;



int main(){
	vector<int> vec({1,3,5,7,9});
	for(auto mem:vec) cout << mem << endl;
	unordered_map<string,string> map;
	map.insert(make_pair("yinshuai","good man"));
	for(auto mem:map){
		cout << mem->first << endl;
	}
	return 0;
}