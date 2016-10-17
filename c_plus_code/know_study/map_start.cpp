#include<iostream>
#include<map>
#include<string>

//the insert with pair version  will return an object consist of  an iterator and
// a bool value ,the bool value indicate the result of the insert(eg,0 or 1) 
// if the key already in the map,the bool value also return false with no value insert
using namespace std;
int main(){

  map<string,int> word_count;//initialize a map 
  word_count.insert(map<string,int>::value_type("Anna",1));//one way to insert a pair element 
  word_count.insert(make_pair("yinshuai",3));//a simplify way to insert pair element 
  typedef map<string,int>::value_type valType;
                                  //using typedef to simplify the complexity appear of insert pair 
  word_count.insert(valType("heheda",250));
  string word;
  cin >> word;
  pair<map<string,int>::iterator,bool> ret = 
       word_count.insert(make_pair(word,1));
  cout << ret.second << endl;
  cout << "the second test about word statistic" << endl;
  while(cin >> word){
    pair<map<string,int>::iterator,bool> ret= 
            word_count.insert(make_pair(word,1));
    if(!ret.second)
       ++ret.first->second;
    cout << word << " with value " << ret.first->second << endl;
  }
}
