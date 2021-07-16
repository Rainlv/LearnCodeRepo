using System;
using System.Security.Cryptography;
using System.Text;

namespace _18_md5
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = "123";
            Console.WriteLine(GetMD5(s));
        }
        public static string GetMD5(string str)
        {
            // 创建一个Md5对象
            MD5 md5 = MD5.Create();
            byte[] buffer = Encoding.Default.GetBytes(str); // 转成字节数组
            byte[] MD5Buffer = md5.ComputeHash(buffer);

            string s = "";
            foreach (var item in MD5Buffer)
            {
                s += item.ToString("x2");  // 转16进制
            }
            return s;
        }
    }


}
