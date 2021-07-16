package 静态代码块;

public class Person {
    static { // 静态代码块
        System.out.println("静态代码块");
    }

    public Person() {
        System.out.println("构造函数");
    }
}
