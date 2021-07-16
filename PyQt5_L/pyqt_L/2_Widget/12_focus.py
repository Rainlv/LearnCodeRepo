from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print(self.focusWidget())  # 获得当前焦点控件的对象
        # self.focusNextChild()  # 聚焦到下一个子控件
        # self.focusPreviousChild()  # 聚焦到上一个子控件
        self.focusNextPrevChild(True)  # 聚焦到上一个（True）或下一个（False）子控件


#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = Window()
#  2.2 设置控件
window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le2 = QLineEdit(window)
le3 = QLineEdit(window)
le1.move(50, 50)
le2.move(150, 150)
le3.move(250, 250)

le2.setFocus()  # 设置le2为焦点

# le2.setFocusPolicy(Qt.TabFocus)  # 只能通过tab键来进行le2的选中，鼠标点击不行
# le2.setFocusPolicy(Qt.ClickFocus)  # 只能通过鼠标点击键来进行le2的选中，tab不行
le2.setFocusPolicy(Qt.StrongFocus)  # 鼠标和tab都行
# le2.setFocusPolicy(Qt.NoFocus)  # 只能通过代码来选中

le2.clearFocus()  # 清除le2的焦点，会默认把焦点转移到第一个控件

# 设置通过tab键更换子控件获取焦点的顺序
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)
QWidget.setTabOrder(le2, le1)

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
