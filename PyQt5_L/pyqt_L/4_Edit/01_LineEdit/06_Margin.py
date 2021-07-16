from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("文本边距和对齐方式设置")
window.resize(500, 500)

le = QLineEdit(window)
le.move(100, 100)
le.resize(300, 300)
# 边距设置
le.setTextMargins(50, 70, 80, 20)  # 左上右下
print(le.getTextMargins())
# 对齐方式设置
'''
水平：
    Qt.AlignRight
            Left
            HCenter
            Justify
垂直：
    Qt.AlignBottom
            Top
            VCenter
            Baseline
Qt.AlignCenter  垂直水平都居中
            
'''
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)  # 设置水平和垂直对齐方式，或运算连接
print(le.alignment())  # 获取对齐方式


window.show()

sys.exit(app.exec_())
