#include<iostream>
#include<string>
using namespace std;

class Student{
public:
	Student(int n,int a,float s):num(n),age(a),score(s){}
	void total();
	static float average();//static function 
private:
	int num;
	int age;
	float score;
	static float sum;//static memeber
	static int count;
};

void Student::total(){
	sum += score;//accumulate sum score 
	count++;
}
float Student::average(){
	return sum/count;
}
float Student::sum;//init static member 
int Student::count;//

void StudentTest(){
		Student stu[3] = {
		Student(1001,18,70),
		Student(1002,19,78),
		Student(1005,20,98)
	};
	int n = 3;
	for(int i=0;i<n;i++)
		stu[i].total();
	cout << "the average score of " << n << " student is " << Student::average() << endl;
}

int main(){
	StudentTest();
	return 0;

}