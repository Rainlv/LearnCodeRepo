using System;
using System.Collections.Generic;
using System.Text;

namespace _10_5_多态
{
    // 抽象类、虚函数
    class Person
    {
        public virtual void Show()  // 虚方法，供子类重写
        {
            Console.WriteLine("Person");
        }
        public void Say()  // 非重写
        {
            Console.WriteLine("I am P");
        }
    }
    class Chinese : Person
    {
        public override void Show()
        {
            Console.WriteLine("Chinese");
        }
        public new void Say()
        {
            Console.WriteLine("I am C");
        }
    }    
    class English : Person
    {
        public override void Show()
        {
            Console.WriteLine("English");
        }
        public new void Say()
        {
            Console.WriteLine("I am E");
        }
    }

    public abstract class Aniaml
    {
        private int _age;
        // 抽象类的函数不一定全是抽象的(实例成员)，但抽象成员只能在抽象类中
        // 抽象成员的权限不能是private
        // 继承抽象类后要重写所有抽象成员，除非子类也是抽象类
        public int Age { get => _age; set => _age = value; }

        public abstract void Bark();
    }
    public class Dog : Aniaml
    {
        public override void Bark()
        {
            Console.WriteLine("狗在叫");
        }
    }   
    public class Cat : Aniaml
    {
        public override void Bark()
        {
            Console.WriteLine("猫在吠");
        }
    }
}
