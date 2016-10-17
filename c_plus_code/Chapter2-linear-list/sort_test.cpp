#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

int main(){
 int myints[] = {32,71,12,56,96,55,25,78};
 std::vector<int> myvector(myints,myints+8);
 std::sort(myvector.begin(),myvector.begin()+4);
 for(std::vector<int>::iterator it = myvector.begin();
 	 it != myvector.end(); ++it){
 	 std::cout << ' ' << *it << std::endl;
 }
 // for(int i=0;i<myvector.size();i++){

 // 	std::cout << myvector[i] << std::endl;

 // }
 return 0;

}
