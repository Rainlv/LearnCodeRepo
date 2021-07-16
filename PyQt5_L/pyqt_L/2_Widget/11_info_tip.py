from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QMainWindow()
window.statusBar()  # 任务栏创建
window.setWindowFlags(Qt.WindowContextHelpButtonHint)  # 带help的窗口
#  2.2 设置控件
window.setWindowTitle("信息提示")
window.resize(500, 500)
window.setStatusTip('这是窗口')

label = QLabel(window)
label.setText('标签')
label.move(200, 200)
# 设置状态栏消息
label.setStatusTip('这是标签')
print(label.statusTip())
# 设置提示消息（鼠标悬停）
label.setToolTip('这是一个提示标签')
print(label.toolTip())
label.setToolTipDuration(2000)  # 设置提示标签持续时间
print(label.toolTipDuration())
# 设置帮助信息（鼠标在help模式下点击显示）
label.setWhatsThis('这是啥？这是标签')
print(label.whatsThis())

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
