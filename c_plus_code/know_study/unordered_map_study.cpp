#include<iostream>
#include<string>
#include<map>
using namespace std::tr1;

int main(){
   unordered_map<string,int> months;
   months["january"] = 31;
   months["feburary"] = 28;
   cout << months["january"] << endl;
   return 0;


}