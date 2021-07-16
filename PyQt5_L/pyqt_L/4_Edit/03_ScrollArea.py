from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("TextEdit父类介绍")
window.resize(500, 500)

te = QTextEdit(window)
# 1.滚动条设置
'''
    Qt.ScrollBarAlwaysOff  不显示滚动条
    Qt.ScrollBarAlwaysOn  始终显示滚动条
    Qt.ScrollBarAsNeeded  需要时显示（当内容多起来时）
'''
# 1.1 垂直方向滚动条设置
te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
# 1.2 水平方向滚动条设置
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

# 2. 角落控件设置（两个滚动条之间的角落）
btn = QPushButton(window)
btn.setIcon(QIcon('../2_Widget/xxx.png'))
te.setCornerWidget(btn)
btn.pressed.connect(lambda: print('按钮被按下'))

window.show()

sys.exit(app.exec_())
