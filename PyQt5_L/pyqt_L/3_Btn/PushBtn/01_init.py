from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("构造函数")
window.resize(500, 500)

# QPushButton(icon, text, parent)
btn = QPushButton(QIcon('../../2_Widget/xxx.png'), '按钮', window)


window.show()

sys.exit(app.exec_())