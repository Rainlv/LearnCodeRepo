from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动画学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton('按钮', self)
        btn.move(100, 100)
        btn.resize(200, 200)
        btn.setStyleSheet('background-color:cyan;')

        # 1. 创建一个动画对象，设置目标属性
        anime = QPropertyAnimation(btn, b'pos', self)
        # anime = QPropertyAnimation(self)
        '''常见属性
            pos  位置  --> QPoint()
            geometry  尺寸+位置  -->QRect()
            size  尺寸  --> Qsize()
            windowOpacity  窗口透明度  -->int  0-1
        '''
        # anime.setTargetObject(btn)
        # anime.setPropertyName(b'pos')

        # 2. 设置属性值 开始 插值 结束
        anime.setStartValue(QPoint(0, 0))
        anime.setKeyValueAt(0.5, QPoint(200, 100))  # 插值，参数;动画播放进度（0.5就是放到一半），值
        anime.setEndValue(QPoint(300, 300))

        # 3. 动画时长
        anime.setDuration(1000)

        anime.setLoopCount(3)  # 设置动画重复次数
        anime.setDirection(QAbstractAnimation.Backward)  # 设置动画方向，这里设置的是倒放

        # 4. 设置动画曲线（默认线性）
        anime.setEasingCurve(QEasingCurve.InQuad)


        # 5. 开始动画
        anime.start()

        # anime.stop()  # 停止动画
        # anime.pause()  # 暂停动画
        # anime.resume()  # 暂停状态下，恢复动画

        # btn.clicked.connect(lambda: print(anime.currentLoop(), anime.currentLoopTime(), anime.currentTime()))  # 当前循环次数，本次循环动画运行时间,动画实际运行时间

        def operate():
            if anime.state() == QAbstractAnimation.Running:  # 状态
                anime.pause()
            elif anime.state() == QAbstractAnimation.Paused:
                anime.resume()
        btn.clicked.connect(operate)


        # 信号
        # anime.finished.connect()  # 运行结束，不是单次循环
        # anime.currentLoopChanged.connect(n)  # 循环改变，参数：当前循环次数
        # anime.stateChanged.connect(x, y)  # 状态改变，参数：新状态，旧状态（都是枚举值对应数值）
        # anime.directionChanged.connect(x)  # 方向改变，参数：新方向


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
