from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("CheckBox")
window.resize(500, 500)

btn = QCheckBox('Python', window)
# 1. 设置三态，三种状态
btn.setTristate(True)
# 2. 设置按钮状态
btn.setCheckState(Qt.PartiallyChecked)  # 部分选中
# btn.setCheckState(Qt.Unchecked)  # 未选中
# btn.setCheckState(Qt.Checked)  # 选中
# btn.setChecked(True)  # 选中
# 3.信号处理
# 三态时用stateChanged，两态就用toggled
btn.stateChanged.connect(lambda state: print(state))
# 三态时，部分选中和选中都视为True
btn.toggled.connect(lambda isChecked:print(isChecked))
window.show()

sys.exit(app.exec_())