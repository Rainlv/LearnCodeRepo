from PyQt5.Qt import *


# 事件转发机制，若子控件没有定义相关的事件方法，会默认从父控件中调用
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件转发机制")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self, QMouseEvent):
        print('顶层控件被按下')


class MidWindow(QWidget):

    def mousePressEvent(self, QMouseEvent):
        print('中间控件被按下')
    # pass


class MyLabel(QLabel):

    def mousePressEvent(self, evt):
        print('标签被按下')
        # evt.accept()  # 标识事件被接收，不再转发
        evt.ignore()  # 标识事件要被转发到上层
        print(evt.isAccepted())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()
    mid_window = MidWindow(window)
    label = MyLabel(mid_window)

    mid_window.setStyleSheet('background-color:cyan;')
    mid_window.resize(200, 200)
    mid_window.move(100, 100)
    mid_window.setAttribute(Qt.WA_StyledBackground, True)

    label.setStyleSheet('background-color:red;')
    label.resize(100, 100)
    label.move(50, 50)
    label.setText('这是一个标签')
    window.show()

    sys.exit(app.exec_())
