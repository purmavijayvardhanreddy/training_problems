import java.util.*;
class data{
    Scanner scn = new Scanner(System.in);
    ArrayList arr= new ArrayList();
    
    public void print(){
    arr.add(2);
    arr.add(4);
    arr.add(6);
    arr.add(22);
    arr.add(42);
    arr.remove(0);
    System.out.println(arr);
    System.out.println(arr.get(3));

    }
    
}
public class arraylist {
    public static void main(String args[]){
        data ob = new data();
        ob.print();

    }
    
}
