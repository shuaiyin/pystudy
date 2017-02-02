#include<iostream>
using namespace std;
//http://wenku.baidu.com/link?url=K4Vul2hUzkXTpDKPIx9M-QWqmOhn_E2Nw3XuTKvlLpW2WwUfvH40B4_XEjzESughsuW3YdOKOnQzzeUVQ81nMxCXRRVHtz1lJqvM3G4jEeS

//value transfer 
void value_exchange(int x ,int y){
	/*
	value_exchange(a,b)
	that equal to int x =a ,int y =b 
	*/
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	cout << "the value of x is " << x << endl;
}



int main(){
	int a = 1;
	int b = 2;
	value_exchange(a,b);
	return 0;
}
