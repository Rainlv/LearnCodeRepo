using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace _17_序列化
{
    class Program
    {
        // 序列化：对象转二进制
        // 反序列化：二进制转对象
        // 用来传输数据
        static void Main(string[] args)
        {
            Person p = new Person();
            p.Age = 10;
            p.Gender = "男";
            p.Name = "张三";

            // 序列化
            //using (FileStream fsWrite = new FileStream(@"E:\Desktop\test.txt", FileMode.OpenOrCreate, FileAccess.Write))
            //{
            //    BinaryFormatter bf = new BinaryFormatter();
            //    bf.Serialize(fsWrite, p); // 不用显式调用Write来写文件
            //}

            // 反序列化
            using (FileStream fsRead = new FileStream(@"E:\Desktop\test.txt", FileMode.OpenOrCreate, FileAccess.Read))
            {
                BinaryFormatter bf = new BinaryFormatter();
                Person pe = (Person)bf.Deserialize(fsRead);
                Console.WriteLine(pe.Age);
                Console.WriteLine(pe.Gender);
                Console.WriteLine(pe.Name);
            }
        }
    }

    [Serializable]  // 标记该类可序列化
    public class Person
    {
        private string _name;
        private int _age;
        private string _gender;

        public string Name { get => _name; set => _name = value; }
        public int Age { get => _age; set => _age = value; }
        public string Gender { get => _gender; set => _gender = value; }
    }
}
