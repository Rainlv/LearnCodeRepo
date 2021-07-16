using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ae
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Lines = null;

            const int c1_price = 5;
            const int c2_price = 3;
            const double c3_price = 1.0 / 3;

            string[] res = new string[2];
            string result = "";

            int chicken_num = 0;
            double money = 0.00;

            bool flag = false;

            try
            {
                // 获取参数
                chicken_num = int.Parse(chiken_num.Text);
                money = double.Parse(money_num.Text);
                flag = true;
            }
            catch {
                MessageBox.Show("非法输入！输入非数字或输入鸡数非整数");
            }


            // c1-->5,c2-->3,c3-->1/3
            int c1 = 0;
            int c2 = 0;
            int c3 = 0;
            int loop1 = chicken_num / 5;
            int loop2 = chicken_num / 3;
            int tick = 0;

            if (flag)
            {          
                for (c1 = 0; c1 < loop1; c1++)
                {
                    for (c2 = 0; c2 < loop2; c2++)
                    {
                        c3 = chicken_num - c1 - c2;
                        double rest_money = money - c1 * c1_price - c2 * c2_price;
                        tick += 1;
                        if (c3*c3_price == rest_money)
                        {
                            result += "公鸡" + c1 + "\t" + "母鸡" + c2 + "\t" + "小鸡" + c3 + "\n";
                        }
                    }
                }

                if (result == "")
                {
                    MessageBox.Show("遍历无结果，钱数无法被全部消耗完或买不到对应数量的鸡！");
                }
                else
                {
                    result += "==================";
                    res[0] = result;
                    res[1] = "迭代次数为" + tick.ToString();
                    richTextBox1.Lines = res;
                }
            }
        }

        private void label1_Click_1(object sender, EventArgs e)
        {

        }
    }
}
