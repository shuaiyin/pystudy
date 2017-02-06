#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class LRUCache{
private:
	struct CacheNode{
		int key;
		int value;
		CacheNode(int k,int v):key(k),value(v){}
	};
public:
	LRUCache(int capacity){
		this->capacity = capacity;
	}
	int get(int key){
		if(cacheMap.find(key) == cacheMap.end()) return -1;
		//move current visit node to the head of the list,and update address in the map
		cacheList 
	}

};