#include<iostream>
using namespace std;


class A{
protected:
	int m_data;
public:
	A(int data = 0){
		m_data = data;
	}
	int GetData(){
		return doGetData();
	}
	virtual int doGetData(){
		return m_data;
	}
};


class B:public A{
protected:
	int m_data;
public:
	B(int data = 1){
		m_data = data;
	}
	int doGetData(){
		return m_data;
	}
};


class C:public B{
protected:
	int m_data;
public:
	C(int data = 2){
		m_data = data;
	}

};




//
int test1(){
	C cIns(10);
	cout << cIns.GetData() << endl;//1
	cout << cIns.A::GetData() << endl;//1
	cout << cIns.B::GetData() << endl;//1
	cout << cIns.C::GetData() << endl;//1
	cout << cIns.doGetData() << endl;//1
	cout << cIns.A::doGetData() << endl;//0
	cout << cIns.B::doGetData() << endl;//1
	cout << cIns.C::doGetData() << endl;//1

}

int main(){
	test2();
	return 0;
}
