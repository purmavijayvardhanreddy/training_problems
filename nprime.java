import java.util.*;
public class nprime {
    static int a=20;
    public static void main( String[] args){
        System.out.println(a);
        Scanner sn = new Scanner(System.in);
        int n;
        n=sn.nextInt();
        int c=0,i=2;
        // int arr[]=new int[20];
        while(c<n){
            int f=0;
            for(int j=2;j<((int)i/2)+1;j++){
                if (i%j==0){
                    f=1;
                }
            }
            if (f==0){
            System.out.print(i+" ");
            c+=1;
            }
            i+=1;
        }
        

    }
    
}
