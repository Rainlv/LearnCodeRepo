using System;

namespace _10_9_接口
{
    class Program
    {
        static void Main(string[] args)
        {
            IFlyable bird = new Bird();
            bird.Fly();
            bird.Turn();
        }
    }
    public class Animal
    {

    }

    public class Bird : Animal, IFlyable  // 子类继承要先继承基类，再写接口
    {
        public int Name { get; set; }

        public void Fly()
        {
            Console.WriteLine("我是类的飞");
        }

        public void Turn()
        {
            Console.WriteLine("拐弯咯");

        }

        void IFlyable.Fly()  // 显式实现接口的Fly，解决类内函数重名问题
        {
            Console.WriteLine("我是接口的飞");
        }
    }
    public interface IFlyable
    {
        // 接口只能包含方法和属性，默认为public，不能加访问修饰符(vs2019可以加)
        // 方法不能写方法体(vs2019可以写，不知道咋用)，继承接口的类必须实现接口的所有方法
        // 
        void Fly();  // 方法
        int Name  // 属性(自动属性,会在编译阶段生成一个字段)
        {
            get;
            set;
        }

        void Turn();

    }

    #region 接口继承
    public interface M1
    {
        void M1_func();
    }
    public interface M2
    {
        void M2_func();
    }
    public interface M3
    {
        void M3_func();
    }
    public interface SuperM : M1, M2, M3
    {
        void SuperM();
    }

    //public interface M0 : Bird // 接口不能继承类
    //{

    //}
    public class C1 : SuperM
    {
        public void M1_func()
        {
        }
        public void M2_func()
        {
        }
        public void M3_func()
        {
        }
        public void SuperM()
        {
        }
    }
    #endregion
}
