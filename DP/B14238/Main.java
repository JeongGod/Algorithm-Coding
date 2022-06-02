package B14238;

import java.io.*;
import java.util.*;

public class Main {
    static char[] answer = new char[51];
    static int a_cnt = 0, b_cnt = 0, c_cnt = 0;
    static boolean[][][][][] dp;
    public static boolean dfs(int a, int b, int c, int target, int pp, int p) {
        if (a + b + c == target) return true;

        if (dp[a][b][c][p][pp]) return false;
        dp[a][b][c][p][pp] = true;


        if (a < a_cnt) {
            answer[a+b+c] = 'A';
            if (dfs(a + 1, b, c, target, p, 0)) return true;
        }
        if (b < b_cnt) {
            answer[a+b+c] = 'B';
            if (p != 1 && dfs(a, b + 1, c, target, p, 1)) return true;

        }
        if (c < c_cnt) {
            answer[a+b+c] = 'C';
            if (p != 2 && pp != 2 && dfs(a, b, c + 1, target, p, 2)) return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        for (char val : s.toCharArray()) {
            if (val == 'A') a_cnt++;
            else if (val == 'B') b_cnt++;
            else c_cnt++;
        }

        dp = new boolean[a_cnt + 1][b_cnt + 1][c_cnt + 1][3][3];

        if (dfs(0, 0, 0, s.length(), 0, 0)) System.out.println(Arrays.copyOfRange(answer, 0, a_cnt + b_cnt + c_cnt));
        else System.out.println(-1);
    }
}

