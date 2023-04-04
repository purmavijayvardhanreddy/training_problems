class parent{
    String s="hey";
    public void print(){
        System.out.println("im ur parent");
    }
}
class child extends parent{

}
public class singleinheri{
    public static void main (String args[]){
        child ob=new child();

        System.out.println(ob.s);

         ob.print();
    }


}