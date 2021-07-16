package 继承.抽象;

// 抽象类
public abstract class Animal_abs {
    // 定义了一个抽象的方法，在(非抽象)子类中必须重写该方法
    public abstract void eat();  // 无方法体
    // 普通方法
    public void normalMethod(){}  // 有方法体
}
