#include<iostream>
using namespace std;



int main(){
	//first show the space need of pointer 
	char *testpointer;//define a pointer 
	cout << "the size of pointer is "<< sizeof(testpointer) << endl;
	//the result is 8,that to say the size of pointer in 64bit system
	//is 8 bytes 
	cout << "the size of int is " << sizeof(int) << endl;//4 bytes 
	cout << "the size of double is " << sizeof(double) << endl;//8 bytes
	//----other test 
	cout << "-----------" << endl;
	char *testString = "yinshuai";
	cout << testString << endl;//yinshuai,may inner iter 
	cout << &testString << endl;//0x7fff90851620
	cout << sizeof(testString) << endl;//8
	cout << *testString << endl;//y 
	cout << *(testString+1) << endl;//i
	cout << *(testString+2) << endl; //n
	/*we can figure out that the type of testString is pointer,
	  although when we use cout it printf all string.(may inner iter?)
	*/
	cout << "----- test end----" << endl;

	cout << "----const char * and char test----" << endl;
	/*
	the content of the const char * is read only
	*/
	const char * const_pointer = "hello world";//define a const p
	cout << *const_pointer << endl;//h
	// *const_pointer = "z";//throw out error 
	cout << &const_pointer << endl;//0x7ffc93e0d218
	char * other_pointer = "good day";
	cout << &other_pointer << endl;//0x7ffc93e0d210
	const_pointer = other_pointer;
	cout << & const_pointer << endl;//0x7ffebde65808
	cout << const_pointer << endl;//good day
    //if the content of the string is unchangable,you can use const char 







 

}
