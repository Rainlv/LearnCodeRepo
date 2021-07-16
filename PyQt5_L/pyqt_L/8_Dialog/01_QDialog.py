from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("对话框父类")
window.resize(500, 500)

d = QDialog(window)
d.setWindowTitle('对话框')

btn = QPushButton('111', d)
btn.move(60, 30)
btn.clicked.connect(lambda: d.accept())  # 关闭窗口，返回1

btn1 = QPushButton('222', d)
btn1.move(60, 70)
btn1.clicked.connect(lambda: d.reject())  # 关闭窗口，返回0

btn3 = QPushButton('333', d)
btn3.move(60, 110)
btn3.clicked.connect(lambda: d.done(5))  # 关闭窗口，返回参数（int类型）

btn4 = QPushButton('444', d)
btn4.move(60, 150)
btn4.clicked.connect(lambda: d.setResult(456))  # 设置一个结果值

btn5 = QPushButton('555', d)
btn5.move(60, 190)
btn5.clicked.connect(lambda: print(d.result()))  # 获取结果值

# 0. 信号
d.accepted.connect(lambda: print('点击了接收按钮'))
d.rejected.connect(lambda: print('点击了拒绝按钮'))  # 点×关闭窗口也会触发
d.finished.connect(lambda val: print('结束', val))  # 接收或者拒绝按钮被点击也会触发，返回的是相应返回值


# 1. 模态与非模态
# 1.1 模态
# 1.1.0 应用程序级别
# 只有关闭后才能访问其他窗口
# d.exec()
# 1.1.1 窗口级别
# 会阻塞关联窗口
# d.open()
# 1.2 非模态--show()
# 不会阻塞与其他窗口的交互
# 1.2.0 非模态转换为模态，两种都是转换为窗口级别
# d.setModal(True)
# d.setWindowModality(Qt.WindowModal)


# 2. 是否显示尺寸调整控件
# 就是右下角拖拽控制
d.setSizeGripEnabled(True)

# d.show()

print(d.exec())

window.show()

sys.exit(app.exec_())