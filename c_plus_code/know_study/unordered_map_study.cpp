#include<iostream>
#include<string>
#include<map>
#include<unordered_map>
#include<vector>
using namespace std;


/*
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
 */
void test1(){
	map<string,int> ageMap;
	ageMap.insert(make_pair("yinshuai",25));
	ageMap.insert(make_pair("yinshuang",26));
	ageMap.insert(make_pair("lipengfei",25));
	map<string,int>::const_iterator map_it = ageMap.begin();
	int agevalue;
	while(map_it != ageMap.end()){
		agevalue = map_it->second;
		map_it++;
		cout << agevalue << endl;//25 25 26

	}
	unordered_map<string,int> unorderedAgeMap;
	unorderedAgeMap.insert(make_pair("yinshuai",25));
	unorderedAgeMap.insert(make_pair("yinshuang",26));
	unorderedAgeMap.insert(make_pair("lipengfei",25));
	auto umap_iter = unorderedAgeMap.begin();
	while(umap_iter!= unorderedAgeMap.end()){
		agevalue = umap_iter->second;
		umap_iter++;
		cout << agevalue << endl;
	}//25 25 26 
}

void test2(){
	unordered_map<string,vector<string>> unordered_map;
	//construct vector 
	vector<string> vecstring1(2,"yin");//["yin","yin"]
	vector<string> vecstring2(2,"shuai");
	vector<string> vecstring3(2,"good");
	unordered_map.insert(make_pair("yin",vecstring1));
	unordered_map.insert(make_pair("shuai",vecstring2));
	unordered_map.insert(make_pair("good",vecstring3));
	auto iter = unordered_map.begin();
	string key;
	vector<string> value;
	while(iter!= unordered_map.end()){
		key = iter->first;
		cout << "the key is :" << key << endl;
		value = iter->second;
		//iterator the vector<string> value;
		string valueString;
		for(auto iter=value.begin();iter!=value.end();iter++){
			valueString += *iter + " ";
		}
		cout << "the value is:" << valueString << endl;
		++iter;

	}
	/*
the key is :yin
the value is:yin yin 
the key is :good
the value is:good good 
the key is :shuai
the value is:shuai shuai 
	*/

}

void test3(){
	unordered_map<string,string> unordered_map;
	unordered_map.insert(make_pair("yinshuai","good boy"));
	unordered_map.insert(make_pair("lpf","bad boy"));
	if(unordered_map.find("yinshuai") != unordered_map.end())
		cout << "has found" << endl;
	else cout << "not found " << endl;//has found 
}

void test4(){
	unordered_map<string,string> um;
	um = {{"yinshuai","2015140920"},{"fengchaolei","2015140852"}};
	cout << "um map contains " << endl; 
	for(auto it=um.cbegin();it!=um.cend();++it){
		cout << " " << it->first << ":" << it->second << endl;
		cout << "size is " << sizeof(it->first) << endl;
		it->first = "what";
	}
	/*
	um map contains 
    fengchaolei:2015140852
    yinshuai:2015140920

	*/
	auto itb = um.begin();
	cout << itb->first << endl;
}


int main(){
	// test1();
	test4();



}

