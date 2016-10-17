#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
//this include contains unordered_multimap
#include<unordered_map>
//this include contains mulitmp 
#include<map>
using namespace std;

class Solution{
public:
   vector< vector<int> > fourSum(vector<int> &nums,int target){
       vector< vector<int> > result;
       if(nums.size() < 4) return result;
       sort(nums.begin(),nums.end());
       unordered_multimap<int,pair<int,int>> cache;
       for(int i=0;i+1<nums.size();++i){
         for(int j=i+1;j<nums.size();++j)
            cache.insert(make_pair(nums[i] + nums[j],make_pair(i,j)));
            
       }

      for(auto i=cache.begin();i!=cache.end();++i){
        int x = target - i->first;
        auto range = cache.equal_range(x);
        for(auto j = range.first; j!=range.second;++j){
          auto a = i->second.first;
          auto b = i->second.second;
          auto c = j->second.first;
          auto d = j->second.second;
          if(a != c && a != d && b != c && b != d){//this place it 
            vector<int> vec = {nums[a],nums[b],nums[c],nums[d]};
            sort(vec.begin(),vec.end());
            result.push_back(vec);
          }
        }
      }

      sort(result.begin(),result.end());
      result.erase(unique(result.begin(),result.end()),result.end());
      return result;

      
  }

};

int main(){
  int init_arr[] = {1,0,-1,0,-2,2};
  int arr_len = sizeof(init_arr)/sizeof(int);
  vector<int> init_vect(init_arr,init_arr + arr_len);
  auto iter = init_vect.begin(); 
  const int target = 0;
  Solution so1= Solution();
  vector< vector<int> >  result = so1.fourSum(init_vect,target);
  for(int i=0; i< result.size();++i){
    cout << "[";
    for(int j=0;j<4;++j)
      cout  << result[i][j] << ",";
      cout <<"]" << endl;
  }


  return 0;
  unordered_map<string,string> um;
  um.insert(make_pair("yinshuai","good man"));
  um.insert(make_pair("yinshuang","good girl"));
  cout << um.count("yinshuai") << endl; 
  um.erase(um.begin(),next(um.begin()));
  cout << um.count("yinshuai") << endl;
  cout << "this is a separater " << endl; 
  unordered_multimap <int,string> um333;
  um333.insert(make_pair(10,"yinshuai"));
  um333.insert(make_pair(8,"linlinafeng"));
  um333.insert(make_pair(8,"yinfenggang"));
  //get the count 
  unordered_multimap<int,string>::iterator iter333;
  
  // cout << sizeof(return_result) << endl;
  return 0;  

  unordered_multimap<string,string> umap;
  umap.insert(make_pair(string("yinshuai"),string("sex:boy")));
  umap.insert(make_pair(string("yinshuai"),string("school:bupt")));
  //username we'll find 
  string search_username("yinshuai");
  //how many entries are there for this author 
  typedef unordered_multimap<string,string>::size_type sz_type;
  sz_type entries = umap.count(search_username);
  cout << entries << endl;
  //get iterator for the first entry for this author 
  unordered_multimap<string,string>::iterator iter1 = umap.find(search_username);
  //look through the number of entries there are for this author 
  for(sz_type cnt = 0; cnt != entries; ++cnt,++iter1){
    cout << iter1->second << endl;
  } 

  return 0;
  auto uiter = umap.begin();
  cout << uiter->second << endl;

  return 0;
  Solution so = Solution();
  so.fourSum(init_vect,0);
  return 0;
}