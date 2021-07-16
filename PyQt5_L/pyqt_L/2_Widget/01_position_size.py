from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("pos_size")
window.move(100, -100)
window.move(100, 100)  # .move(x, y)
window.resize(500, 500)  # .resize(width, height)
# 注：窗口有最小尺寸，再小就不会变化了
# window.setFixedSize(500, 600)  # 设置固定大小，不能改变
label = QLabel(window)
label.setText('测试文字')
label.setStyleSheet('background-color:cyan;font-size:25px;')
label.move(100, 200)


def cao():
    new_content = label.text()
    label.setText(new_content + '测试文字')
    label.adjustSize()  # 自适应大小


btn = QPushButton(window)
btn.resize(100, 100)
btn.move(200, 300)
btn.setText('增加内容')
btn.clicked.connect(cao)
# print(window.x())
# print(window.pos())
# print(window.width())
# print(window.size())
# print(window.geometry())


#  2.3 展示控件

# 位置大小信息只有在窗口显示完后才能准确计算
window.show()

# window.setGeometry(0, 0, 500, 500)  # show前设置与show后设置效果不同

# print(window.x())  # 相对于父控件的x位置，包含框架
print(window.pos())  # x,y的组合
# print(window.width())  # 控件宽度，不包含窗口框架
# print(window.size())  # width和height的组合
# print(window.frameSize())  # 含框架的size
# print(window.geometry())  # 用户区域对于父控件的位置和尺寸组合 x0(不是x),y0,width,height
# print(window.rect())  # 0,0,width,height

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
