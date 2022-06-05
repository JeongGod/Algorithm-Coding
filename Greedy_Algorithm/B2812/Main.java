package B2812;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());


        char[] nums = br.readLine().toCharArray();
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            int target = Character.getNumericValue(nums[i]);

            while (k > 0 && !stack.isEmpty() && target > stack.getLast()) {
                stack.removeLast();
                k--;
            }
            stack.addLast(target);
        }
        while (k > 0) {
            stack.removeLast();
            k--;
        }
        System.out.println(Arrays.toString(stack.toArray()).replaceAll("[^0-9]", ""));
    }
}

