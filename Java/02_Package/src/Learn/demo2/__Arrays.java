package Learn.demo2;

import java.util.Arrays;

public class __Arrays {
    public static void main(String[] args) {
        int[] intArr = {10, 20 , 30};
        String intStr = Arrays.toString(intArr); // 转字符串
        System.out.println(intArr); // 打印的是地址
        System.out.println(intStr); // [10, 20, 30]

        String[] s_arr = {"abc", "ss", "asd"};
        Arrays.sort(s_arr);  // 排序，默认升序
        System.out.println(Arrays.toString(s_arr));
    }
}
