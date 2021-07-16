package Learn.demo2;

import java.util.ArrayList;
/*
*   基本类型      包装类
*    byte         Byte
*    short        Short
*    int          integer
*    long         Long
*    double       Double
*    char         Character
*    boolean      Boolean
* */

public class List {
    public static void main(String[] args) {
        // 泛型ArrayList的类型只能是引用类型，需要用包装类Integer来替代int基本类型
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        System.out.println(list.size());
        list.remove(0);
        System.out.println(list);

    }
}
