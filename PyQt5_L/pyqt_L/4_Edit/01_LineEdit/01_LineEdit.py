from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("QLineEdit")
window.resize(500, 500)
# QLineEdit是单行纯文本，无法换行，不能插入图片等富文本

# 1. 初始化
# le = QLineEdit(window)
# 1.1 提前输入默认文本
# le.setText('默认输入的文本')
le = QLineEdit('默认输入的文本', window)  # 初始化并提前输入文本
le.move(200, 150)
# 2. 插入文本
btn = QPushButton('insert', window)
btn.move(200, 200)
btn.pressed.connect(lambda: le.insert('inserted_text'))
btn1 = QPushButton('text', window)
# 3. 获取真实文本内容
btn1.move(200, 230)
btn1.pressed.connect(lambda: print(le.text()))
# 4. 获取用户看到的文本内容
btn2 = QPushButton('display', window)
btn2.move(200, 260)
btn2.pressed.connect(lambda: print(le.displayText()))
# 5. 设置输出模式
le2 = QLineEdit(window)
le2.move(200, 175)
'''
    NoEcho = 1  文本框内不展示输入内容
    Normal = 0  明文显示
    Password = 2  密文显示
    PasswordEchoOnEdit = 3  编辑时明文，编辑结束（焦点转移）密文
'''
le2.setEchoMode(QLineEdit.Password)
print(le2.echoMode())
btn3 = QPushButton('text2', window)
btn3.move(200, 290)
btn3.clicked.connect(lambda: print(le2.text(), le2.displayText()))
# 6. 占位提示文本
le.setPlaceholderText('请输入账号')
le2.setPlaceholderText('请输入密码')
print(le.placeholderText())
# 7. 清空按钮设置
le2.setClearButtonEnabled(True)  # 会出现一个×，在文本框末尾，点击会清空输入
# 8. 自定义Action添加，以显示隐藏文本为例
action = QAction(le2)
action.setIcon(QIcon('close.png'))
"""
    addAction(self, QAction)
    addAction(self, QAction, QLineEdit.ActionPosition)
    addAction(self, QIcon, QLineEdit.ActionPosition) -> QAction
"""
'''
    LeadingPosition = 0  显示在文本框前面
    TrailingPosition = 1  显示在文本框最后
'''
le2.addAction(action, QLineEdit.TrailingPosition)

def change_state():
    if le2.echoMode() == QLineEdit.Normal:
        action.setIcon(QIcon('close.png'))
        le2.setEchoMode(QLineEdit.Password)

    elif le2.echoMode() == QLineEdit.Password:
        action.setIcon(QIcon('open.png'))
        le2.setEchoMode(QLineEdit.Normal)


action.triggered.connect(change_state)
# 9. 文本自动补全
# 9.1 创建一个完成器对象
"""
    QCompleter(parent: QObject = None)
    QCompleter(QAbstractItemModel, parent: QObject = None)
    QCompleter(Iterable[str], parent: QObject = None)
    """
complete = QCompleter(['wxh', 'wahaha', '6102'])  # 里面传入待选项
# 9.2 给指定文本框添加完成器
le.setCompleter(complete)
# 10. 限制条件设置
le3 = QLineEdit(window)
le3.move(200, 120)
# 10.1 设置最大长度
le3.setMaxLength(3)
print(le3.maxLength())
# 10.2 设置只读，但可以代码写入
le3.setReadOnly(True)
le3.setText('代码写入的只读文本')  # 只显示前三个文本


window.show()

sys.exit(app.exec_())
