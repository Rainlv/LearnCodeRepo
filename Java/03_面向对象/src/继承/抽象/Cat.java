package 继承.抽象;

public class Cat extends Animal_abs {
    @Override
    public void eat() { // 重写抽象类的抽象方法
        System.out.println("猫吃鱼");
    }
}
