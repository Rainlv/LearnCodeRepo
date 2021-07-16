using System;

namespace _09_GameProj
{
    class Program
    {
        static int[] Map = new int[100];  // 默认值全为0
        static int[] playerPos = new int[2];
        static string[] playerName = GetPlayerName();
        static bool[] Flags = new bool[2];  // 默认值全为false

        static void Main(string[] args)
        {
            GameHead();

            Console.Clear(); //清屏
            GameHead();
            Console.WriteLine("{0}的棋子用A表示", playerName[0]);
            Console.WriteLine("{0}的棋子用B表示", playerName[1]);
            Console.WriteLine();

            InitMapArr();
            DrawMap();

            GameLogic();
        }
        public static void GameHead()
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("***************************");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("***************************");
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("****1009版飞行棋小游戏*****");
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("***************************");
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("***************************");
            Console.ForegroundColor = ConsoleColor.White;
        }
        public static void InitMapArr()
        {
            int[] luckyTurn = { 6, 23, 40, 55, 69, 83 };
            int[] landMine = { 5, 13, 17, 33, 38, 50, 64, 80, 94 };
            int[] parse = { 9, 27, 60, 93 };
            int[] jumpTunnel = { 20, 25, 45, 63, 72, 88, 90 };
            for (int i = 0; i < luckyTurn.Length; i++)
            {
                Map[luckyTurn[i]] = 1; // 幸运转盘
            }            
            for (int i = 0; i < landMine.Length; i++)
            {
                Map[landMine[i]] = 2; // 地雷
            }            
            for (int i = 0; i < parse.Length; i++)
            {
                Map[parse[i]] = 3; // 暂停
            }
            for (int i = 0; i < jumpTunnel.Length; i++)
            {
                Map[jumpTunnel[i]] = 4; // 时空隧道
            }
        }
        public static void DrawMap()
        {
            Console.WriteLine("图例:幸运轮盘:◎   地雷:☆    暂停:▲    时空隧道:卍");

            #region 第一横行
            for (int i = 0; i <= 29; i++)
            {
                Console.Write(DrawMapStr(i));
            }
            #endregion
            #region 第一竖列
            for (int j = 30; j < 35; j++)
            {
                Console.WriteLine();
                for (int i = 0; i <= 28; i++)
                {
                    Console.Write("  ");
                }
                Console.Write(DrawMapStr(j));
            }
            #endregion
            #region 第二横行
            Console.WriteLine();
            for (int i = 64; i >= 35; i--)
            {
                Console.Write(DrawMapStr(i));
            }
            Console.WriteLine();
            #endregion
            #region 第二竖列
            for (int i = 65; i < 69; i++)
            {
                Console.WriteLine(DrawMapStr(i));
            }
            #endregion
            #region 第三横行
            for (int i = 70; i <= 99; i++)
            {
                Console.Write(DrawMapStr(i));
            }
            #endregion

            Console.WriteLine();

        }
        public static string DrawMapStr(int i)
        {
            string str = "";
            if (playerPos[0] == playerPos[1] && playerPos[0] == i)
            {
                str = "<>";
            }
            else if (playerPos[0] == i)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                str = "Ａ";
            }
            else if (playerPos[1] == i)
            {
                Console.ForegroundColor = ConsoleColor.Blue;
                str = "Ｂ";
            }
            else
            {
                switch (Map[i])
                {
                    case 0:
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        str = "□";
                        break;
                    case 1:
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        str = "◎";
                        break;
                    case 2:
                        Console.ForegroundColor = ConsoleColor.DarkGreen;
                        str = "☆";
                        break;
                    case 3:
                        Console.ForegroundColor = ConsoleColor.DarkGray;
                        str = "▲";
                        break;
                    case 4:
                        Console.ForegroundColor = ConsoleColor.DarkMagenta;
                        str = "卍";
                        break;
                }
            }// end else
            return str;
        }
        public static string[] GetPlayerName()
        {
            string[] playerName = new string[2];
            Console.WriteLine("请输入玩家A的昵称");
            playerName[0] = Console.ReadLine();
            while (playerName[0] == "")
            {
                Console.WriteLine("玩家的昵称不能为空，请重新输入");
                playerName[0] = Console.ReadLine();
            }

            Console.WriteLine("请输入玩家B的昵称");
            playerName[1] = Console.ReadLine();
            while (playerName[1] == ""||playerName[1] == playerName[0])
            {
                if (playerName[1] == "")
                {
                    Console.WriteLine("玩家的昵称不能为空，请重新输入");
                    playerName[1] = Console.ReadLine();
                }
                else
                {
                    Console.WriteLine("玩家AB昵称不能相同，请重新输入");
                    playerName[1] = Console.ReadLine();

                }
            }
            return playerName;
        }
        public static void GameLogic()
        {
            while (playerPos[0] < 99 && playerPos[1] < 99)
            {
                if (Flags[0] == false)
                {
                    PlayGame(0);
                }
                else
                {
                    Flags[0] = false;
                }
                if (Flags[1] == false)
                {
                    PlayGame(1);
                }
                else
                {
                    Flags[1] = false;
                }
                if (playerPos[0] >= 99)
                {
                    Console.WriteLine("玩家{0}胜利！！！！！！", playerName[0]);
                    break;
                }
                if (playerPos[1]>=99)
                {
                    Console.WriteLine("玩家{0}胜利！！！！！！", playerName[1]);
                    break;
                }
            }
        }// end func
        public static void PlayGame(int playerNum)
        {
            // 掷骰子
            Random r = new Random();
            int rNum = r.Next(0, 7);
            Console.WriteLine("{0}按任意键开始掷骰子", playerName[playerNum]);
            Console.ReadKey(true); // 重载，传入参数表示输入值不显示在控制台
            Console.WriteLine("{0}掷出了{1}", playerName[playerNum], rNum);
            playerPos[playerNum] += rNum;
            ChangePos();
            Console.ReadKey(true); // 重载，传入参数表示输入值不显示在控制台
            Console.WriteLine("{0}按任意键开始行动", playerName[playerNum]);
            Console.ReadKey(true); // 重载，传入参数表示输入值不显示在控制台
            Console.WriteLine("{0}行动完了", playerName[playerNum]);
            Console.ReadKey(true);

            // 行动规则
            if (playerPos[playerNum] == playerPos[1 - playerNum])
            {
                Console.WriteLine("玩家{0}踩到了玩家{1},玩家{1}退6格", playerName[playerNum], playerName[1 - playerNum]);
                playerPos[1 - playerNum] -= 6;
                ChangePos();
                Console.ReadKey(true);
            }
            else
            {
                switch (Map[playerPos[playerNum]])
                {
                    case 0:
                        Console.WriteLine("玩家{0}踩到了方块，什么都没发生", playerName[playerNum]);
                        Console.ReadKey(true);
                        break;
                    case 1:
                        Console.WriteLine("玩家{0}踩到了幸运轮盘，请选择1--交换位置,2--轰炸对方", playerName[playerNum]);
                        string input = Console.ReadLine();
                        while (true)
                        {
                            if (input == "1")
                            {
                                Console.WriteLine("玩家{0}选择与玩家{1}交换位置", playerName[playerNum], playerName[1 - playerNum]);
                                int temp;
                                temp = playerPos[playerNum];
                                playerPos[playerNum] = playerPos[1 - playerNum];
                                playerPos[1 - playerNum] = temp;

                                Console.WriteLine("交换完成,请按任意键继续游戏");
                                Console.ReadKey(true);
                                break;
                            }
                            else if (input == "2")
                            {
                                Console.WriteLine("玩家{0}选择轰炸玩家{1}", playerName[playerNum], playerName[1 - playerNum]);
                                playerPos[1 - playerNum] -= 6;
                                ChangePos();
                                Console.WriteLine("玩家{0}后退6格", playerName[1 - playerNum]);
                                Console.ReadKey(true);
                                break;
                            }
                            else
                            {
                                Console.WriteLine("只能输入1或2, 1--交换位置,2--轰炸对方");
                                input = Console.ReadLine();
                            }
                        }
                        break;
                    case 2:
                        Console.WriteLine("玩家{0}踩到了地雷,退6格", playerName[playerNum]);
                        Console.ReadKey(true);
                        playerPos[playerNum] -= 6;
                        ChangePos();
                        break;
                    case 3:
                        Console.WriteLine("玩家{0}踩到了暂停，暂停一回合", playerPos[playerNum]);
                        Flags[playerNum] = true;
                        Console.ReadKey(true);
                        break;
                    case 4:
                        Console.WriteLine("玩家{0}踩到了时空隧道,前进10格", playerName[playerNum]);
                        playerPos[playerNum] += 10;
                        ChangePos();
                        Console.ReadKey(true);
                        break;
                }// swith
            }// else
            ChangePos();
            Console.Clear();
            DrawMap();
        }
        public static void ChangePos()
        {
            if (playerPos[0] < 0)
            {
                playerPos[0] = 0;
            }
            if (playerPos[0] > 99)
            {
                playerPos[0] = 99;
            }
            
            if (playerPos[1] < 0)
            {
                playerPos[1] = 0;
            }
            if (playerPos[1] > 99)
            {
                playerPos[1] = 99;
            }
        }
    }
}
