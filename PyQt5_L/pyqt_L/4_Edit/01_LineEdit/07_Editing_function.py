from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("常用编辑功能和信号")
window.resize(500, 500)

le = QLineEdit(window)
le.move(200, 200)
le2 = QLineEdit(window)
le2.move(200, 230)
btn = QPushButton('按钮', window)
btn.move(200, 260)

# 编辑功能
def cao():
    # le.backspace()  # 向左删一个字符
    # le.del_()  # 向右删除一个字符
    # le.clear()  # 清空文本框

    # 注意焦点位置
    # le.cursorBackward(True, 3)
    # le.copy()  # 复制
    # le.end(False)
    # le.paste()  # 粘贴
    # le.cut()    # 剪切

    # le.undo()   # 撤销
    # le.redo()   # 取消撤销 ctrl + Y
    # print(le.isUndoAvailable())  # 获取能否撤销
    # print(le.isRedoAvailable())

    # le.setDragEnabled(True)  # 设置文本是否可拖放，默认不可以

    # 注意焦点位置
    le.setSelection(2, 1)  # 选中文本，第一个是光标起始位置，第二个是选中长度
    # le.selectAll()  # 全选
    # le.deselect()  # 取消选中

    # print(le.hasSelectedText())  # 是否选中文本
    # print(le.selectedText())  # 获取选中的文本
    print(le.selectionLength())  # 选中文本长度，
    print(le.selectionStart())  # 选中文本起始位置，没有返回-1
    print(le.selectionEnd())    # 选中文本末尾位置，没有返回-1


btn.pressed.connect(cao)

# 信号
# 会返回val，是文本框内的内容
le.textChanged.connect(lambda val: print('文本内容发生改变', val))  # 内容改变就会触发
le.textEdited.connect(lambda val: print('文本被编辑', val))  # 用户编辑才会触发，代码改变不会
le.setText('11')  # 只触发 textChanged

le.returnPressed.connect(lambda: print('回车键被按下'))
# le.returnPressed.connect(lambda: le2.setFocus())
le.editingFinished.connect(lambda: print('结束编辑'))  # 回车被按下会触发，焦点切换也会

le.cursorPositionChanged.connect(lambda old_pos, new_pos: print(old_pos, new_pos))  # 光标位置改变触发，两个参数（原来光标位置和改变后位置）
le.selectionChanged.connect(lambda: print('选中文本改变'))


window.show()

sys.exit(app.exec_())
