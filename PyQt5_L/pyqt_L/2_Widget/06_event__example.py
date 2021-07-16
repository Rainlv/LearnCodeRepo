from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


# 实现窗口内移动窗口
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件案例")
        self.resize(500, 500)
        self.setup_ui()
        self.move_flag = False

    def setup_ui(self):
        pass

    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:  # 判定是鼠标左键而不是右键
            self.move_flag = True
            # 设置标志是为了防止设置鼠标追踪后，跳过该事件而执行下面的移动事件函数引起程序崩溃
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

            self.orgin_x = self.x()
            self.orgin_y = self.y()

    def mouseMoveEvent(self, evt):
        if self.move_flag:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            self.move(self.orgin_x + move_x, self.orgin_y + move_y)

    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False
        

# 实现监听键盘按键输入
class MyLabel(QLabel):
    def keyPressEvent(self, evt):
        # 键盘输入分为普通键和修饰键

        # 普通键写法：
        if evt.key() == Qt.Key_Tab:
            print('Tab被按下')

        # 修饰键加普通键写法：
        elif evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            print('Ctrl+S被按下')

        # 多修饰键写法：
        elif evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_R:
            print('shift+ctrl+r被按下')


#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = Window()
window.setMouseTracking(True)
#  2.2 设置控件

# label = MyLabel(window)
# label.resize(200, 200)
# label.move(100, 100)
# label.setStyleSheet('background-color:cyan;')
# label.grabKeyboard()  # 由label捕获键盘输入，而不是父控件

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
