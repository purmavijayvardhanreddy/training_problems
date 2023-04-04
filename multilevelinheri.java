class parent{
    String s="hey";
    public void print(){
        System.out.println("im the parent of child1");
    }
}
class parentchild extends parent{
    public void print_notoveride(){
        System.out.println("hey parent, here is my chid named child 2");
    }

}
class child extends parentchild{

}
public class multilevelinheri {
    public static void main (String args[]){
        child ob=new child();

        System.out.println(ob.s);
         ob.print();
         ob.print_notoveride();
    }


}

    

