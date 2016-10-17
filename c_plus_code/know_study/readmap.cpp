#include<iostream>
#include<string>
#include<map>
using namespace std;
int main(){
    map<string,int> word_count;
    int occurs = word_count["foobar"];
    cout << occurs << endl;//0  when the ele is not exist, it will create new 
    //find oper will read element  while not insert this element 
    int find_occurs = 0;
    map<string,int>::iterator it = word_count.find("yinshuai");
    if(it != word_count.end())
       occurs = it->second;
    else
       cout << "the key is not exist" << endl; 
    
    

}
