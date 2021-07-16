using System;
using System.Collections.Generic;
using System.Text;

namespace _10_1_OOB
{
    // 属性方法字段
    public class Person
    {
        // 字段
        private string _name;
        private int _age;
        private string _gender;
        private string _salary;

        // 属性(get/set)


        public string Name
        {
            get { return _name; }  // 取值调用get
            set { _name = value; } // 赋值调用set
        }

        public string Gender
        {
            get
            {
                if (_gender == "男" || _gender == "女")
                {
                    return _gender;
                }
                else
                {
                    return _gender = "男";
                }
            }
            set
            {
                if (value == "男" || value == "女")
                {
                    _gender = value;
                }
                else
                {
                    _gender = "男";
                }

            }
        }
        public int Age
        {
            get { return _age; }
            set
            {
                if (value <= 0 || value > 100)
                {
                    _age = 0;
                }
                else
                {
                    _age = value;
                }
            }
        }

        // lambda表达式，封装字段 (快捷键Ctrl+r+e)
        public string Salary { get => _salary; set => _salary = value; }

        // 方法
        public void Show()
        {
            Console.WriteLine("我叫{0},性别{1},年龄{2}", this.Name, this.Gender, this.Age);
        }
    }

    // 静态类
    public static class Stu
    {
        public static void Show()
        {
            Console.WriteLine("我是静态类");
        }
    }

    public class Init
    {
        private int a;
        private string b;
        private bool c;

        public int A { get => a; set => a = value; }
        public string B { get => b; set => b = value; }
        public bool C { get => c; set => c = value; }

        // 全参构造函数(参数最全)
        public Init(int a, string b, bool c)
        {
            A = a;
            B = b;
            C = c;
            Console.WriteLine("三个参数的构造函数");

        }
        public Init(int a, string b):this(a, b, true) // this调用全参的构造函数，避免代码冗余
        {
            // 先调用全参的构造函数，再执行本身的函数体
            Console.WriteLine("两个参数的构造函数");
        }
    }
}
