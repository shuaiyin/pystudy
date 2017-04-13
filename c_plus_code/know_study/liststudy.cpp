#include<iostream>
#include<list>
#include<algorithm>
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


void test3(){
   int data[6] = {3,5,7,9,2,4};
   list<int> lidata(data,data+6);
   for(list<int>::iterator iter = lidata.begin();iter!=lidata.end();iter++)
   		cout << *iter << endl;
   cout << "the front item is  " <<  lidata.front() << endl;//3
   cout << "the last item is " << lidata.back() << endl;//4

   //reverse test 
   lidata.reverse();
   for(list<int>::iterator iter = lidata.begin();iter!=lidata.end();iter++){
   	  cout << *iter << " ";
   }
   cout << endl;//4 2 9 7 5 3 

}

void test4(){
	list<int> listOne({1,2,3,4,5});
	list<int> listTwo({6,7,8,9});
	listOne.splice(listOne.begin(),listTwo);
	//print listOne
	for(list<int>::iterator iter = listOne.begin();iter!= listOne.end();iter++)
		cout << *iter << " ";
	cout << endl;
	//print listTwo
	for(list<int>::iterator iter = listTwo.begin();iter!= listTwo.end();iter++)
		cout << *iter << " ";
	cout << endl;//and listTwo is empty 
	cout << " listTwo is empty after splice ? " << listTwo.empty() << endl;//the result is 1 
}



void test5(){
	list<int> a({1,2,3,4,5});
	list<int> b({6,7,8,9,10});
	auto iter = next(a.begin());
	a.splice(a.begin(),a,++iter);
	iter = a.begin();
	while(iter != a.end()){
		cout << *iter << endl;
		iter++;
	}

}





int main(){

	test5();
	return 0;
}