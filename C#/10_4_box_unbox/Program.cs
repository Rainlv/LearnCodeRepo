using System;

namespace _10_4_box_unbox
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
        static void box()
        {
            // 拆箱：引用类型 --> 值类型
            // 装箱：值类型 --> 引用类型

            // 装箱/拆箱影响系统性能！尽量避免
            int n = 10;  // 值类型

            object o = n;  //装箱
            int nn = (int)o;  // 拆箱

            string str = "123";  // 引用类型
            n = Convert.ToInt32(str);  // 不存在拆箱操作(前后不存在继承交集)
        }
    }
}
