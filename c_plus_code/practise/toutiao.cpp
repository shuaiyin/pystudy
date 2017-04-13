#include<iostream>
#include<math.h>
using namespace std;
class Test{

public:
	Test(int aa,int bb){
		a = aa--;
		b = a*bb;
	}
	int a;
	int b;
};


void test4(){
	int n[][3] = {10,20,30,40,50,60};
	int(*p)[3];
	p = n;
	cout << p[0][0] << "," << *(p[0]+1) << "," << (*p)[2] << endl;
}


bool isSxh(int inputVal){
	int val = inputVal;
	int sumVal = 0;
	while(val){
		sumVal = sumVal + pow(val%10,3);
		val = val/10;

	}
	if(sumVal == inputVal) return true;
	else return false;
}

int main(){
	int n,m;
	bool hasSxh;
	while(cin >> m >> n){
		hasSxh = false;
		for(int i=m;i<=n;i++){
			if(isSxh(i)){
				cout << i << ' ';
				hasSxh = true;
			}
		}
		if(!hasSxh) cout << "no" << endl;
	}
	return 0;
}