from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys
#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()
window.setWindowTitle("图标设置")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('按钮')

# 1. 设置图标
icon = QIcon('../2_Widget/ooo.png')
btn.setIcon(icon)
# 1.1 设置图标大小
size = QSize(20, 20)  # 若图标大小大于按钮大小会把按钮撑大
btn.setIconSize(size)

print(btn.icon())
print(btn.iconSize())

window.show()

sys.exit(app.exec_())