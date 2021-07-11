// 누적합 | bj 2167 2차원 배열의 합
// github.com/chj3748
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n, m, t;
        int[][] acc_sum;
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        acc_sum = new int[n + 1][m + 1];
        for (int i = 0; i < n + 1; i++) {
            if (i > 0){
                input = br.readLine().split(" ");
            }
            for (int j = 0; j < m + 1; j++) {
                if (i == 0 || j == 0){
                    acc_sum[i][j] = 0;
                } else {
                    acc_sum[i][j] = Integer.parseInt(input[j - 1]) + acc_sum[i - 1][j] + acc_sum[i][j - 1] - acc_sum[i - 1][j - 1];
                }
            }
        }

        t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            input = br.readLine().split(" ");
            int x1 = Integer.parseInt(input[0]);
            int y1 = Integer.parseInt(input[1]);
            int x2 = Integer.parseInt(input[2]);
            int y2 = Integer.parseInt(input[3]);
            int suf_sum = acc_sum[x2][y2] - acc_sum[x1 - 1][y2] - acc_sum[x2][y1 - 1] + acc_sum[x1 - 1][y1 - 1];
            bw.write(Integer.toString(suf_sum) + "\n");
            bw.flush();
        }
    }
}
