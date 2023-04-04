#include<iostream>
#include<vector>
using namespace std;
// vector <int> stk;
class op{
    public:
        vector <int> stk;
        void push(int ele){
            stk.push_back(ele);
        };
        void pop(){
            if (stk.size()==0){
                cout <<"stack is empty";
            }
            else{
                stk.pop_back();
            }
        }
        void peek(){
            if (stk.size()==0){
                cout <<"stack is empty";
            }
            else{
                cout << stk[(stk.size()-1)];
            }
        }
        void display(){
            if (stk.size()==0){
                cout <<"stack is empty";
            }
            else{
                for(int i=0;i<(stk.size());i++){
                    cout << stk[i];
                }
            }
        }

};
  
int main(){
    op ob;
    ob.push(10);
    ob.push(20);
    ob.push(30);
    ob.push(40);
    ob.push(50);
    ob.push(60);
    ob.display();
    ob.pop();
}