#include <iostream>
#include <vector>
#include <numeric>
#include <limits>
#include<stdlib.h>

using namespace std;

/** 请完成下面这个函数，实现题目要求的功能 **/
 /** 当然，你也可以不按照这个模板来作答，完全按照自己的想法来 ^-^  **/
int findMissedBuilding(string route) {


}

int main() {
	// string a("yinshuai");
	
	// return 0;
 //    int res;

    string _route;
    getline(cin, _route);
    string center_route;
    center_route = _route.substr(1,_route.length()-2);
    string other_route;
    for(int i=center_route.length()-1;i>=0;i--){
    	other_route  = other_route + center_route[i];
    }
    cout << atoi(other_route) << endl;

    
    // res = findMissedBuilding(_route);
    // cout << res << endl;
    
    return 0;

}