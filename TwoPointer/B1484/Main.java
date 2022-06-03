package B1484;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int g = Integer.parseInt(br.readLine());

        ArrayList<Integer> answer = new ArrayList<>();

        int left = 1, right = 2;
        while (right <= 100000) {
            int result = (int) (Math.pow(right, 2) - Math.pow(left, 2));
            if (result == g) answer.add(right);

            if (result <= g) right++;
            else left++;
        }

        if (answer.isEmpty()) System.out.println(-1);
        else {
            for (int x : answer) {
                System.out.println(x);
            }
        }
    }
}

