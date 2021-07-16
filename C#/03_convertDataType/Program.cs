using System;

namespace _03_convertDataType
{
    class Program
    {
        static void Main(string[] args)
        {
            // 兼容的类型，如int和double可以进行隐式类型转换和强制类型转换
            int a = 10;
            double b = a; // 隐式
            double c = (double)a; // 强制
            int d = (int)c;
            #region Convert
            // 不兼容的类型，如string和int，需要使用Convert进行类型转换
            string str_int = "10";
            string str_double = "132.123";
            int num = Convert.ToInt32(str_int);  // str --> int
            double num_double = Convert.ToDouble(str_double); // str --> double
            string from_num = Convert.ToString(num); // int --> str
                // 转float是ToSingle
            Console.WriteLine(num);
            Console.WriteLine(num_double);

            // dynamic类似弱类型的数据类型
            dynamic myValue = 100;
            Console.WriteLine(myValue);
            myValue = "It's OK";
            Console.WriteLine(myValue);
            #endregion
            #region Parse
            // Convert本质就是调用Parse
            int t1 = int.Parse("123");
            double t2 = double.Parse("123");
            float t3 = float.Parse("123");
            //int t1 = int.Parse("123abc");  报错
            #endregion
            #region TryParse
            // 转化失败不会抛出异常
            // 参数1：类型转换的字符串；参数2：转换完成赋值的变量；返回值：转换结果bool类型
            int num_1 = 0;
            bool res = int.TryParse("123", out num_1);  // 对"123"转int，成功，把转换的值即123赋值给num_1，返回True；失败，返回False
            Console.WriteLine(res);
            Console.WriteLine(num_1);
            #endregion
        }
    }
}
