#include <iostream>
#include<cstring>
#include <cstdlib>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};
void addstudent(Student*&students,int &size){
Student*temp=(Student*)realloc(Student,(size+1)*sizeof(Student));

if (temp==null){
cout<<"memory allocation failed!"<<endl;
exit(1);
}

Student=temp;

cout<<"enter student id:";
cin>>Student[size].id;

cin.ignore();

cout<<"enter student name:";
cin.getline(students[size].name,50);

cout<<"enter student cgpa:";
cin>>Student[size].cgpa;

size++;

}

void displayStudent(Student s){
cout<<"id:"<<s.id;
  cout<<",name:"<<s.name;
  cout<<",cgpa:"<<s.cgpa<<endl;
    }
  
void sortStudents(Student*students,int size){
for(int i=0;i<size-1; i++)
{
for(int j=0; j<size-i-1; j++)
{
if(students[j].id>students[j+1].id)
{
Student temp= students[j];
students[j]=students[j+1];
students[j+1]=temp;
}
}
}
}

void binarySearch(Student*students,int size)
{
int searchid;
cout<<"\nenter student id to search:";
cin>>searchid;

int low=0;
int high = size-1;
bool found = false;

while(low<=high)
{
int mid= (low+high)/2;

if(students[mid].id==searchid)
{
cout<<"\nstudent found!\n";
displayStudent(students[mid]);
found = true;
break;
}
else if(searchid<students[mid].id)
{
high= mid-1;
}
else
{
low=mid+1;
}
}

if(!found)
{
cout<<"\nStudent not found !"<<endl;
}
}

int main()
{
Student*students=null;
int size=0;
int n;

cout<<"enter number of student:";
cin>>n;

for(int i=0; i<n; i++)
{
cout<<"\nenter detail of studnt"<<i+1<<endl;
addStudent(students,size);
}

sortStudents(students,size);

cout<<"\nstudent records"<<endl;
for(int i=0; i<size; i++)
{
displayStudent(students[i]);
}

binarysearch(students, size);

free(students);

return 0;
}
