from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("窗口设置案例")
        self.resize(500, 500)
        self.setWindowOpacity(0.7)

        self.btn_w = 60
        self.btn_h = 30
        self.top_margin = 5

        self.setup_ui()

    def setup_ui(self):
        # 关闭按钮
        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.setText('关闭')
        close_btn.resize(self.btn_w, self.btn_h)

        # 最大化按钮
        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setText('最大化')
        max_btn.resize(self.btn_w, self.btn_h)

        # 最小化按钮
        min_btn = QPushButton(self)
        self.min_btn = min_btn
        min_btn.setText('最小化')
        min_btn.resize(self.btn_w, self.btn_h)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText('最大化')
            else:
                self.showMaximized()
                max_btn.setText('恢复')

        close_btn.pressed.connect(self.close)
        max_btn.pressed.connect(max_normal)
        min_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, evt):
        window_x = self.width()
        close_btn_x = window_x - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

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
        

app = QApplication(sys.argv)  # sys.argv接受外部参数

# 设置无边框窗口
# window = QWidget(flags=Qt.FramelessWindowHint)
window = Window()

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
