from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


class Btn(QPushButton):
    def paintEvent(self, QPaintEvent):
        print('按钮绘制')
        return super(Btn, self).paintEvent(QPaintEvent)


class Window(QWidget):
    def paintEvent(self, QPaintEvent):
        print('窗口绘制')
        return super(Window, self).paintEvent(QPaintEvent)


#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = Window()
#  2.2 设置控件
window.setWindowTitle("交互状态[*]")
window.resize(500, 500)

btn = Btn(window)
btn.setText('按钮')
btn.resize(100, 100)
btn.move(100, 100)
btn.pressed.connect(lambda: btn.hide())

# 是否被编辑状态
# 在窗口标题加上[*]，若处于编辑状态会显示
window.setWindowModified(True)
print(window.isWindowModified())

# 是否可交互状态
# btn.setEnabled(True)  # 设置按钮是否可用
# print(btn.isEnabled())  # 按钮是否可用


# 是否可见状态
# 每次子控件中状态或样式改变，整个窗口都重新绘制
# 先绘制父控件，在绘制子控件。父控件不显示，子控件也不显示
w2 = QWidget()
window.setVisible(True)
btn.destroyed.connect(lambda: print('控件被删除'))
# btn.deleteLater()
btn.setAttribute(Qt.WA_DeleteOnClose, True)  # 设置了这一属性后，close后控件即被删除
btn.close()  # 默认情况效果同隐藏
# w2.show()
# window.show()
# window.hide()
# window.setHidden(False)
# btn.isVisible()  # 控件的最终状态是否可见（被上层控件覆盖也算可见）
# btn.isHidden()  # 控件是否被设置为隐藏。（即相对于父控件来说是否可见，父控件存在时是否可见）
# btn.isVisibleTo(window)  # 控件相对于某个控件是否可见。控件状态能随着window的显示隐藏，则true


# 是否活跃窗口
# window.activateWindow()
# print('w2是否活跃窗口:', w2.isActiveWindow())
# print('window是否活跃窗口:', window.isActiveWindow())


sys.exit(app.exec_())
