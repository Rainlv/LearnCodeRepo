from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("父类滑块功能")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sd = QSlider(self)
        sd.move(50, 50)
        label = QLabel('0', self)
        label.move(200, 200)
        label.resize(100, 30)

        # 信号
        sd.valueChanged.connect(lambda val: label.setText(str(val)))

        # 设置最值
        sd.setMaximum(100)
        sd.setMinimum(60)

        # 设置数值
        sd.setValue(66)
        print(sd.value())

        # 步长设置（用于键盘↑↓和page up down，鼠标拖拽无关）
        sd.setSingleStep(5)  # ↑↓
        sd.setPageStep(10)

        # 跟踪设置
        sd.setTracking(False)  # 不追踪，鼠标松开后值才会改变
        print(sd.hasTracking())

        # 滑块位置设置
        sd.setSliderPosition(68)  # 非追踪状态时，值不会改变
        print(sd.sliderPosition())

        # 倒立外观
        sd.setInvertedAppearance(True)  # 上小下大
        print(sd.invertedAppearance())
        # 操作反转（键盘操作控制的是值的变化，不是滑块）
        sd.setInvertedControls(True)
        print(sd.invertedControls())

        # 滑块方向
        sd.setOrientation(Qt.Horizontal)  # 滑块水平摆放

        # 滑块是否被按下
        sd.setSliderDown(True)
        print(sd.isSliderDown())

        # 信号plus
        sd.sliderPressed.connect(lambda: print('滑块被按下'))
        sd.sliderReleased.connect(lambda: print('滑块被松开'))

        sd.sliderMoved.connect(lambda val: print('滑块移动', val))

        '''
            SliderNoAction = 0
            SliderSingleStepAdd = 1
            SliderSingleStepSub = 2
            SliderPageStepAdd = 3
            SliderPageStepSub = 4
            SliderToMinimum = 5
            SliderToMaximum = 6
            SliderMove = 7
        '''
        sd.actionTriggered.connect(lambda action: print('行为发生', action))  # 返回的是发生行为的枚举数字

        sd.rangeChanged.connect(lambda min_, max_: print('范围改变', min_, max_))

        sd.setMinimum(50)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
