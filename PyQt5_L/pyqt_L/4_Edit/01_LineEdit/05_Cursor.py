from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("光标移动")
window.resize(500, 500)

le = QLineEdit(window)
le.move(200, 200)

btn = QPushButton('按钮', window)
btn.move(200, 230)


def cao():
    # cursorBackward(bool, steps=1)

    # le.cursorBackward(True, 2)  # 第一个参数决定光标移动是否选中文本，第二个是每次移动步长
    # le.cursorForward(True, 1)
    # le.cursorWordBackward(True)  # 移动一个单词长度，原理就是按空格分隔
    # le.cursorWordForward(True)
    # le.home(True)  # 光标移到行首
    # le.end(True)

    # le.setCursorPosition(5)  # 设置光标位置，写小数会下载取整
    # print(le.cursorPosition())

    print(le.cursorPositionAt(QPoint(15, 5)))  # 获取点坐标对应的光标位置，点坐标是相对文本框而言的
    le.setFocus()


# 设置为pressed时，好像会有不一样的反应
btn.clicked.connect(cao)

window.show()

sys.exit(app.exec_())
