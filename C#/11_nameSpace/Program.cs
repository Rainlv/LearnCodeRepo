using System;
using _10_1_OOB;

namespace _11_nameSpace
{
    class Program
    {
        /* 引用
         *      右键项目下的依赖项，添加项目引用
         *      引用命名空间(using xxx;)
         */
        static void Main(string[] args)
        {
            Init i = new Init(1, "a"); // 引用了_10_1_OOB中的类
        }
    }
}
