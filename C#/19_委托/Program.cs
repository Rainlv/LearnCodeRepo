using System;

namespace _19_委托
{
    class Program
    {
        // 委托就是一个函数指针，把函数作为参数传入

        // 声明一个委托
        public delegate void Del_Show(string name);
        public delegate void Del_Test();
        // 声明一个泛型委托
        public delegate bool Del_Compare<T>(T t1, T t2);

        static void Main(string[] args)
        {
            // 1. 创建委托对象并调用
            //Del_Show del = I_show;
            // Del_Show del = new Del_Show(I_show); 与上面等价
            //del("张三");

            // 2. 函数作为参数调用委托
            //Test("张三", I_show);

            // 3. 匿名函数作为参数
            //Test("无名", delegate(string name)
            //{
            //    Console.WriteLine(name);
            //});

            // 4. lambda表达式做参数
            //Test("无名", (string name) => { Console.WriteLine(name);});

            // 5. 泛型委托(函数模板)
            //int[] num_arr = { 1, 23, 4, 6 };
            //string[] str_arr = { "abc", "adas", "sdasdasdas" };

            //int m = GetMax<int>(num_arr, (int t1, int t2) =>
            //{
            //    return t1 > t2;
            //});
            //string s = GetMax<string>(str_arr, (string s1, string s2) =>
            //{
            //    return s1.Length > s2.Length;
            //});
            //Console.WriteLine(m);
            //Console.WriteLine(s);

            // 6. 多播委托
            Del_Test del = T1;
            del += T2;
            del += T3;
            del += T4;
            del();
            del -= T1;
            del();
        }

        public static void Test(string name, Del_Show D_Show)
        {
            D_Show(name);
        }
        public static void I_show(string name)
        {
            Console.WriteLine("我show");
        }
        public static void Y_show(string name)
        {
            Console.WriteLine("你show");
        }

        public static T GetMax<T>(T[] nums, Del_Compare<T> del_c)
        {
            T max = nums[0];
            foreach (T item in nums)
            {
                if (del_c(item, max))
                {
                    max = item;
                }
            }
            return max;
        }

        public static void T1()
        {
            Console.WriteLine("T1");
        }
        public static void T2()
        {
            Console.WriteLine("T2");
        }
        public static void T3()
        {
            Console.WriteLine("T3");
        }
        public static void T4()
        {
            Console.WriteLine("T4");
        }
    }
}
