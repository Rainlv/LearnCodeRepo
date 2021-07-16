from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("菜单设置")
window.resize(500, 500)

btn = QPushButton('文件', window)
# 1. 创建菜单对象
"""
QMenu(parent: QWidget = None)
QMenu(str, parent: QWidget = None)
"""
menu = QMenu(window)
# 1.1 创建子菜单对象
open_recent_menu = QMenu('最近打开', menu)
# 2. 创建菜单内的行为对象
"""
    QAction(parent: QObject = None)
    QAction(str, parent: QObject = None)
    QAction(QIcon, str, parent: QObject = None)
"""
new_action = QAction(QIcon('../../2_Widget/xxx.png'), '新建')
# new_action.setText('新建')
# new_action.setIcon(QIcon('../../2_Widget/xxx.png'))
new_action.triggered.connect(lambda: print('新建文件'))  # 菜单内行为对象被点击时

open_action = QAction(QIcon('../../2_Widget/xxx.png'), '打开')
open_action.triggered.connect(lambda: print('打开文件'))  # 菜单内行为对象被点击时

exit_action = QAction('退出')
exit_action.triggered.connect(lambda: print('退出程序'))  # 菜单内行为对象被点击时

# 2.1 创建子菜单中行为对象
file_action = QAction('Python')
# 3. 给菜单对象添加行为
menu.addAction(new_action)
menu.addAction(open_action)
# 3.1 给子菜单添加行为
menu.addMenu(open_recent_menu)
# 3.2 添加分割线
menu.addSeparator()

menu.addAction(exit_action)

# 3.3 主菜单中添加子菜单
open_recent_menu.addAction(file_action)

# 4. 给按钮对象设置菜单
btn.setMenu(menu)
print(btn.menu())  # 获取菜单对象

window.show()
btn.showMenu()  # 展示菜单


sys.exit(app.exec_())
