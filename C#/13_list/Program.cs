using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace _13_list
{
    class Program
    {
        static void Main(string[] args)
        {
            array_list();
        }

        static void array_list()
        {
            ArrayList list = new ArrayList();
            // 添加单个元素
            list.Add("hah");
            list.Add(1);
            list.Add(true);
            list.Add(new int[] { 1, 2, 3, 4 }); // 添加数组
            list.Clear(); // 清空list
            // 添加集合(想当于把集合元素添加进来，而不是一个集合对象)
            list.AddRange(new int[] { 1, 2, 33, 4 }); // 添加集合内的元素，而不是集合本身

            list.Remove(33); // 按值删除元素
            list.RemoveAt(0); // 按索引删除元素
            list.RemoveRange(0, 3); // 按下标范围删元素
            list.Sort(); // 升序排列(前提是同类型？)
            list.Reverse(); // 反转数组
            list.Insert(1, "插入的"); // 指定位置插入元素
            list.InsertRange(2, new string[] { "张三", "李思" });  // 指定位置插入集合(以元素形式)

            bool f = list.Contains("张三"); // 数组是否包含某个值

            int len = list.Count; // 数组长度
            int l = list.Capacity; // 数组可包含最大长度
            /* 可变长度数组实现原理：
                    每次数组实际长度到达数组最大长度，向内存申请多一倍的空间*/
        }

        // 泛型数组(常用)
        static void list()
        {
            List<int> i_list = new List<int>();  // 存int的List
            i_list.Add(1);
            i_list.Add(2);
            i_list.Add(3);
            i_list.AddRange(new int[] { 1, 2, 3, 45 });

            // 转数组
            int[] i_arr = i_list.ToArray();

            char[] chs = new char[] { 'a', 'b', 'v' };
            List<char> chs_list = chs.ToList(); // 数组转list

        }

    }
}
