from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("字体选择框")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        fcb = QFontComboBox(self)
        label = QLabel('测试文字段', self)
        label.move(50, 50)

        fcb.currentFontChanged.connect(lambda font: label.setFont(font))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
