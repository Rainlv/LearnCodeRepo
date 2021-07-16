from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("内容边距")
window.resize(500, 500)

# label.setContentsMargins(左,上,右,下)
label = QLabel(window)
label.setText('这是内容')
label.resize(200, 200)
label.setStyleSheet('background-color:cyan;')
label.setContentsMargins(100, 50, 0, 0)
print(label.contentsRect())
# 获取margin值
print(label.getContentsMargins())

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())