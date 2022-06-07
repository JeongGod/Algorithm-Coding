package B25239;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static int hourTomin(int hour, int minute) {
        return hour * 60 + minute;
    }

    public static void changeBoard(double sec, int[] board) {

        if (0 < sec && sec < 120) board[0] = 0;
        else if (120 < sec && sec < 240) board[1] = 0;
        else if (240 < sec && sec < 360) board[2] = 0;
        else if (360 < sec && sec < 480) board[3] = 0;
        else if (480 < sec && sec < 600) board[4] = 0;
        else if (600 < sec && sec < 720) board[5] = 0;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        List<Integer> t = Arrays.stream(br.readLine().split(":")).map(Integer::parseInt).collect(Collectors.toList());
        int secs = hourTomin(t.get(0), t.get(1));

        st = new StringTokenizer(br.readLine());
        int[] board = new int[6];
        for (int i=0; i<6; i++) board[i] = Integer.parseInt(st.nextToken());

        int n = Integer.parseInt(br.readLine());

        for (int i=0 ;i<n; i++) {
            String et = br.readLine();
            String[] tmp = et.split(" ");

            if (tmp[1].equals("^")) {
                changeBoard(secs, board);
            } else {
                if (tmp[1].charAt(2) == 'M') secs += hourTomin(0, Integer.parseInt(tmp[1].substring(0, 2)));
                else secs += hourTomin(tmp[1].charAt(0) - '0', 0);

                if (secs >= 720) secs -= 720;
            }
        }
        int result = IntStream.of(board).sum();
        if (result > 100) result = 100;
        System.out.println(result);
    }
}


