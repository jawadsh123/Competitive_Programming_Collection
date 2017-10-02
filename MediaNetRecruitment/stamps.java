import java.io.*;
import java.util.*;

class Codechef {

    public static void main(String[] args) throws Exception {
        // int T;
        Scanner sc=new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); 
        int t = Integer.parseInt(bf.readLine());
        for (int i=0; i<t; i++) {
            int n = Integer.parseInt(bf.readLine());
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int[] docs = new int[n];

            for (int j = 0; j<n; j++){
                docs[j] = Integer.parseInt(st.nextToken());
            }

            int p = Integer.parseInt(bf.readLine());
            boolean pFound = false;
            int pValue = 0;
            Map<Integer, Integer> map = new HashMap<Integer, Integer>();
            // int[] frequency = new int[10000000];
            int time = 0;
            int remaining = n;

            for (int j=0; j<n; j++){

                if (pFound){
                    // frequency[docs[j]] += 1;
                    
                    Integer val = map.get(docs[j]);
                    if (val != null){
                        map.put(docs[j], val+1);
                    } else {
                        map.put(docs[j], 1);
                    }

                } else {
                    // possible
                    // frequency[docs[j]-1] += 1;

                    Integer val = map.get(docs[j]-1);
                    if (val != null){
                        map.put(docs[j]-1, val+1);
                    } else {
                        map.put(docs[j]-1, 1);
                    }

                    if (docs[j]-1 == 0){
                        remaining -= 1;
                    }
                    time += 1;
                    if (j == p){
                        pFound = true;
                        pValue = docs[j]-1;
                    }
                }
            }
            // System.out.print(time);

            // for (int j = 0; j<n+1; j++){
            //     System.out.print(frequency[j]);
            // }

            int depth = 1;

            // while (pValue > 0){
            //     // System.out.println(time+" "+remaining+" "+depth+" "+frequency[depth]);
            //     time += remaining;
            //     // remaining -= frequency[depth];

            //     Integer val = map.get(depth);
            //     if (val != null){
            //         remaining -= val;
            //     }
                
            //     pValue -= 1;
            //     depth += 1;
            // }

            // System.out.print(pValue);


            for (Integer key : map.keySet()) {
                Integer val = map.get(key);
                System.out.println(key+" "+val);

                if (key > pValue){
                    time += pValue * val;
                } else {
                    time += key * val;
                }
                // System.out.println(time);
            }
            System.out.println(time);


        }

    }
}