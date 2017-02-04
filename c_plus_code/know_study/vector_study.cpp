#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void test1(){
	//init a vector 
	vector<int> v{0,1,2,3,4};
	int n1 = 3;
	auto result1 = find(v.begin(),v.end(),n1);
	if(result1 != v.end()) cout << "v contains " << n1 << endl;
	else cout << "v not contains " << n1 << endl;
	//v contains 3
}

void test2(){
	//insert test 
	vector<string> vec{"yin","shuai"};
	vector<string> toInsert{"good"};
	toInsert.insert(toInsert.end(),vec.begin(),vec.end());//same as copy one vector to another vector 
	for(auto val:toInsert){
		cout << val << endl;
	}//good yin shuai 

}

int main(){
	test2();
	return 0;
}