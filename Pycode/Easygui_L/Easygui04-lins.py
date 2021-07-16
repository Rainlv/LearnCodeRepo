import os 
import easygui as g

# os.path.split()获取文件名
# os.path.splitext()获取扩展名


target = [ '.cpp','.py','.html','.c','.java' ]
code_file = []


def search(path):
    global code_file

    for doucument_name in os.listdir(path):
        doucument_path = os.path.join(path, doucument_name)
        if os.path.isdir(doucument_path):
            search(doucument_path)
        elif os.path.splitext(doucument_name)[1] in target:
            code_file.append(doucument_path)
        else:
            pass
    return code_file


def code_lines(code_file_path):
    lines = 0
    with open(code_file_path,'rb') as r:
        for line in r:
            lines += 1
    return lines


def show_result(path):
    output = []
    total_lines = 0
    py_file = 0
    html_file = 0
    cpp_file = 0
    c_file = 0
    java_file = 0
    py_lines = 0
    html_lines = 0
    cpp_lines = 0
    c_lines = 0
    java_lines = 0
    
    for src in search(path):
        if os.path.splitext(src)[1] == '.py':
            py_lines += code_lines(src)
            py_file += 1
        if os.path.splitext(src)[1] == '.html':
            html_lines += code_lines(src)
            html_file += 1
        if os.path.splitext(src)[1] == '.cpp':
            cpp_lines += code_lines(src)
            cpp_file += 1
        if os.path.splitext(src)[1] == '.c':
            c_lines += code_lines(src)
            c_file += 1
        if os.path.splitext(src)[1] == '.jave':
            java_lines += code_lines(src)
            java_file += 1
        src_lines = code_lines(src)
        total_lines += src_lines
        file_name = os.path.split(src)
        file_name = file_name[1]
        output += '{}：           共有{}行代码 \n'.format(file_name,src_lines)
    
    with open(r'E:\Code\Pycode\Cal_CodeLine.txt','w') as w:
        w.writelines('代码总行数为{} \n'.format(total_lines))
        w.writelines('【.py】源文件数目为：{}，源代码总行数为{} \n'.format(py_file,py_lines))
        w.writelines('【.html】源文件数目为：{}，源代码总行数为{} \n'.format(html_file,html_lines))
        w.writelines('【.cpp】源文件数目为：{}，源代码总行数为{} \n'.format(cpp_file,cpp_lines))
        w.writelines('【.c】源文件数目为：{}，源代码总行数为{} \n'.format(c_file,c_lines))
        w.writelines('【.java】源文件数目为：{}，源代码总行数为{} \n'.format(java_file,java_lines))

        w.writelines(output)
    
    with open(r'E:\Code\Pycode\Cal_CodeLine.txt','r') as r:
        text = r.read()
        
    g.textbox(msg='代码行数统计如下：',title='代码行数统计工具',text=text)


Code_path = g.diropenbox(msg='请选择代码所在目录',title='代码行数统计工具')
show_result(Code_path)