using System;

namespace _05_enum
{
    // 枚举不要写在main方法里，视使用情况写在命名空间或者类中

    #region 枚举类型声明
    // 声明一个枚举
    public enum Gender  // public表示使用权限，不写默认为public
    {
        // 声明的两个值，即可选的值
        male,
        female
    } 
    #endregion
    enum Seasons
    {
        Spring,
        Summer,
        Autumn,
        Winter
    }
    class Program
    {
        static void Main(string[] args)
        {
            #region 枚举类型使用
            // 变量类型 变量名=值;
            int n = 10;
            Gender sex = Gender.female;  // Gender即是自定义的变量类型
            #endregion

            #region 枚举类型转int
            // 枚举类型变量默认可以跟int类型相互转换
            // 变量从上到下默认从0开始，不过可以在声明中自己指定
            Seasons seasons = Seasons.Autumn;
            int num = (int)seasons;
            Console.WriteLine(num); // 2
            Console.WriteLine((int)Seasons.Spring); // 0
            Console.WriteLine((int)Seasons.Summer); // 1
            Console.WriteLine((int)Seasons.Winter); // 3
            #endregion
            #region int转枚举类型
            int s = 2;
            Seasons seasons1 = (Seasons)s;
            Console.WriteLine(seasons1); // Autumn，在枚举范围内的，输出对应的值
            Console.WriteLine((Seasons)8); // 8,遇到不在枚举范围内的直接输出原值
            #endregion

            #region 枚举转String
            string s1 = Seasons.Spring.ToString();
            Console.WriteLine(s1); // Spring
            #endregion
            #region String转枚举
            Console.WriteLine("--------String转枚举------------");
            string ss = "0";
            // Enum.Parse(枚举类型, 字符串)
            Seasons seasons2 = (Seasons)Enum.Parse(typeof(Seasons), ss); // Spring,范围内的找对应值
            Seasons seasons3 = (Seasons)Enum.Parse(typeof(Seasons), "8"); // 8，范围外的数字直接输出
            Seasons seasons4 = (Seasons)Enum.Parse(typeof(Seasons), "Spring"); // Spring，范围外的数字直接输出
            Seasons seasons5 = (Seasons)Enum.Parse(typeof(Seasons), "Springssss"); // 报错
            Console.WriteLine(seasons2);
            Console.WriteLine(seasons3);
            Console.WriteLine(seasons4);
            #endregion
        }
    }
}
