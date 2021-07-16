from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


# 事件运行顺序：
# 1. 操作系统第一个接收事件，分发到相应的应用程序
# 2. 应用程序接收事件，将事件接收者receiver和事件对象event传递给QApplication的notify函数
# 3. notify将事件分发给receiver的event方法
# 4. event根据事件类型分发给具体的执行函数

class App(QApplication):
    # notify函数用来接收app产生的事件
    def notify(self, receiver, event):
        if receiver.inherits('QPushButton') and event.type() == QEvent.MouseButtonPress:
            print(receiver, event)
        return super().notify(receiver, event)


class Btn(QPushButton):
    # event函数用来接收传递到控件的事件
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print('类中event函数执行', evt)
        return super().event(evt)

    # 具体的事件执行函数
    def mousePressEvent(self, *args, **kwargs):
        print('鼠标按下事件产生')
        return super(Btn, self).mousePressEvent(*args, **kwargs)


#  1. 创建一个应用程序对象
app = App(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("event-and-receiver")
window.resize(500, 500)

btn = Btn(window)
btn.setText('点击')
btn.resize(100, 100)
btn.move(200, 200)
btn.pressed.connect(lambda: print('点击事件槽函数被执行'))

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
