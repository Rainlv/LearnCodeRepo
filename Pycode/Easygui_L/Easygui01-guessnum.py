import easygui as g
import random as r

def game():
    # 判断结果
    def judeg():
        nonlocal inp_num
        if inp_num == num:
            g.msgbox( msg='恭喜你，猜对了！')
            if g.ccbox(msg='是否再来一局',title='重来？'):
                game()
            else:
                g.msgbox(msg='游戏结束')
        else:
            msgword = '猜错啦，是否重来'
            choices = ['继续','不来了']
            if g.ccbox( msg=msgword,title='是否继续',choices=choices):
                if inp_num > num:
                    g.msgbox('刚刚输大了')
                else:
                    g.msgbox('刚刚输小了')
                inp_num = g.integerbox(msg,title,lowerbound=0,upperbound=10)
                judeg()
            else:
                g.msgbox('游戏失败')
    # 游戏框
    num = r.randint(0,10) 
    msg = '猜数字（0-10）'
    title = '数字小游戏'
    inp_num = g.integerbox(msg,title,lowerbound=0,upperbound=10)
    if inp_num:
        judeg()
    else:
        g.msgbox('游戏结束')
game()
    