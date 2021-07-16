using System;

namespace _10_3_IsAs
{
    class Program
    {
        static void Main(string[] args)
        {
            Teacher t = new Teacher();
            // 里式转换,子类父类间转换
            Person p1 = t as Person;
            Person p2 = (Person)t;
            if (t is Person) // is 判断能否进行转换,返回bool
            {
                Console.WriteLine("yes");
            }


        }
    }

    class Person
    {

    }

    class Teacher : Person
    {

    }
}
