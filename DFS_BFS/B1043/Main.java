package B1043;

import java.io.*;
import java.util.*;

public class Main {
    static int[] tree;

    public static int find(int x) {
        if (tree[x] == x) return tree[x];
        return tree[x] = find(tree[x]);
    }

    public static void union(int x, int y) {
        tree[y] = x;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        tree = new int[n+1];
        for (int i=1; i<=n; i++) {
            tree[i] = i;
        }


        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());

        // 진실 친구
        HashSet<Integer> truePeople = new HashSet<>();
        for (int i=0; i<k; i++) {
            truePeople.add(Integer.parseInt(st.nextToken()));
        }

        // 파티
        List<List<Integer>> parties = new ArrayList<>(m);
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());

            int p = 0;

            ArrayList<Integer> tmp = new ArrayList<>();
            for (int j=0; j<num; j++) {
                int person = Integer.parseInt(st.nextToken());
                if (truePeople.contains(find(person))) p = find(person);
                tmp.add(person);
            }
            parties.add(tmp);
            if (p != 0) {
                for (int person : tmp) {
                    int px = find(person);
                    union(p, px);
                }
            }
        }
        int[] visited = new int[m];
        // 안되는 파티를 찾는다.
        while (true) {
            boolean flag = true;
            for (int i=0; i<m; i++) {
                if (visited[i] == 1) continue;
                for (int person : parties.get(i)) {
                    // 안되는 파티를 찾았다면
                    if (truePeople.contains(find(person))) {
                        for (int p : parties.get(i)) union(find(person), p);
                        visited[i] = 1;
                        flag = false;
                    }
                }
            }
            if (flag) break;
        }
        System.out.println(m - Arrays.stream(visited).sum());
    }
}

