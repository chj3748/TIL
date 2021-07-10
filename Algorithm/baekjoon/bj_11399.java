// 그리디 정렬 | bj 11399 ATM
// github.com/chj3748
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer strings = new StringTokenizer(br.readLine());
        Integer [] numbers = new Integer[n];
        while (strings.hasMoreTokens()) {
            numbers[--n] = Integer.parseInt(strings.nextToken());
        }
        Arrays.sort(numbers, Collections.reverseOrder());
        int total = 0;
        for (int num: numbers) {
            total += num * ++n;
        }
        System.out.println(total);
    }
}
