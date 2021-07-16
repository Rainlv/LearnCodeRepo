from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


class Label(QLabel):
    def mousePressEvent(self, evt):
        self.raise_()

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("层级关系")
window.resize(500, 500)

label = Label(window)
label.setText('标签111')
label.resize(200, 200)
label.setStyleSheet('background-color:cyan;')

label2 = Label(window)
label2.setText('标签222')
label2.resize(200, 200)
label2.move(100, 100)
label2.setStyleSheet('background-color:red;')

# label2.lower()
# label.raise_()
label2.stackUnder(label)  # label2放在label下面
#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())