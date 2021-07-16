package 静态代码块;

// 类的静态代码块只会调用一次(自动调用)，通常用来给静态属性赋值(连接数据库等)
public class Run {
    public static void main(String[] args) {
        Person p1 = new Person();
        Person p2 = new Person();
    }
}
