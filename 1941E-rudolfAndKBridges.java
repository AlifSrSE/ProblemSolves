// Author : AlifSrSE
// Date : 2025-03-12
// Problem link : https://codeforces.com/contest/1941/problem/E


import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

    static long makeBridge(List<Long> a, int d) {
        int len = a.size();
        if (len <= d) return a.get(0) + a.get(len - 1) + 2;

        long[] dp = new long[len];
        dp[0] = a.get(0) + 1;

        Deque<long[]> dq = new ArrayDeque<>();
        dq.add(new long[]{dp[0], 0});

        for (int i = 1; i < len; i++) {
            while (!dq.isEmpty() && dq.peekFirst()[1] < i - d - 1)
                dq.pollFirst();

            dp[i] = dq.peekFirst()[0] + a.get(i) + 1;
            while (!dq.isEmpty() && dq.peekLast()[0] >= dp[i])
                dq.pollLast();
            dq.add(new long[]{dp[i], i});
        }

        return dp[len - 1];
    }

    static void solve(int t, int total, FastScanner sc, PrintWriter out) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int d = sc.nextInt();

        List<List<Long>> f = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            List<Long> row = new ArrayList<>(m);
            for (int j = 0; j < m; j++)
                row.add(sc.nextLong());
            f.add(row);
        }

        long[] b = new long[n];
        for (int i = 0; i < n; i++)
            b[i] = makeBridge(f.get(i), d);

        long sum = 0;
        long minCost = Long.MAX_VALUE;
        for (int i = 0; i < k; i++)
            sum += b[i];
        minCost = sum;

        for (int i = k; i < n; i++) {
            sum = sum - b[i - k] + b[i];
            minCost = Math.min(minCost, sum);
        }

        out.print(minCost);
        if (t != total) out.println();
    }

    public static void main(String[] args) throws IOException {
        FastScanner sc = new FastScanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        
        int t = sc.nextInt();
        for (int i = 1; i <= t; i++)
            solve(i, t, sc, out);
        
        out.flush();
    }
}