package B2437;


import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] chus = new int[n];
        for (int i = 0; i < n; i++) {
            chus[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(chus);

        long acc = 0;
        for (int i = 0; i < n; i++) {
            if (acc + 1 < chus[i]) break;
            acc += chus[i];
        }
        System.out.println(acc+1);
    }
}
