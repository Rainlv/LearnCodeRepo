from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("QLabel的学习")
window.resize(500, 500)

label = QLabel(window)
label.setText('xxx')

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())