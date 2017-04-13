#include<iostream>
#include<string.h>
using namespace std;

int a;
char *p1;

void test1(){
	int b;
	char s[] = "abc";
	char *p2;
	const char *p3 = "123456";
	static int c = 0;
	p1 = (char*)malloc(10);
	p2 = (char*)malloc(20);
	strcpy(p1,"123456");
}

void test2(){
   const char* a = "yinshuai good day";
   cout << strlen(a) << endl;//17
   cout << sizeof(a) << endl;//8
   cout << "other tests " << endl;
   char b[] = "yinshuai good day";
   cout << sizeof(b) << endl;//18
   cout << strlen(b) << endl;//17	
}

class Test{
private:
	int age;
public:
	Test(int age,int sex):age(age){}
	int getAge()const{
		// age = 15;//assignment of member ‘Test::age’ in read-only object
		return age;
	}
};


class A{
public:
	virtual void foo(){
		cout << "A::foo() is called " << endl;
	}

};

class B:public A{
public:
	void foo(){
		cout << "B::foo() is called " << endl;
	}
};

int main(){
	A* a = new B();
	a->foo();//B::foo() is called
	return 0;
}