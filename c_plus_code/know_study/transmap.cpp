#include<iostream>
#include<string>
#include<map>
using namespace std;

int main(int args char ** argv){
  //map to hold the word transformation pairs
  //key is the word to look for in the input
  //value is word to use in the output 
  map<string,string> trans_map;
  string key,value;
  if(argc != 3)
     throw runtime_error("wrong number of argument");
  //open transformation file and check that open succeeded 
  //ifstream use as  read content from disk to memory
  ifstream map_file;
  if(!open_file(map_file,argv[1]))
     throw runtime_error(" no transformation file "):
  //read the transformation map and build the map 
  while(map_file >> key >> value)
     trans_map.insert(make_pair(key,value));

  

}
