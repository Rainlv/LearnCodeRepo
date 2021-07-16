using System;
using System.Diagnostics;
using System.Text;

namespace _12_str
{
    class Program
    {
        static void Main(string[] args)
        {
            //reValueStr();
            strBuilder();
        }
        public static void reValueStr()
        {
            // string类型可以看做是char类型的只读数组
            // string字符串是不可变的，每次赋值都会重新在堆上开辟内存
            string s = "abcdef";
            //s[0] = "b"; // 报错，string类型是只读的
            Console.WriteLine(s[0]); // 可以访问，输出为a

            // 想要实现类似s[0] = "b"的功能，需要转化为可读可写char[]数组，再转回string类型
            char[] chs = s.ToCharArray(); // string类型的ToCharArray()方法，转化为char数组
            chs[0] = 'b';
            s = new string(chs);
            Console.WriteLine(s);
        }
        public static void strBuilder()
        {
            string s = null;
            StringBuilder sb = new StringBuilder();  // 不会重复开空间
            Stopwatch sw = new Stopwatch(); // 创建一个计时器，记录程序运行时间
            sw.Start(); // 开始计时
            for (int i = 0; i < 120000; i++)
            {
                //s += i;  // 约15s
                sb.Append(i);  // 效率远高于string，0.04s

            }
            sw.Stop(); // 结束计时
            Console.WriteLine(sw.Elapsed);
            s = sb.ToString();
        }

        public static void methods()
        {
            string a = "C#";
            string b = "c#";
            int len_a = a.Length;  // 字符串长度
            string A = a.ToLower(); // 转小写
            string B = b.ToUpper(); // 转大写

            bool flag = a.Equals(b, StringComparison.OrdinalIgnoreCase);  // Equals比较两个字符串是否相等，第二个参数控制比较方式(忽略大小写等)

            // 分割字符串
            string s = "a b c d e ... ? =,,,";
            char[] split_chs = { ' ', ',', '.', '=' }; // 要分割的字符列表
            s.Split(split_chs, StringSplitOptions.RemoveEmptyEntries); // 按分割字符列表分割字符串，第二个参数控制分割方式(删除分割字符或者设置为'')

            string name = "哈哈哈哈nmsl";
            if (name.Contains("nmsl"))  // 判断字符串是否包含某个字符或字符串
            {
                name.Replace("nmsl", "****"); // 替换字符串
                // 哈哈哈哈****
            }

            bool f = name.StartsWith("哈哈");  // true
            f = name.StartsWith("sl");  // true
            string ha = name.Substring(0, 4); // 哈哈哈哈，第二个参数不是结束索引，是截取长度

            int i = s.IndexOf('哈', 1); // 返回字符索引位置，找不到返回-1，第二个参数表示从第几位开始找
            int j = s.LastIndexOf("哈"); //  反向找

            string s_ = "    abc   ";
            string s1 = s_.Trim(); // 去两端空格
            string s2 = s_.TrimStart(); // 去前端空格
            string s3 = s_.TrimEnd(); // 去后端空格

            bool f1 = String.IsNullOrEmpty(""); // 判断字符串是否为空 

            string[] s_arr = { "真不错", "住在山里真不错", "啊" };
            string s_new = String.Join(',', s_arr); // 用,连接字符串数组
        }
    }
}
