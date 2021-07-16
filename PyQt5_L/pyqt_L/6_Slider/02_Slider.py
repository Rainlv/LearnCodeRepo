from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sd = QSlider(self)
        '''
            NoTicks = 0  无刻度线
            TicksAbove = 1  上方绘制刻度线（水平滑块）
            TicksBelow = 2  下方绘制刻度线（水平滑块）
            TicksLeft = 1   左侧绘制刻度线（垂直滑块）
            TicksRight = 2  右侧绘制刻度线（垂直滑块）
            TicksBothSides = 3  在凹槽两侧绘制
        '''
        sd.setTickPosition(QSlider.TicksLeft)
        # （默认）刻度线的步长是一个page step的长度，更改page step会改变刻度线密集程度
        # 手动设置刻度线步长，不影响步长
        sd.setTickInterval(20)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
