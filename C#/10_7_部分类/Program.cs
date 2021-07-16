using System;

namespace _10_7_部分类
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }

    // 相当于把一个类分开写
    public partial class Person
    {
        private int _age;

        public int Age { get => _age; set => _age = value; }
    }

    public partial class Person
    {
        public void Show()
        {
            Console.WriteLine(this.Age); 
        }
    }
}
