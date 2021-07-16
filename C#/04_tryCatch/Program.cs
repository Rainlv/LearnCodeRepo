using System;

namespace _04_tryCatch
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = 0;
            bool flag = false;
            Console.WriteLine("输入一个数字:");

            // 选中之后ctrl+k+s，快捷#region
            #region try-catch
            try
            {
                num = Convert.ToInt32(Console.ReadLine());
                flag = true;

            }
            catch
            {
                Console.WriteLine("\n输入内容非数字");
            } 
            #endregion
            if (flag)
            {
                Console.WriteLine(num * 2);
            }


        }
    }
}
