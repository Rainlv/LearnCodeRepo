using System;
using System.IO;
using System.Text;

namespace _16_File
{
    class Program
    {
        static void Main(string[] args)
        {
            //mk_del_copy();
            //readFile();   // 乱码
            //writeFile();
            //FileStream_r();
            //FileStream_w();
            //Cope_file();
            //Stream_r();
            Stream_w();
        }
        static void mk_del_copy()
        {
            File.Create(@"E:\Desktop\new.txt");  // 创建文件
            File.Delete(@"E:\Desktop\new.txt");  // 删除文件
            File.Copy(@"E:\Desktop\code.txt", @"E:\Desktop\new.txt");  // 复制文件,第二个参数的文件必须不存在，否则报错
        }
        static void readFile()
        {
            // ReadAllBytes
            //byte[] buffer = File.ReadAllBytes(@"E:\Desktop\test.txt");
            ////string s = Encoding.GetEncoding("iso-8859-1").GetString(buffer);
            //string s = Encoding.Default.GetString(buffer);
            //Console.WriteLine(s);

            // ReadAllLines
            //string[] contents = File.ReadAllLines(@"E:\Desktop\test.txt", Encoding.Default);
            //foreach (var item in contents)
            //{
            //    Console.WriteLine(item);
            //}

            string str = File.ReadAllText(@"E:\Desktop\test.txt", Encoding.Default);
            Console.WriteLine(str);

        }
        static void writeFile()
        {
            // WriteAllBytes
            //byte[] buffer = Encoding.Default.GetBytes("测试文字");
            //File.WriteAllBytes(@"E:\Desktop\test.txt", buffer);

            // 写入
            //File.WriteAllText(@"E:\Desktop\test.txt", "哈哈哈aaa");
            File.WriteAllLines(@"E:\Desktop\test.txt", new string[] { "aha", "dasdas" }); 

            // 追加
            File.AppendAllText(@"E:\Desktop\test.txt", "追加");

        }
        static void FileStream_r()
        {
            // 文件路径，打开方式，读写方式
            FileStream fsRead = new FileStream(@"E:\Desktop\updata_req.txt", FileMode.OpenOrCreate, FileAccess.Read);
            byte[] buffer = new byte[1024 * 1024 * 5];
            // r 是本次读取的有效字节数
            int r = fsRead.Read(buffer, 0, buffer.Length); // 存储数组，从数组第几位开始存放，每次读取长度
            string s = Encoding.Default.GetString(buffer, 0, r); // 仅解码有效部分的字符(5M可能有多余的，会用空白填充)
            fsRead.Close();  // 关闭流
            fsRead.Dispose();  // 释放流占用的资源
            Console.WriteLine(s);


        }
        static void FileStream_w()
        {
            // using相当于python中的with open
            using (FileStream fsWrite = new FileStream(@"E:\Desktop\updata_req.txt", FileMode.OpenOrCreate, FileAccess.Write))
            {
                string s = "写点试试";
                byte[] buffer = Encoding.Default.GetBytes(s);
                fsWrite.Write(buffer, 0, buffer.Length);
                // 不用手动释放资源
            }
        }
        static void Cope_file()
        {
            using (FileStream fsRead = new FileStream(@"E:\Desktop\updata_req.txt", FileMode.OpenOrCreate, FileAccess.Read))
            {
                using (FileStream fsWrite = new FileStream(@"E:\Desktop\updata_req_copy.txt", FileMode.OpenOrCreate, FileAccess.Write))
                {
                    byte[] buffer = new byte[1024 * 1024 * 5];
                    while (true)
                    {
                        int r = fsRead.Read(buffer, 0, buffer.Length);
                        if (r == 0)
                        {
                            break;
                        }
                        fsWrite.Write(buffer, 0, r);
                    }
                }
            }

           

        }
        static void Stream_r()
        {
            using (StreamReader s_r = new StreamReader(@"E:\Desktop\updata_req.txt", Encoding.Default)) // 第二个参数控制编码
            {
                while (!s_r.EndOfStream)
                {
                    Console.WriteLine(s_r.ReadLine());
                }
            }
        }

        static void Stream_w()
        {
            using (StreamWriter s_w = new StreamWriter(@"E:\Desktop\updata_req_new.txt", true, Encoding.Default))
            {
                s_w.Write("覆盖否");
            }
        }
    }
}
