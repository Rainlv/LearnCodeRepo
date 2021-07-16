from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("cmdLinkBtn的使用")
window.resize(500, 500)

"""
    QCommandLinkButton(parent: QWidget = None)
    QCommandLinkButton(str, parent: QWidget = None)
    QCommandLinkButton(str, str, parent: QWidget = None)
"""
# 默认扁平化，有一个箭头icon
btn = QCommandLinkButton('标题', '描述', window)
btn.setText('标题2')
btn.setDescription('描述plus')
btn.setIcon(QIcon('../../2_Widget/ooo.png'))
print(btn.description())


window.show()

sys.exit(app.exec_())
