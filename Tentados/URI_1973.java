import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.IntStream;

public class Principal {
    public static void main(String[] args) {
        Scanner e = new Scanner(System.in);
        int n, i = 0;
        Set<Integer> yRoub = new HashSet<>();
        
        n = e.nextInt();
        e = new Scanner(System.in);
        String[] seq = e.nextLine().split(" ");
        int[] star = new int[seq.length];
        
        int j = 0;
        for(String s: seq){
            star[j] =  Integer.parseInt(s);
            j++;
        }
        while(true){
            if(n==0 || i>=n || i<0) break;
            yRoub.add(i);
            if(star[i]==0) break;
            star[i]--;
            if(star[i]%2==0){
                i++;
            }else{
                i--;
            }
        }
        System.out.println(yRoub.size()+" "+IntStream.of(star).sum());
    }
}
