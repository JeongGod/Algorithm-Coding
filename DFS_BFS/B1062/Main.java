package B1062;

import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;
    static boolean[] visited;
    static int[] words;
    public static boolean check(int s, int study) {
        return (s & study) == s;
    }
    public static void dfs(int start, int depth, int target, int study) {
        if (answer == words.length) return;
        if (depth == target) {
            int result = 0;
            // check
            for (int s : words) {
                if (check(s, study)) result++;
            }
            answer = Math.max(answer, result);
            return;
        }

        for (int i = start; i < 26; i++) {
            if (visited[i]) continue;
            dfs(i+1, depth + 1, target, study | (1 << i));
        }
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());

        if (m < 5) {
            System.out.println(0);
            return;
        }

        visited = new boolean[27];
        visited[0] = true; visited['c' - 'a'] = true; visited['i' - 'a'] = true; visited['t' - 'a'] = true; visited['n' - 'a'] = true;
        int first = 0;
        first |= 1; first |= 1 << ('c' - 'a'); first |= 1 << ('i' - 'a'); first |= 1 << ('t' - 'a'); first |= 1 << ('n' - 'a');

        words = new int[n];
        for (int i=0; i<n; i++) {
            String val = br.readLine();
            int tmp = 0;
            for (Character c : val.substring(4, val.length()-4).toCharArray()) {
                tmp |= 1 << (c - 'a');
            }
            words[i] = tmp;
        }

        // 가능한 알파벳으로 가능한지 판단
        dfs(0,5, m, first);
        System.out.println(answer);
    }
}

