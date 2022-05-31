package B9177;

import java.io.*;
import java.util.*;

public class Main {
    public static boolean check(String s1, String s2, String answer) {
        int lenS1 = s1.length(), lenS2 = s2.length();
        boolean[][] dp = new boolean[lenS1+1][lenS2+1];

        for (int i = 1; i < lenS1; i++) {
            dp[i][0] = s1.charAt(i-1) == answer.charAt(i-1);
        }
        for (int i = 1; i < lenS2; i++) {
            dp[0][i] = s2.charAt(i-1) == answer.charAt(i-1);
        }

        for (int i = 1; i <= lenS1; i++) {
            for (int j = 1; j <= lenS2; j++) {
                if (dp[i-1][j] && s1.charAt(i-1) == answer.charAt(i-1+j)) dp[i][j] = true;
                if (dp[i][j-1] && s2.charAt(j-1) == answer.charAt(i-1+j)) dp[i][j] = true;
            }
        }

        return dp[s1.length()][s2.length()];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            String s1 = st.nextToken();
            String s2 = st.nextToken();

            String answer = st.nextToken();

            bw.write(String.format("Data set %d:", i+1));
            if (check(s1, s2, answer)) {
                bw.write(" yes\n");
            } else {
                bw.write(" no\n");
            }
            bw.flush();
        }
    }
}

