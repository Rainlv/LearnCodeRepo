from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("RaidoBtn_BtnGroup")
window.resize(500, 500)

r_male = QRadioButton('男', window)
r_female = QRadioButton('女', window)
r_male.move(100, 100)
r_female.move(100, 150)
# 1. 创建分组
sex_group = QButtonGroup(window)
# 2. 分组中添加按钮（和其id）.id是int类型
sex_group.addButton(r_male, 1)
sex_group.addButton(r_female, 2)
# 3. 将按钮对象从组中移除
# sex_group.removeButton(r_female)
r_male.setChecked(True)

print(sex_group.buttons())  # 获取按钮组下的所有按钮对象
print(sex_group.button(2))  # 获取组内的某个id的按钮对象，没有返回none
print(sex_group.checkedButton())  # 获取组内被选中的按钮对象，若没有则返回none

r_yes = QRadioButton('是', window)
r_no = QRadioButton('否', window)
r_yes.move(300, 100)
r_no.move(300, 150)
answer_group = QButtonGroup(window)
answer_group.addButton(r_yes)
answer_group.addButton(r_no)
# 1. 设置id
answer_group.setId(r_yes, 1)
answer_group.setId(r_no, 2)
# 2. 获取id
print(answer_group.id(r_yes))
# 2.1 获取选中按钮id，没有选中的按钮则返回-1
# r_no.setChecked(True)
print(answer_group.checkedId())
# 3. 设置组内排他性
answer_group.setExclusive(False)
print(answer_group.exclusive())  # 获取排他性

print(answer_group.checkedButton())


# *********信号发射**********


def obj_cao(val):
    print(val)
    print(sex_group.id(val))


def id_cao(val):
    print(val)


# 传递的参数是按钮对象
sex_group.buttonToggled.connect(obj_cao)
# 传递的参数是按钮id
answer_group.buttonClicked[int].connect(id_cao)

window.show()

sys.exit(app.exec_())
