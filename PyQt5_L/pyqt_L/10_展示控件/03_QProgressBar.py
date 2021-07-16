from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("进度条")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)

        # 最值区间设置
        # pb.setMaximum(100)
        # pb.setMinimum(50)
        pb.setRange(0, 100)
        # pb.setRange(0, 0)  # 处于繁忙状态

        # 设置当前值
        pb.setValue(75)  # 设置的不是百分比，百分比是根据当前值和范围计算得出的

        # 重置
        # 重置的只是value，区间范围不会变，重置完后value变为区间最小值减一
        def test():
            pb.reset()
            print(pb.value())
            print(pb.maximum())

        btn = QPushButton('测试按钮', self)
        btn.move(50, 50)
        # btn.clicked.connect(test)

        # 文本内容展示格式化
        '''
            %p 百分比
            %v 当前值
            %m 总值（最大值-最小值计算得到的）
        '''
        pb.setFormat('当前人数/总人数 %p%')  # 后面的百分号是显示用的
        pb.resize(400, 40)
        # 重置字符串格式
        # btn.clicked.connect(lambda: pb.resetFormat())
        # 文本对齐方式
        pb.setAlignment(Qt.AlignHCenter)

        # 隐藏文本
        pb.setTextVisible(True)
        # 获取文本
        print(pb.text())

        # 进度条方向（水平，垂直）
        def wasd():
            pb.resize(40, 400)
            # pb.setOrientation(Qt.Horizontal)  # 水平
            pb.setOrientation(Qt.Vertical)  # 垂直
            # 垂直进度条好像不会显示文本内容

            # 倒置进度条方向（从后往前加载）
            pb.setInvertedAppearance(True)

        btn.clicked.connect(wasd)

        # 小案例+信号
        time = QTimer()

        def change_progress():
            if pb.value() == pb.maximum():
                time.stop()
            pb.setValue(pb.value() + 1)

        time.timeout.connect(change_progress)
        time.start(100)

        pb.valueChanged.connect(lambda val:print('当前进度为', val))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
