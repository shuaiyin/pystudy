#include<iostream>
using namespace std;

template<typename T>
T minVal(T x,T y){
	return (x < y) ? x:y;
}//you'd better not user min to named this funciton,for that it has been used by system 

void test1(){
	//return the min value 
	int a=10,b=12;
	int result = minVal(10,12);
	cout << result << endl; //10
	char ac = 'a';
	char bc='b';
	char res = minVal(ac,bc);
	cout << res << endl;//a
}

class TemplateTest{
public:
	template<typename myval>
	myval getMax(myval x,myval y){
		return x > y ? x:y;
	}
};

void test2(){
	auto tIns = TemplateTest();
	cout << tIns.getMax(10,12) << endl;//12
	cout << tIns.getMax('c','a') << endl;//'c'
}

class TemplateSec{
public:
	int getMax(int x,int y){
		return getMax(x,y);
	}
	template<typename inputVal>
	int getMax(inputVal x,inputVal y){
		return x > y ? x:y;
	}
};

void test3(){
	auto ts = TemplateSec();
	int result = ts.getMax(10,20);
	cout << result << endl;
}



int main(){
	test3();
	return 0;

}