using System;

namespace _10_5_多态
{
    class Program
    {
        static void Main(string[] args)
        {
            Chinese c = new Chinese();
            English e = new English();
            Person p = new Person();
            Person[] p_arr = { c, e, p };
            foreach (var item in p_arr)
            {
                item.Say();
                item.Show();
                /*
                    I am P
                    Chinese
                    I am P
                    English
                    I am P
                    Person
                 */
            }

            //Aniaml a = new Aniaml();  // 抽象类无法实例化
            Dog d = new Dog();
            Cat cat = new Cat();
            d.Bark();
            cat.Bark();
        }
    }
}
