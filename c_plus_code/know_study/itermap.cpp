#include<iostream>
#include<string>
#include<map>
using namespace std;
int main(){
  map<string,string> word_count ;
  word_count.insert(make_pair("yinshuai","2015140920"));
  word_count.insert(make_pair("liyafei","20151408888"));
  word_count.insert(make_pair("wenjing","20151406666"));
  //get iterator positioned on the first element 
  map<string,string>::const_iterator map_it = word_count.begin();
  //for each element in the map 
  while(map_it != word_count.end()){
     //print the element key,vlaue pairs;
     cout << map_it->first << " 's userid is  " 
          << map_it->second << endl;
     ++map_it;// increment iterator to denote the next element 
   }
  
}
