using System;

namespace _10_8_密封类
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }

    // 密封类无法被继承，但可以继承别人
    public sealed class Person
    {

    }

    //public class Student : Person  // 无法继承自密封类
    //{

    //}
}
