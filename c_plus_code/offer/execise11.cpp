#include<iostream>
using namespace std;


class Solution{
public:
	bool g_InvaidInput = false;
	double Power(double base,int exponent){
		g_InvaidInput = false;
		if(equal(base,0.0) && exponent <0){
			g_InvaidInput = true;
			return 0.0;
		}
		unsigned int absExponent = (unsigned int)(exponent);
		if(exponent < 0) absExponent = (unsigned int)(-exponent);
		double result = PowerWithUnsignedExponent(base,absExponent);
		if(exponent < 0)
			result = 1.0/result;
		return result;
	}

	bool equal(double num1,double num2){
		if((num1-num2 > -0.0000001) && (num1-num2 < 0.0000001)) return true;
		else return false;
	}
	double PowerWithUnsignedExponent(double base,unsigned int exponent){
		double result = 1.0;
		while(exponent){
			result *= base;
			exponent--;
		}
		return result;
	}
	double PowerWithUnsignedExponentFastest(double base,unsigned int exponent){
		if(exponent == 0) return 1;
		if(exponent == 1) return base;
		double result = PowerWithUnsignedExponentFastest(base,exponent >> 1);
		result *= result;
		if(exponent & 0x1 == 1)
			result *= base;
		return result;
	}
};


int main(){
	auto ret = Solution().Power(0.15269636,-2);
	cout << ret << endl;
	return 0;
}