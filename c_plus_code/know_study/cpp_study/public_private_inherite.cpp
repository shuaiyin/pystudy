#include<iostream>
using namespace std;



//public inherit and private inherit 
class Animal{
public:
	Animal(){}	
	void eat(){
		cout << "eat" << endl;
	}
};

class Giraffe:private Animal{//private inherit  
public:
	Giraffe(){}
	void StrechNeck(){
		cout << "Strech neck  " << endl;
	}
	void take(){
		eat();//ok
	}
};


class Dog:protected Animal{//protected inherit (same as private inherit )
public:
	Dog(){}
	void eating(){
		eat();
	}

};

class Cat:public Animal{//public inherit 
public:
	Cat(){}
	void Meaw(){
		cout << "meaw " << endl;
	}
};

void Func(Animal& an){
	an.eat();
}

class Parent{
protected:
	int leg = 2;
};

class Child:public Parent{
public:
	int getLegCount(){
		leg = 300;
		return leg;
	}
};


int main(){

	Cat dao;
	Giraffe gir;
	Func(dao);//eat 
	// Func(gir);//error
	gir.take();//eat 
	Dog dog;
	dog.eating();//eat
	// dog.eat();//error not accessible .

	// auto ret = Parent().leg;
	// cout << ret << endl;
	auto ret = Child().getLegCount();
	cout << ret << endl;	
	return 0;
}