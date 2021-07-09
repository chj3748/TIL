// 문자열 | bj 15721 번데기
// github.com/chj3748
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int T = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());

        int loop = 0;
        int people = 0;
        int val;
        boolean flag = true;
        while (flag){
            loop += 1;
            int game_len = 4 + (loop + 1) * 2;
            for (int i = 0; i < game_len; i++) {
                if (i < 4){
                    if ( i % 2 == 0){
                        val = 0;
                    } else {
                        val = 1;
                    }
                } else {
                    if ( i < 4 + (loop + 1)){
                        val = 0;
                    } else {
                        val = 1;
                    }
                }
                if ( val == target){
                    T -= 1;
                    if (T == 0){
                        flag = false;
                        bw.write(Integer.toString(people));
                        bw.flush();
                        break;
                    }
                }
                people += 1;
                people %= n;
            }

       }

    }
}
