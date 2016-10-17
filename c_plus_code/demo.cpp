#include <iostream>
#include <string.h>
#include <map>
using namespace std;
class CGoods{
private:
    char Name[21];
    int Amount;
    float Price;
    float Total_value;
public:
    void RegisterGoods(char*,int,float);//register new goods,this is the head 
    float getPrice(); 
    int getAmount(){ return Amount;};//define the function in class directly 
};

//you can define the funciton in the out of the class 
void CGoods::RegisterGoods(char* name,int amount,float price){
  strcpy(Name,name);
  Amount = amount;
  Price = price;
}
 float CGoods::getPrice(){
  return Price;
}



int main(void)
{
    CGoods cgoods;//instance the class 
    cgoods.RegisterGoods("yinshuai",25,23.6);// 
    cout << cgoods.getPrice();
    cout << cgoods.getAmount();
    cout << "hello worldheh\n";
    cout << endl;
    map<string,int> word_count;//empty map from string to int 
    string word = "yinshuai";
    while(cin >> word)
      ++word_count[word];  
    // map<string,int>::const_iterator map_it = w
    // return 0;


}
