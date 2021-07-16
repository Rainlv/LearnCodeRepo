using System;

namespace _10_1_OOB
{
    class Program
    {
        static void Main(string[] args)
        {
            Person p = new Person();
            p.Age = 10;

            Stu.Show();

            Init i = new Init(1, "a");
        }
    }
}
