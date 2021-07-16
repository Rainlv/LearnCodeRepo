from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


# class Label(QLabel):
#     def mousePressEvent(self, QMouseEvent):
#         self.setStyleSheet('background-color:red;')

class Window(QWidget):
    def mousePressEvent(self, evt):
        # 获取鼠标点击的位置
        local_x = evt.x()
        local_y = evt.y()
        # 根据位置返回子控件
        sub_widget = self.childAt(local_x, local_y)
        if sub_widget:
            sub_widget.setStyleSheet('background-color:red;')

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = Window()
#  2.2 设置控件
window.setWindowTitle("父子关系补充")
window.resize(500, 500)

# ********API*********
label2 = QLabel(window)
print(window.childAt(50, 50))  # 返回该位置对应的子控件
print(label2.parentWidget())  # 返回控件对应的父控件
print(window.childrenRect())  # 返回子控件组成的矩形区域(0, 0, 500, 430)
# ********API*********

for i in range(1, 11):
    label = QLabel(window)
    label.setText('标签' + str(i))
    label.move(i * 40, i * 40)

print(window.childAt(50, 50))
print(window.childrenRect())
#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
