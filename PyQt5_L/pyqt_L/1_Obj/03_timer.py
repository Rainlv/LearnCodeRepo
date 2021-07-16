from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


# .startTimer(ms)
class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)
        self.setText('10')
        self.move(150, 150)
        self.setStyleSheet('font-size:30px')
        self.timer_id = self.startTimer(1000)  # 每过1000ms执行一次timerEvent

    # startTimer会执行类中的timerEvent
    def timerEvent(self, *args, **kwargs):
        print('xx')
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))
        if current_sec == 0:
            print('停止')
            self.killTimer(self.timer_id)

    def setSec(self, ms):
        self.setText(str(ms))


#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("timer_learn")
window.resize(500, 500)

label = MyLabel(window)
label.setSec(5)

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
