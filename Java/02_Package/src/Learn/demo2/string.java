package Learn.demo2;

public class string {
    public static void main(String[] args) {
        // 字符串字面值赋值存在堆区的字符串常量值，底层存的是byte[]
        // 字符串new创建的在堆区，但不在常量池中
        String str1 = "abc";
        String str2 = "abc";
        char[] chars = {'a', 'b', 'c'};
        String str3 = new String(chars);

        // 引用类型==比较的是地址
        // 值类型==比较的是值
        System.out.println(str1 == str2);  // true
        System.out.println(str1 == str3);  // false
        System.out.println(str2 == str3);  // false

        System.out.println(str1.equals(str3));  // true，equals方法比较的是值
        System.out.println("ABC".equalsIgnoreCase(str1)); // true，无视大小匹配

        // 连接字符串concat
        String s = str1.concat(str2);
        System.out.println("s=" + s);

        // charof获取指定索引位置的单个字符
        char ch = "Hello".charAt(1);

        // indexof获取参数字符(串)在本来字符串第一次出现的位置
        String ss = "HelloHelloHello";
        int index = ss.indexOf("llo");

        // split分割字符串，参数默认为正则匹配
//        String[] s_list = "zzz.aaa.aaa".split(".");  切不出来，正则的.匹配所有字符
        String[] s_list = "zzz.aaa.aaa".split("\\.");
        for (String value : s_list) {
            System.out.println(value);
        }
    }
}
