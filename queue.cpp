#include<iostream>
#include<vector>
using namespace std;
// vector <int> stk;
class op{
    public:
        vector <int> stk;
        int rear=-1,front=-1,sz=10;
        void enqueue(int ele){
            if (front==-1)
                front=0;
            if (rear==sz){
                cout<<"overflow";
            }
            else{
            stk.push_back(ele);
            rear+=1;
            }
        };
        void dequeue(){
            if ((front==-1) or (front>rear)){
                cout <<"underflow";
            }
            else{
                front+=1;
            }
        }

        void display(){
            if (stk.size()==0){
                cout <<"stack is empty";
            }
            else{
                for(int i=front;i<=(rear);i++){
                    cout << stk[i] << endl;
                }
            }
        }

};
  
int main(){
    op ob;
    ob.enqueue(10);
    ob.enqueue(20);
    ob.enqueue(30);
    ob.enqueue(40);
    ob.enqueue(50);
    ob.enqueue(60);
    ob.display();
    ob.dequeue();
    ob.display();
}