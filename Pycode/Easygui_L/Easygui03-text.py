import easygui as g
import os


path = g.fileopenbox(default=r'E:\Code\Pycode',filetypes=['*.txt'])
if path:
    try:
        filename = os.path.basename(path)

        msg="文件{}的内容如下:".format(filename)
        title='显示文件内容'
        if path:
            with open(path,'r',encoding='utf-8') as f:
                oldfile = f.read()
                newfile = g.textbox(text=oldfile,msg=msg,title=title)
        if oldfile != newfile:
            choices = ['覆盖保存','另存为','取消保存']
            decide = g.buttonbox(msg='文件修改，是否保存',choices=choices)
            if decide == '覆盖保存':
                with open(path,'w') as w:
                    w.write(newfile)
            elif decide == '另存为':
                savepath = g.filesavebox(title='另存为',filetypes=['*.txt'])
                get_fname = os.path.splitext(savepath)
                if get_fname[1] != '.txt':
                    savepath = get_fname[0]+'.txt'
                with open(savepath,'w') as sw:
                    sw.write(newfile)
    except Exception as err:
        g.msgbox(msg=err)
else:
    g.msgbox('操作取消')