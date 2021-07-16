package 继承;

// java中权限缺省为protected
public class Student extends Person{  // 继承语法
    public int age = 11;

    // 子类调用父类的构造函数只能调用一次，而且必须在构造函数的第一句话
    public Student() {
        // super();  //  默认调用父类的无参构造
    }

    public Student(int age) {
        super(age);  // 调用父类的有参构造
    }

    @Override // 标志重写，不加也没事
    public void Show(){
        System.out.println("Stu的show");
    }
    @Override  // 重写的子类方法中返回值小于等于父类的方法；重写的方法权限也要大于等于父类的方法
    public String override_test(){
        return null;
    }
    public void print_age(){
        int age = 9;
        System.out.println("局部：" + age);
        System.out.println("本类：" + this.age);
        System.out.println("父类：" + super.age);  // 通过super访问父类
    }
}
