from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("扁平化设置")
window.resize(500, 500)

btn = QPushButton('按钮', window)
btn.setStyleSheet('background-color:red;')
# 设置扁平化，即按钮不会突出，与背景融合，正常不会显示设置的StyleSheet
btn.setFlat(True)
print(btn.isFlat())


window.show()

sys.exit(app.exec_())