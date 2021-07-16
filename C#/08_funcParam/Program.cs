using System;

namespace _08_funcParam
{
    class Program
    {
        static void Main(string[] args)
        {
            // out 使用
            Console.WriteLine("-------------out-------------");
            int[] arr = { -1, 0, 1, 2, 3, 4, 5 };
            int sum, max, min;
            double aver;
            calc(arr, out sum, out max, out min, out aver);
            Console.WriteLine(sum);
            Console.WriteLine(max);
            Console.WriteLine(min);
            Console.WriteLine(aver);
            Console.WriteLine("------------- end out -------------");
            Console.WriteLine("------------- ref -------------");
            double num1 = 5.2, num2 = 3.3, res = 0;
            sumFunc(ref res, num1, num2);
            Console.WriteLine(res); // 8.5
            Console.WriteLine("------------- end ref -------------");

            Console.WriteLine("------------- params -------------");
            double n1 = 1, n2 = 2, n3 = 3;
            // 要求输入的是double[]数组，加上params会把输入的多个同类型的值包装成数组。
            // 放在参数列表的最后一个！只能有一个
            double add_res = addFunc(n1, n2, n3);  
            Console.WriteLine(add_res);
            Console.WriteLine("------------- end params -------------");
        }

        // out 参数，从函数内部传出值(可以多个,可以不同类型)
        #region out参数的使用
        static void calc(int[] arr, out int sum, out int max, out int min, out double aver)
        {
            sum = 0;
            max = int.MinValue; // int类型的最小值
            min = int.MaxValue;
            aver = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                sum += arr[i];
                max = max > arr[i] ? max : arr[i];
                min = min < arr[i] ? min : arr[i];
            }
            aver = (double)sum / arr.Length;
        }
        #endregion
        // ref 参数, 引用一个函数外部的值，函数内部直接修改，不需要return传出。就是C++的引用
        #region ref参数的使用
        static void sumFunc(ref double res, double num1, double num2)
        {
            res = num1 + num2;
        }
        #endregion
        // params 参数，零散的输入装包成数组
        public static double addFunc(params double[] arr)
        {
            double res=0;
            for(int i = 0; i < arr.Length; i++)
            {
                res += arr[i];
            }
            return res;
        }
    }

}
