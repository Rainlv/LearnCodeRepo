from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


# QAbstractButton是抽象类，需要子类化
class Btn(QAbstractButton):
    def paintEvent(self, QPaintEvent):
        # 1. 创建一个painter
        painter = QPainter(self)
        # 2. 创建一个pen
        pen = QPen(QColor(10, 20, 30), 10)  # 颜色，粗细
        # 3. 给painter对象设置pen
        painter.setPen(pen)
        # 4. painter绘制
        painter.drawEllipse(0, 0, 100, 100)  # 位置
        painter.drawText(30, 50, self.text())  # 位置，内容


#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("重写paint_event")
window.resize(500, 500)

btn = Btn(window)
btn.resize(100, 100)
btn.setText('按钮')

btn.pressed.connect(lambda: print('按钮被点击了'))

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
