from PyQt5.Qt import *


class Label(QLabel):
    # 设置最小尺寸
    def minimumSizeHint(self):
        return QSize(100, 20)

    # 设置建议尺寸
    def sizeHint(self):
        return QSize(150, 60)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("补充讲解")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = Label('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:red')
        # 1. 创建一个布局管理器对象
        layout = QBoxLayout(QBoxLayout.LeftToRight)  # 传一个方向参数
        # 2. 给父控件设置布局对象
        self.setLayout(layout)
        # 3. 把父控件中的子控件添加到布局中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # 设置尺寸策略
        '''
            QSizePolicy.Fixed 实际尺寸参考sizeHint，不改变
            Minimum  可以伸缩，以sizeHint为最小值
            Maximum  可以伸缩，以sizeHint为最大值
            Preferred  可以自由伸缩，但获取空间的优先级较小
            Expanding  可以自由伸缩，获取更大空间的优先级大
            MinimumExpanding  可以自由伸缩，以sizeHint为最小值，获取更大空间的优先级大
            Ignored  忽略sizeHint的作用（空间过小会没）
        '''
        # label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 水平，垂直策略
        label1.hide()
        sp = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # 隐藏时占位
        sp.setRetainSizeWhenHidden(True)
        label1.setSizePolicy(sp)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
