#include <iostream>  
#include <stdio.h>  
#include <string.h>  
#include <stdlib.h>
#include <assert.h>  
using namespace std;  





//memcpy 
void *memory(void *dst,const void *src,size_t s)  
{  
   const char* psrc=static_cast<const char*>(src);  
    char* pdst=static_cast<char*>(dst); //强制类型转化. 把某个类型转成字符指针类型, 
  
    if(psrc==NULL||pdst==NULL)  
        return NULL;  
  
    if(pdst>psrc&&pdst<(psrc+s)) //override  
    {  
        for(size_t i=s-1;i!=-1;i--)  
            pdst[i]=psrc[i];  
    }  
    else  
    {  
        for(size_t i=0;i<s;++i)  
            pdst[i]=psrc[i];  
    }  
    return dst;  
}  



//strcpy 
void  *mystrcpy(char* dst,char* src){
    if(dst == nullptr || src == nullptr) return nullptr;
    //assert((dst != nullptr) && (src != nullptr));
    char* address = dst;
    while((*dst++ = *src++) != '\0');//still need char '\0' last 
    return address;
}


#include<limits.h>

void LoopMove(char* pStr,int steps){
  int b = strlen(pStr) - steps;
  cout << b << endl;
  cout << MAX_LEN << endl;

}


int test1(){
  char src[10] = "abcdefghi";
  memory(src+5,src,10);
  printf("%s\n",src);
  cout << sizeof(src) << endl;
}

void test2(){
  char src[10] = "abcdefghi";
  char dst[3];
  memory(dst,src,5);

  cout << dst << endl;
}


void test3(){
  char src[10] = "abcdefghi";
  char dst[10];
  mystrcpy(dst,src);
  cout << dst << endl;
}


void test4(){
  int a[] = {1,2,3,4};
  int b[2];
  memcpy(b,a,4);//only copy 4 bytes just one int number 
  for(int i=0;i<2;i++)
    cout << b[i] << endl;
  //1 0 
}

void test5(){
  char s[] = "123456789";
  char d[] = "123";
  strcpy(d,s);
  printf("%s,\n%s",d,s);
}

void test7(){
  char pstr[] = "abcdefghi";
  int steps = 2;
  LoopMove(pstr,steps);
}




int main()  
{  
  test7();
  return 0;
   char buf[100]="abcdefghijk";  
   memory(buf+2,buf,5);  
   printf("%s\n",buf+2);  
   return 0;  
}  