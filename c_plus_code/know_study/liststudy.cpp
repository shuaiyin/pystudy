#include<iostream>
#include<list>
using namespace std;

void test1(){
	list<int> testlist{1,2,3,4};
	for(auto val:testlist){
		cout << val << endl;
	}// 1 2 3 4
	for(list<int>::iterator iter=testlist.begin();iter!=testlist.end();iter++){
		cout << *iter << endl;
	}//1 2 3 4 

}

void test2(){
	list<int> testlist{1,2,3,4,5,6,7,8,9};
	//find 4th member in the list.a little complexiy
	list<int>::iterator it=testlist.begin();
	for(int i=0;i<4;i++){
		++it;
	}
	cout << "the forth value of the list is " << *it << endl;
	//the forth value of the list is 5
}




int main(){

	test2();
	return 0;
}