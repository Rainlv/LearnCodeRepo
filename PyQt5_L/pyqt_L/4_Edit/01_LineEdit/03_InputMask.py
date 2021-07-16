from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("掩码验证器学习")
window.resize(500, 500)

le = QLineEdit(window)
le2 = QLineEdit(window)
le.move(150, 150)
le2.move(150, 200)
# 掩码字符串写法：掩码分隔符掩码分号占位符
# 字母(大写两位)-数字(两位)
le.setInputMask('>AA-99;#')  # 输入必须符合掩码规则，不然会无法输入，大小写会自动转换
le2.setInputMask('999.999.999.999')
window.show()

sys.exit(app.exec_())