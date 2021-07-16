package Learn.demo1;

import java.util.Random;

public class random {
    public static void main(String[] args) {
        Random r = new Random();
        for (int i = 0; i < 10; i++) {
            int n = r.nextInt(10); // [0,10)区间随机数
            System.out.println(n);
        }
    }
}
