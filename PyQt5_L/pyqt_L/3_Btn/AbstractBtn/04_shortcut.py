from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

#  1. 创建一个应用程序对象
app = QApplication(sys.argv)  # sys.argv接受外部参数

#  2. 控件的操作
#  2.1 创建控件
window = QWidget()
#  2.2 设置控件
window.setWindowTitle("快捷键设置")
window.resize(500, 500)

btn = QPushButton(window)
# 在按钮文本前加上&，设定快捷键为alt+&后的字符
# btn.setText('&abcd')  # alt+a
# btn.setText('a&da')  # alt+d
# 在文本非字母情况可手动设置快捷键
btn.setText('按钮')
btn.setShortcut('Alt+c')
btn.pressed.connect(lambda: print('按钮按下了'))

#  2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
