from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RubberBand学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        '''
            Line = 0  直线
            Rectangle = 1  矩形
        '''
        rb = QRubberBand(QRubberBand.Rectangle, self)
        rb.setGeometry(10, 10, 60, 60)
        rb.show()  # 默认不可见，要手动show


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
