#include <iostream>
#include<cstring>
#include <cstdlib>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};
void addstudent(student*&student,int&size){
student*temp=(student*)realloc(student,(size+1)*sizeof(student));

if (tem==null){
cout<<"memory allocation failed!"<<endl;
exit(1);
}

student=temp;

cout<<"enter student id:";
cin>>student[size].id;

cin.ignore();

cout<<"enter student name:";
cin.getline(students[size].name,50);

cout<<"enter student cgpa:";
cin>>student[size].cgpa;

size++;

}

void displaystudent(student s){
cout<<"id:"<<s.id;
    <<",name:"<<s.name;
    <<",cgpa:"<<s.cgpa<<endl;
    }
    
void searchstudent(student*student,int size){
int searchid;
bool found = false;

cout<<"\nenter studentg id to search:";
cin>>searchid;

for(int i=0; i<size; i++){
if(student[i].id==searchid)
{
  cout<<"\nstudent found!"<<endl;
  displaystudent(student[i]);
  found=true;
  break;
  }
  }
  
if(!found)
{
cout<<"\nstudent not found!"<<endl;
}
}

int main()
{
stuident*student=null;
int size=0;
int n;

cout<<"enter number of student:";
cin>>n;

for(int i=0; i<n; i++)
{
cout<<"\nenter detail of studnt"<<i+1<<endl;
addstudent(student,size);
}

cout<<"\nstudent records"<<endl;
for(int i=0; i<size; i++)
{
displaystudent(student[i]);
}

searchstudent(student, size);

free(student);

return 0;
}

