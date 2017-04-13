#include<iostream>
#include<stack>
#include<vector>
#include<stdexcept>
using namespace std;



template<class dataType>
class Compare{
private:
	dataType x,y;
public:
	Compare(dataType a,dataType b){
		x = a;
		y = b;
	}
	dataType getMax(){
		return (x > y) ? x:y;
	}

};

template<typename dataType>
class myCompare{
public:
	myCompare(void){}
	~myCompare(void){}
	dataType testcase(dataType val){
		return val;
	}
};

int templateClassTest(){
	myCompare<int> mc;///////////////////////////////////////////////////////////////////////////////////////turn out to be that 
	int  retc = mc.testcase(10);
	cout << retc << endl;
	return 0;
	Compare<int> cmp1(3,7);
	auto ret = cmp1.getMax();
	cout << ret << endl ;//7
	Compare<int> cmp2('a','b');
	char rett = cmp2.getMax();
	cout << rett << endl;//'b'


}





template<class T> 
class CQueue{
public:
	CQueue(void){}//construction method 
	~CQueue(void){} //unconstruction method 
	void appendTail(const T& node){
		stack1.push(node);

	}

	T deleteHead(){

		if(stack2.empty()){
			while(!stack1.empty()){
				T tval = stack1.top();
				stack1.pop();
				stack2.push(tval);
			}
			if(stack2.empty()){
				cout << "queue is empty" << endl;
				return 0;
			}
		}
		T deleteVal = stack2.top();
		stack2.pop();
		return deleteVal;

	}

	stack<T> getStack1(){
		return stack1;
	}

	stack<T> getStack2(){
		return stack2;
	}
private:
	stack<T> stack1;
	stack<T> stack2;
};


void testQueue(){
	CQueue<int> cq;//do not use cq(),for that there is no param in construct method 
	cq.appendTail(11);
	cq.appendTail(12);
	cq.appendTail(13);
	int val = cq.deleteHead();
	cq.deleteHead();
	auto st = cq.getStack2();
	while(!st.empty()){
		cout << st.top() << endl;
		st.pop();
	}

}


class myQueue{
public:
	int deleteHead(){
		if(stack2.empty()){
			while(!stack1.empty()){
				int val = stack1.top();
				stack2.push(val);
				stack1.pop();
			}
		}
		if(stack2.empty()){
			cout << "queue is empty" << endl;
			return 0;
		}
		int deleteNode = stack2.top();
		stack2.pop();
		return deleteNode;

	}

	void appendTail(int val){
		stack1.push(val);
	}



	stack<int> getStack1(){
		return stack1;
	}
	stack<int> getStack2(){
		return stack2;
	}
private:
	stack<int> stack1;//push
	stack<int> stack2;//pop

};



// stack<int> getStack1(){
// 	return stack1;
// }

// stack<int> getStack2(){
// 	return stack2;
// }




int main(){	
	testQueue();
	return 0;
	myQueue myQ = myQueue();
	myQ.appendTail(10);
	myQ.appendTail(11);
	stack<int> ret = myQ.getStack1();

	int val = myQ.deleteHead();
	cout << val << endl;
	return 0;
	while(!ret.empty()){
		cout << ret.top() << endl;
		ret.pop();
	}

	return 0;
}