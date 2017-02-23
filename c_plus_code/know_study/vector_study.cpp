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
void test3(){
	vector<int> vec{1,2,3,4,5};
	cout << vec.back() << endl;//5
	for(int val:vec) cout << val << endl;// 1 2 3 4 5
	vec.pop_back();
	for(int val:vec) cout << val << endl;//1 2 3 4
	
}
void test4(){
	vector<int> vec{1,2,3,4,5};
	for(auto iter=vec.rbegin();iter!=vec.rend();iter++){
		cout << *iter << endl;
	}//5 4 3 2  1
}

void test5(){
	vector<int> vec1({1,2,3,4});
	cout << vec1.size() << endl;//4
	vec1.resize(10);
	cout << vec1.size() << endl;//10
     
 
}

int main(){
	test5();
	return 0;
}