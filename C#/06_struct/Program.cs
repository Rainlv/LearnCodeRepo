using System;

namespace _06_struct
{
    // 声明结构体，public可省略（默认为public）
    public struct Person
    {
        public string _name;  // 字段，命名规范在前加‘_’，需要声明公有权限
        public int _age;
        public Gender _gender;

    }

    public enum Gender
    {
        male,
        female
    }
    class Program
    {
        static void Main(string[] args)
        {
            // 使用结构体
            Person p;
            p._age = 10;
            p._name = "zs";
            p._gender = Gender.male;
        }
    }
}
