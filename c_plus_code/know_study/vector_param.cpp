#include<iostream>
#include<vector>
using namespace std;


void init_vector(vector<int> &vecTest);
void show_vector(vector<int> &vecTest);
void insert_array_to_vector(vector<int> &vecTest,int a[]);


void init_vector(vector<int> &vecTest){
	for(int i=0;i<10;i++){
		//push_back 
		vecTest.push_back(i);
		cout << i << endl;
	}
	cout << "size of vecTest" << sizeof(vecTest)/sizeof(vecTest[0]) << endl;
	cout << "other size is " << vecTest.size() << endl;
	vector<int>::iterator it = vecTest.begin();
	cout << *(++it) <<endl;
	cout << sizeof(it) << endl;

}

void exchange(int &x,int &y){
	int tmp = x;
	cout << "the address of x is " << &x << endl;
	cout << "the value of x is " << x <<endl;
	x = y;
	y = tmp;
	cout << "x is " << x << "y is " << y<< endl;


}

void exchange2(int *x,int *y){
	cout << "test of x is " << x << endl;
	int * tmp = x;
	x = y;
	cout << "test of x1 is " << x << endl;
	y = tmp;

}

void exchange3(int *a,int *b){
	cout << "the address of a is " << a <<endl;
	int tmp = *a;
	*a = *b;
	*b = tmp;
	return;
}
//http://www.jb51.net/article/54049.htm
int main(){


	int x =0;
	int y =1 ;
	cout << "the value of x is " << x << endl;
	exchange3(&x,&y);
	cout << "the value of x is " << x << endl;
	return 0;

	int a = 0;
	int b = 1;
	cout << "a is" << a << "and b is " << b << endl;
	cout << "the address of a is " << &a << endl;
	exchange2(&a,&b);
	cout << "a is" << a << "and b is " << b << endl;
	cout << "the address of a is " << &a << endl;
	return 0;



	//define a vector 
	vector<int> vec;
	//init the vector 
	init_vector(vec);
	return 0;
}