from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("齿轮状滑块")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        dia = QDial(self)
        # 设置刻度可见
        dia.setNotchesVisible(True)
        # 大刻度（page step）
        dia.setPageStep(20)
        # 刻度包裹（不会在下面留空）
        dia.setWrapping(True)
        # 设置刻度密度
        dia.setNotchTarget(10)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
