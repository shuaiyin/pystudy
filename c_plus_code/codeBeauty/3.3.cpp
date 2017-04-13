#include<iostream>
#include<string>
using namespace std;



int minValue(int t1,int t2,int t3){
	int minVal = t1;
	if(t2 < minVal)
		minVal = t2;
	if(t3 < minVal)
		minVal = t3;
	return minVal;
}



int CalculateStringDistance(string strA,int pABegin,int pAend,string strB,int pBBegin,int pBEnd){
	if(pABegin > pAend){
		if(pBBegin > pBEnd)
			return 0;
		else
			return pBEnd - pBBegin + 1;
	}
	if(pBBegin > pBEnd){
		if(pABegin > pAend)
			return 0;
		else 
			return pAend - pABegin + 1;
	}
	if(strA[pABegin] == strB[pBBegin]){
		return CalculateStringDistance(strA,pABegin+1,pAend,strB,pBBegin+1,pBEnd);
	}else{
		int t1 = CalculateStringDistance(strA,pABegin,pAend,strB,pBBegin+1,pBEnd);
		int t2 = CalculateStringDistance(strA,pABegin+1,pAend,strB,pBBegin,pBEnd);
		int t3 = CalculateStringDistance(strA,pABegin+1,pAend,strB,pBBegin+1,pBEnd);
		return minValue(t1,t2,t3) + 1;
	}
}




int main(){
	string A("xabcdae");
	string B("xfdfa");
	int aSize = A.size();
	int bSize = B.size();
	auto val = CalculateStringDistance(A,0,aSize,B,0,bSize);
	cout << val << endl;	
	return 0;
}