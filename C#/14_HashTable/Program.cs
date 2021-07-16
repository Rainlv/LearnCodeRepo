using System;
using System.Collections;
using System.Collections.Generic;

namespace _14_HashTable
{
    class Program
    {
        static void Main(string[] args)
        {

        }
        static void hashTable()
        {
            // 类python字典
            Hashtable ht = new Hashtable();
            ht.Add(1, "key1");
            ht.Add(2, "key2");
            ht.Add(3, "哈");
            ht.Add(4, 123456);
            ht.Add(5, new int[] { 1, 2, 3, 5 });
            ht.Add(6, 'l');
            ht["new"] = "新来的7";  // 添加
            ht[1] = "new key"; // 替换赋值

            //var input; // 隐式类型的变量必须声明的时候就初始化

            // 遍历哈希表
            foreach (var k in ht.Keys)
            {
                Console.WriteLine(ht[k]);
            }

            // 一些方法
            bool f = ht.ContainsKey("new"); // 是否包含某个键
            int l = ht.Count; // 长度

            ht.Remove(2); // 按key移除
            ht.Clear(); // 清空表
        }

        static void dict()
        {
            Dictionary<int, string> i_s_dic = new Dictionary<int, string>();
            i_s_dic.Add(1, "第一个");
            i_s_dic.Add(2, "第2个");
            i_s_dic.Add(3, "第3个");

            foreach (KeyValuePair<int,string> item in i_s_dic)  // 键值对遍历
            {
                Console.WriteLine(item.Key);
                Console.WriteLine(item.Value);
            }
        }
    }
}
