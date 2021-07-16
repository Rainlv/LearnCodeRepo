from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("默认选中的按钮设置")
window.resize(500, 500)

btn = QPushButton('按钮1', window)
btn.move(100, 100)
btn2 = QPushButton('按钮2', window)
btn.setAutoDefault(True)  # 点击后设为默认（实测好像一开始就是默认）
# btn.setDefault(True)  # 打开时就是默认
print(btn.autoDefault())
print(btn2.autoDefault())
print(btn.isDefault())
print(btn2.isDefault())


window.show()

sys.exit(app.exec_())