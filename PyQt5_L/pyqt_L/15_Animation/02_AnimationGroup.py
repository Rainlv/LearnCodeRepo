from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动画组")
        self.resize(700, 700)
        self.setup_ui()

    def setup_ui(self):
        red_btn = QPushButton('红色按钮', self)
        red_btn.resize(100, 100)
        red_btn.setStyleSheet('background-color:red;')

        green_btn = QPushButton('绿色按钮', self)
        green_btn.resize(100, 100)
        green_btn.setStyleSheet('background-color:green;')
        green_btn.move(100, 150)

        animation = QPropertyAnimation(green_btn, b'pos', self)

        animation.setKeyValueAt(0, QPoint(150, 150))
        animation.setKeyValueAt(0.25, QPoint(550, 150))
        animation.setKeyValueAt(0.5, QPoint(550, 550))
        animation.setKeyValueAt(0.75, QPoint(150, 550))
        animation.setKeyValueAt(0.1, QPoint(150, 150))

        animation.setDuration(2300)

        animation.start()
        # 动画组
        animation2 = QPropertyAnimation(red_btn, b'pos', self)

        animation2.setKeyValueAt(0, QPoint(0, 0))
        animation2.setKeyValueAt(0.25, QPoint(0, 500))
        animation2.setKeyValueAt(0.5, QPoint(500, 500))
        animation2.setKeyValueAt(0.75, QPoint(500, 0))
        animation2.setKeyValueAt(0.1, QPoint(0, 0))

        animation2.setDuration(2300)

        animation.start()


        # animation_group = QParallelAnimationGroup(self)  # 并行动画
        animation_group = QSequentialAnimationGroup(self)  # 串行动画
        animation_group.addAnimation(animation)
        animation_group.addPause(1000)  # 串行动画专属
        animation_group.addAnimation(animation2)
        animation_group.start()
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
