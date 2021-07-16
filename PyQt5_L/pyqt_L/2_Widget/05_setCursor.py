from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


class MyWindow(QWidget):
    def mouseMoveEvent(self, me):
        # 鼠标追踪未开启时，只有按住鼠标左键移动，该函数才会执行
        # print('鼠标移动了')
        # print('全局鼠标位置：', me.globalPos())
        # print('控件内鼠标位置：', me.localPos())
        label = self.findChild(QLabel)
        label.move(me.localPos().x(), me.localPos().y())

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = MyWindow()
#  2.2 设置控件
window.setWindowTitle("鼠标指针相关")
window.resize(500, 500)

label = QLabel(window)
label.move(100, 100)
label.setText('十七张牌你能秒我？')
label.setStyleSheet('background-color:cyan;')
# 设置鼠标追踪
window.setMouseTracking(True)
print(window.hasMouseTracking())  # 当前追踪状态，是否追踪

# 设置指针为内置样式
# window.setCursor(Qt.ForbiddenCursor)

# 设置自定义样式
pixmap = QPixmap('xxx.png')
new_pixmap = pixmap.scaled(30, 30)  # 设置图片缩放
cursor = QCursor(new_pixmap, 0, 0)
# cursor = QCursor(new_pixmap, 0, 0) 第一个参数是QPixmap对象（决定鼠标样式的图片），第二三个参数决定鼠标点击的有效区域（默认图片中间）
window.setCursor(cursor)
# window.unsetCursor()  # 重置鼠标样式

current_cursor = window.cursor()
# print(current_cursor.pos())  # 获取鼠标位置
# current_cursor.setPos(0, 0)  # 设置鼠标位置

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
