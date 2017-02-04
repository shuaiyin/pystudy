#include<iostream>
#include<string>
#include<algorithm>
using namespace std;


void test1(){
    string ss = "i am a bat, i am not battle";
    string sub = "bat";
    int n=0;//appear times;
    int pos;
    pos = ss.rfind(sub);//21
    while(pos != string::npos){
        ++n;
        cout << "pos is " << pos << endl;
        pos = ss.rfind(sub,pos-1);
    }
    cout << "numer of appearance is " << n << endl;
} 

void test2(){
    string my_str = "Hello world";
    string::iterator it = my_str.begin();
    cout << *it << endl; //H
    cout << *(it+1) << endl;//e
    for(it=my_str.begin();it!=my_str.end();it++){
        cout << *it << endl;
    }
    //H e l l o w o r l d 
}


void test3(){
    string s = "god live no tips";
    for(string::iterator it=s.begin();it!=s.end();it++){
        cout << *it << endl;
    }
}


void test4(){
    string s = "What a good day,But When to Cry";
    transform(s.begin(),s.end(),s.begin(),::tolower);
    cout << s << endl;//what a good day,but when to cry
    auto left = s.begin(),right=prev(s.end());
    cout <<  *left << endl;//w
    cout << *right << endl;//y
}

void test5(){
    string s = "what is the weather today";
    for(string::iterator it=s.begin();it!=s.end();it++){
        char tmp = *it;
        int result = isalnum(tmp);
        cout << result << endl;
    }
}

void test6(){
    string quip("hello world");
    cout << quip.size() << endl;//11
    quip.resize(12);
    cout << quip.size() << endl;//12
}
void test7(){
    string s = "yinshuai good day";
    cout << s <<endl;
}
void test8(){
    string mymsg = "i am a batman and you battle?";
    int pos2 = mymsg.find("bat");
    while(pos2 != string::npos){
        mymsg.replace(pos2,3,"cat");
        pos2 = mymsg.find("bat",pos2+1);
    }
    cout << mymsg << endl;//i am a catman and you cattle?
}

void test9(){
    string s = "yinshuai ";
    sort(s.begin(),s.end());//need algorithm lib
    cout << s << endl;//ahiinsuy
}

//stl algorithm of find 
template<class InputIterator,class T>
InputIterator myfind(InputIterator first,InputIterator last,const T&value){
    for(;first!=last;first++)
        if(*first == value) break;
    return first;//if finally not found,return last pointer 
}


void test10(){
    vector<int> testvect;
    int i=0;
    while(i<10){
        testvect.push_back(i);
        i++;
    }
    vector<int>::iterator vreturn;
    const int findVal = 5;
    vreturn = myfind(testvect.begin(),testvect.end(),findVal);
    cout << *vreturn << endl;//5
}


void test11(){
    string aa = "hello world";
    string::reverse_iterator it =  aa.rbegin();
    cout << *it << endl;//d
    cout << *(++it) << endl;//d
    int dis = distance(aa.begin(),aa.begin()+1);//
    cout << dis << endl;//1
    dis = distance(aa.rbegin(),aa.rbegin()+1);
    cout << dis << endl;//1
}

void test12(){
    //string to c_str 
    string str = "hello world";
    char *s = (char *)str.c_str();//transfer  string to c style str 
    cout << s << endl;
    string str1 = "good day";//do not need using type trans again 
    const char *ss = str1.c_str();
    cout << ss << endl;
    //if not use type trans,it will throw "invalid conversion from ‘const char*’ to ‘char*"  exception 
}



int main(){
    test12();
	return 0;
}