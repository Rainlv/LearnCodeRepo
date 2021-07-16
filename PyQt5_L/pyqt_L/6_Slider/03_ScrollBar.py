from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("滚动条")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = QScrollBar(self)
        sb.move(100, 100)
        sb.resize(30, 200)

        # 水平滚动条
        sb2 = QScrollBar(Qt.Horizontal, self)
        sb2.move(150, 100)
        sb2.resize(200, 30)

        # 设置滑块高度，通过设置page step设置
        sb.setPageStep(50)

        sb.grabKeyboard()  # sb控件捕获键盘输入


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
