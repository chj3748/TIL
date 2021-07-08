// 문자열 구현 | bj 1259 팰린드롬수
// github.com/chj3748
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true){
            String number = br.readLine();
            if (number.equals("0")){
                break;
            }
            boolean flag = true;
            for (int i = 0; i < number.length()/2; i++) {
                int back_i = number.length() - 1 - i;
                if (number.charAt(i) == number.charAt(back_i)) {
                    continue;
                } else {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                bw.write("yes" + "\n");
            } else {
                bw.write("no" + "\n");
            }
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
