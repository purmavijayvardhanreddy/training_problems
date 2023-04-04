import java.util.*;
class op{
    ArrayList <Integer> arr =new ArrayList<Integer>();
    public void push(int ele){
        arr.add(ele);
    }
    public void pop(){
        if (arr.size()==0){
            System.out.println("stack is empty");

        }
        else{
            arr.remove((arr.size()-1));
        }
    }
    public void peek(){
        if (arr.size()==0){
            System.out.println("stack is empty");

        }
        else{
            System.out.println(arr.get(arr.size()-1));
        }
        
    }
    public void isEmpty(){
        if (arr.size()==0){
            System.out.println("stack is empty");

        }
        else{
            System.out.println("stack is not empty");
        }
        
    }
    public void display(){
        for(int i=0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }

    }

}

public class stack {
    public static void main(String args[]){

        op ob = new op();
        ob.isEmpty();
        ob.push(10);
        ob.push(20);
        ob.display();
        ob.push(1);
        ob.peek();
        ob.pop();
        ob.push(33);
        ob.push(53);
        ob.push(34);
        ob.push(234);
        ob.display();

    
    }
    
}
