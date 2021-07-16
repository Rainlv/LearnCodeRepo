using System;
using System.IO;

namespace _15_Path
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = @"E:\Desktop\AE\需求规格说明书.doc";

            string fileName = Path.GetFileName(path);   // 取文件名
            string fileNameWithoutExt = Path.GetFileNameWithoutExtension(path); // 取不带扩展名的文件名
            string extension = Path.GetExtension(path);  // 取扩展名
            string dirName = Path.GetDirectoryName(path);   // 取文件夹名
            string fullPath = Path.GetFullPath(path);   // 取全路径
            string combinePath = Path.Combine(@"C:\aa", "a.txt");  // 连接路径(os.path.join)
            Console.WriteLine(fileName);
            Console.WriteLine(fileNameWithoutExt);
            Console.WriteLine(extension);
            Console.WriteLine(dirName);
            Console.WriteLine(fullPath);
            Console.WriteLine(combinePath);

        }
    }
}
