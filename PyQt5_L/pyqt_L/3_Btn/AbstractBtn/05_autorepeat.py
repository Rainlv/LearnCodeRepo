from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("自动重复")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('按钮')
btn.move(200, 200)

n = 1


def cao():
    global n
    print('按钮被点击了', n)
    n += 1


btn.pressed.connect(cao)

btn.setAutoRepeat(True)  # 设置自动重复
btn.setAutoRepeatDelay(2000)  # 设置触发延迟
btn.setAutoRepeatInterval(1000)  # 设置重复频率

print(btn.autoRepeat())
print(btn.autoRepeatDelay())
print(btn.autoRepeatInterval())

window.show()

sys.exit(app.exec_())
