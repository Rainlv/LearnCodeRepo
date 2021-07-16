from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("文本编辑修改状态")
window.resize(500, 500)

le = QLineEdit(window)
le.move(200, 200)
le2 = QLineEdit(window)
le2.move(200, 250)

btn = QPushButton('按钮', window)
btn.move(200, 280)
le2.setModified(True)  # 设置文本处于编辑状态（文本被修改）
btn.pressed.connect(lambda: print(le.isModified()))  # 文本是否被修改过

window.show()

sys.exit(app.exec_())
