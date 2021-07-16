import easygui as g

title = '账号中心'
msg = '''      【*真实姓名】为必填项
      【*手机号码】为必填项
      【*E-mail】为必填项'''
fileds = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
ret = g.multenterbox(msg= msg,title=title,fields=fileds)

def judge():
    global ret
    for values,items in enumerate(ret):
        if values==0 or values==1 or values==3 or values==5:
            if not items:
                g.msgbox(msg='{}不能为空'.format(fileds[values]))
                if g.ccbox(msg='是否重新输入'):
                    ret = g.multenterbox(msg= msg,title=title,fields=fileds)
                    judge()
                else:
                    g.msgbox('输入失败')
                    break
    else:
            g.msgbox('输入完成')

judge()