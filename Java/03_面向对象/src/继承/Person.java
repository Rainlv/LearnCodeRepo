package 继承;

public class Person {
    public int age = 10;

    public Person() {
    }

    public Person(int age) {
        this.age = age;
    }

    public void Show(){
        System.out.println("Person的show");
    }
    public Object override_test(){
        return null;
    }

}
