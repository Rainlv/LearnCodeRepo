from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("按钮排他性设置")
window.resize(500, 500)

# 同一个父控件下的子控件，设置了排他性的按钮之间具有排他性
for i in range(1, 4):
    btn = QPushButton(window)
    btn.move(20 * i, 20 * i)
    btn.setText('按钮{}'.format(i))
    btn.setAutoExclusive(True)
    btn.setCheckable(True)
btn = QPushButton(window)
btn.move(300, 300)
btn.setText('另一个按钮')
btn.setCheckable(True)
print(btn.autoExclusive())

# QRadioButton默认具有排他性
for i in range(1, 4):
    r_btn = QRadioButton(window)
    r_btn.move(100+20 * i, 100+20 * i)
    r_btn.setAutoExclusive(True)
    r_btn.setText('按钮{}'.format(i))
    r_btn.setCheckable(True)
r_btn = QRadioButton(window)
r_btn.move(200, 200)
r_btn.setText('另一个按钮')
r_btn.setCheckable(True)
print(r_btn.autoExclusive())

window.show()

sys.exit(app.exec_())
