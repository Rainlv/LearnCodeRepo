from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        dsb = QDoubleSpinBox(self)
        dsb.move(100, 100)
        dsb.resize(100, 30)
        self.dsb = dsb

    def api(self):
        # 最大最小，默认0.00-99.99
        # 步长，默认1.00

        # 保留小数位数
        self.dsb.setDecimals(1)  # 1位
        print(self.dsb.decimals())

        # 获取数值文本（文本类型）
        print(self.dsb.cleanText())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
