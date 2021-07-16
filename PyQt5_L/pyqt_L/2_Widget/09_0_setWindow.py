from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.resize(500, 500)


# 设置窗口标题名称
window.setWindowTitle("顶层窗口设置")
print(window.windowTitle())  # 获取窗口标题文本

# 设置窗口图标
icon = QIcon('ooo.png')
window.setWindowIcon(icon)
print(window.windowIcon())  # 获取窗口图标对象

# 设置窗口不透明度
window.setWindowOpacity(0.9)
print(window.windowOpacity())  # 获取窗口不透明度

# 窗口大小状态
print(window.windowState() == Qt.WindowNoState)  # 窗口状态是否处于默认状态（无状态）
# window.setWindowState(Qt.WindowMinimized)  # 设置窗口最小化
# window.setWindowState(Qt.WindowFullScreen)  # 设置窗口全屏
print(window.windowState() == Qt.WindowNoState)  # 窗口状态是否处于默认状态（无状态）

# 多窗口情况
#   创建额外的窗口
w2 = QWidget()
w2.setWindowTitle('w2')



#  2.3 展示控件
window.show()
w2.show()
window.setWindowState(Qt.WindowActive)  # 设置窗口活跃，置顶窗口

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
