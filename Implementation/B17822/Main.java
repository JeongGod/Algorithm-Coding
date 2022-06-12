package B17822;

import java.io.*;
import java.util.*;

class Point {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static List<List<Integer>> board;
    static int n, m, t;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static void rotate(int line, int dist, int k) {
        if (dist == 0) {
            Collections.rotate(board.get(line), k%m);
        } else {
            Collections.rotate(board.get(line), -(k%m));
        }
    }

    static boolean check(int x) {
        return 1 <= x && x <= n;
    }
    static List<Point> bfs(int x, int y, boolean[][] visited) {
        int val = board.get(x).get(y);
        ArrayDeque<Point> dq = new ArrayDeque<>();
        dq.add(new Point(x, y));

        ArrayList<Point> result = new ArrayList<>();

        while (!dq.isEmpty()) {
            Point cur = dq.poll();

            for (int i=0; i<4; i++) {
                int nx = cur.x + dx[i], ny = (cur.y + dy[i] + m)%m;

                if (!check(nx) || visited[nx][ny] || board.get(nx).get(ny) != val) continue;

                visited[nx][ny] = true;
                Point next = new Point(nx, ny);
                dq.add(next);
                result.add(next);
            }
        }
        if (result.size() > 0) result.add(new Point(x, y));
        return result;
    }

    static List<Point> checkAdjacent(int line, boolean[][] visited) {
        List<Point> result = new ArrayList<>();
        for (int j=0; j<m; j++) {
            if (visited[line][j] || board.get(line).get(j) == -1) continue;

            visited[line][j] = true;

            result.addAll(bfs(line, j, visited));
        }
        return result;
    }

    static void removeAdjacent(List<Point> result) {
        for (Point p : result) {
            board.get(p.x).set(p.y, -1);
        }
    }

    static double getAvgBoard() {
        double result = 0;
        int cnt = 0;
        for (int i=1; i<=n; i++) {
            Iterator iter = board.get(i).iterator();
            while (iter.hasNext()) {
                int val = (int) iter.next();
                if (val == -1) continue;

                result += val;
                cnt++;
            }
        }
        return result / cnt;
    }

    static void changeBoard(double avg) {
        for (int i=1; i<=n; i++) {
            for (int j=0; j<m; j++) {
                int val = board.get(i).get(j);
                if (val == -1) continue;

                if (val < avg) board.get(i).set(j, val+1);
                else if (val > avg) board.get(i).set(j, val-1);
            }
        }
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); m = Integer.parseInt(st.nextToken()); t = Integer.parseInt(st.nextToken());

        board = new ArrayList<>();
        board.add(new ArrayList<>());

        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());

            board.add(new ArrayList<>());
            for (int j=0; j<m; j++) {
                board.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }


        boolean avgFlag = true;
        for (int i=0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()), d = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());

            for (int b=x; b<=n; b+=x) {
                rotate(b, d, k);
            }

            boolean[][] visited = new boolean[n+1][m];
            boolean flag = false;

            if (avgFlag) {
                for (int j=1; j<=n; j++) {
                    List<Point> result = checkAdjacent(j, visited);
                    if (result.size() > 0) {
                        removeAdjacent(result);
                        flag = true;
                    }
                }
                avgFlag = false;
            } else {
                for (int b=x; b<=n; b+=x) {

                    List<Point> result = checkAdjacent(b, visited);
                    if (result.size() > 0) {
                        removeAdjacent(result);
                        flag = true;
                    }
                }
            }

            if (!flag) {
                double avg = getAvgBoard();
                avgFlag = true;
                changeBoard(avg);
            }
        }

        int result = 0;
        for (int i=1; i<=n; i++) {
            result += board.get(i).stream().mapToInt(a -> a == -1 ? 0 : a).sum();
        }
        System.out.println(result);
    }
}

