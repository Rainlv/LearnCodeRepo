package Learn.demo1;

import java.util.Scanner;
// 一个包下是一个命名空间，同一个包下的文件之间不需要import
// java.lang下的包不需要import
public class scanner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  //System.in表示输入来源是从键盘输入
        int n = sc.nextInt();  // 获取输入的int(键盘输入的都是string，只是转成了int)
        System.out.println("输入的int数字是:" + n);
        String str = sc.next();
        System.out.println("输入的字符串是:" + str);
    }

}
