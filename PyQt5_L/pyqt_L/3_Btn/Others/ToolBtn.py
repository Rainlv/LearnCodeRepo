from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("ToolBtn")
window.resize(500, 500)

btn = QToolButton(window)
# 1. 图标文本设置
# 当文本和图标都设置时，默认只显示图标
btn.setText('工具')
btn.setIcon(QIcon('../../2_Widget/ooo.png'))
btn.setIconSize(QSize(30, 30))
# 要想同时显示文本和图标要设置setToolButtonStyle属性
'''
    Qt.ToolButtonFollowStyle 遵循风格
    Qt.ToolButtonIconOnly  仅显示图标
    Qt.ToolButtonTextOnly  仅显示文本
    Qt.ToolButtonTextBesideIcon  文本显示在图标右边
    Qt.ToolButtonTextUnderIcon  文本显示在图标下面
'''
btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
print('图标类型', btn.toolButtonStyle())

# 2. 箭头设置
# 既设置了箭头又设置了图标会优先显示箭头
'''
    Qt.LeftArrow
    Qt.RightArrow
    Qt.UpArrow
    Qt.DownArrow
    Qt.NoArrow
'''
btn.setArrowType(Qt.NoArrow)
print('箭头类型', btn.arrowType())

# 3. 自动提升
btn.setAutoRaise(True)  # 鼠标悬停会有样式

# 4. ToolBtn的菜单
# 4.1 创建菜单
menu = QMenu(btn)
sub_menu = QMenu(menu)

sub_menu.setTitle('子菜单')

new_action = QAction('新建')
new_action.setData({'新建按钮': 1})
file_action = QAction('最近打开')
file_action.triggered.connect(lambda: print('最近打开被点击了'))
file_action.setData('这个是最近打开按钮哦')

menu.addAction(new_action)
sub_menu.addAction(file_action)
menu.addMenu(sub_menu)

# 4.2 设置菜单展示方法
'''
    QToolButton.DelayedPopup 鼠标按住一会后会显示
    QToolButton.MenuButtonPopup 菜单会有一个专门的小箭头放在按钮旁边，点击小箭头才显示
    QToolButton.InstantPopup 点击按钮显示菜单（不会触发click信号的发射）
'''
btn.setPopupMode(QToolButton.InstantPopup)
print('菜单弹出模式', btn.popupMode())

# 5. 信号triggered
# 点击菜单内的行为会触发，会传入一个行为对象本身
# 可以通过这个信号配合QAction.setData()来统一管理菜单内的行为
def cao(action):
    print(action.data())


btn.triggered.connect(cao)

btn.setMenu(menu)

window.show()

sys.exit(app.exec_())
