from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("按钮状态")
window.resize(500, 500)

# 初始化对象
btn = QPushButton(window)
btn.resize(80, 40)
btn.setText('控制按钮')

p_btn = QPushButton(window)
p_btn.move(200, 100)
p_btn.setText('这是一个按钮')
p_btn.setStyleSheet('QPushButton:pressed {background-color:red;}')

radio_btn = QRadioButton(window)
radio_btn.move(200, 150)
radio_btn.setText('这是一个单选按钮')

check_btn = QCheckBox(window)
check_btn.move(200, 200)
check_btn.setText('这是一个复选按钮')

# 按钮状态设置
# 1. 按下按钮状态
# p_btn.setDown(True)
# radio_btn.setDown(True)
# check_btn.setDown(True)
# print(btn.isDown())
# 2. 选中按钮状态
# QPushButton默认是不可选中的，要设置
# 2.1 设置是否可选中
p_btn.setCheckable(True)
print(p_btn.isCheckable())
# 2.2 选中按钮
p_btn.setChecked(True)
radio_btn.setChecked(True)
check_btn.setChecked(True)
print(p_btn.isChecked())
# 2.3 切换选中状态
def cao():
    p_btn.toggle()
    check_btn.toggle()
    radio_btn.toggle()
btn.pressed.connect(cao)
# 2.4 按钮是否可用
# 不可以时不能通过鼠标键盘正常交互，但可以通过代码控制
p_btn.setEnabled(False)
radio_btn.setEnabled(False)
check_btn.setEnabled(False)
print(p_btn.isEnabled())


window.show()

sys.exit(app.exec_())
