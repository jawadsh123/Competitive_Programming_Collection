import java.io.IOException;
import java.util.Scanner;

public class rishabh {

    public static void main(String[] args) throws Exception {
        int T;
        Scanner sc=new Scanner(System.in);
        T=sc.nextInt();
        for(int p=0;p<T;p++){
            String str=sc.next();

            char[] arr = str.toCharArray();
            int count=0;

            int i=Integer.parseInt(str);
            int j=str.length()-1;

            while(Integer.parseInt(str)!=0){
                while(arr[j]!='1'){
                    j--;
                }
                for(int x=0;x<=j;x++){
                    if(arr[x]=='0')
                       arr[x]='1';
                   else
                    arr[x]='0';
                }
            count++;
            str=String.valueOf(arr);
            
            }
        System.out.println(count);

        }
    }
}