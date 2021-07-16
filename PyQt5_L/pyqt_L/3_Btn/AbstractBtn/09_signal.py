from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("按钮相关信号")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('按钮')
btn.move(250, 250)
btn.setCheckable(True)
btn.pressed.connect(lambda: print('按钮被按下'))
btn.released.connect(lambda: print('按钮被松开'))  # 鼠标移除有效区域也算松开
btn.clicked.connect(lambda x: print('按钮被点击', x))  # 点击事件要按钮被按下并在有效区域内松开才算完成,按钮当前是否被选中会作为参数传入
btn.toggled.connect(lambda x: print('按钮选中状态发生了改变', x))  # 按钮当前是否被选中会作为参数传入

window.show()

sys.exit(app.exec_())