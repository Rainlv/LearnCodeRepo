using System;
using System.Collections.Generic;
using System.Text;

namespace _10_2_extend
{
    class Person
    {
        private string name;
        private int age;
        private string _gender;

        public string Name { get => name; set => name = value; }
        public int Age { get => age; set => age = value; }
        public string Gender { get => _gender; set => _gender = value; }

        public Person()
        {
            Console.WriteLine("这是父类的无参构造函数");
        }
        public Person(string name, int age, string gender)
        {
            this.Name = name;
            this.Age = age;
            this.Gender = gender;
        }

        public void Show()
        {
            Console.WriteLine("父类的show");
        }
    }

    class Student : Person  // 继承
    {
        private int socre;

        // 子类实例化对象会先调用父类的构造函数，再调用子类的对应构造函数
        public Student()  // 不写:base默认调用父类的无参构造
        {
            Console.WriteLine("这是子类的无参构造函数");
        }
        public Student(string name, int age, string gender, int score) : base(name, age, gender)  // 调用父类的有参构造函数
        {
            // 减少重复初始化属性的冗余
            this.Socre = socre;
        }

        public new void Show()  // 使用new关键字来重写父类的同名函数
        {
            Console.WriteLine("这是子类的show");
        }

        public int Socre { get => socre; set => socre = value; }
    }

}
