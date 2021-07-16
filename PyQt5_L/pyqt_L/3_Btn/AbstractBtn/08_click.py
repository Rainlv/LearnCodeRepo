from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("按钮点击")
window.resize(500, 500)

btn = QPushButton(window)
btn2 = QPushButton(window)
btn.setText('按钮')
btn2.setText('控制按钮')
btn.move(200, 200)
btn2.move(20, 20)

btn.pressed.connect(lambda: print('按钮被点击了'))
btn2.pressed.connect(lambda: btn.animateClick(1000))
# btn2.click()  # 按钮点击事件
# btn.animateClick(1000)  # 按钮点击事件，不过会有点击过程的效果


window.show()

sys.exit(app.exec_())
