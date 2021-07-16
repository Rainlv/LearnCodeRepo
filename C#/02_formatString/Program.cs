using System;

namespace _02_formatString
{
    class Program
    {
        static void Main(string[] args)
        {
            #region 格式化字符串
            int age = 10;
            string name = "张三";
            double money = 1000.123456;
            Console.WriteLine("我叫{0}，我今年{1}岁了,有{2:0.00}钱", name, age, money); // 格式化字符串，{2:0.00}表示输出两位小数
            #endregion

            #region 输出原生字符串
            Console.WriteLine(@"\file\a\b\c"); // 无转义
            Console.WriteLine(@"无边落木萧萧下
不尽长江滚滚来"); // 带换行
            #endregion
        }
    }
}
