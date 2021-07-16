from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys

app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("QFrame学习")
window.resize(500, 500)

frame = QFrame(window)
frame.resize(200, 200)
frame.move(100, 100)
frame.setStyleSheet('background-color:cyan;')

# 0. 设置 形状+阴影
'''
相当于同时设置了setFrameShape和setFrameShadow。
要用或运算连接 
'''
# frame.setFrameStyle(QFrame.Box | QFrame.Raised)

# 1. 设置形状
'''
    QFrame.Box 围绕内容绘制一个框
    QFrame.Panel 绘制一个面板，使内容凸起或凹陷
    QFrame.HLine 绘制一条没有框架的水平线（用作分隔符）
    QFrame.VLine 绘制一条无框架的垂直线（用作分隔符）
    QFrame.StyledPanel 绘制一个矩形面板，其外观取决于当前的GUI样式
    QFrame.WinPanel 建议使用StyledPanel
'''
frame.setFrameShape(QFrame.Box)
# 2. 设置阴影——营造立体效果
'''
    QFrame.Plain 与周围水平，没有3D效果
    QFrame.Raise 使用当前颜色组的浅色和深色绘制3D效果，凸起效果
    QFrame.Sunken 凹陷效果
    
'''
frame.setFrameShadow(QFrame.Raised)
# 3. 设置边线宽度
# 3.1 设置外线宽度
frame.setLineWidth(6)
# 3.2 设置中线宽度（一般设置完阴影才有，有些形状没有中线）
frame.setMidLineWidth(10)
# 3.3 框架宽度
'''
框架宽度 = 内线 + 外线 + 中线
其中，内线宽度 = 外线宽度
'''
print(frame.frameWidth())
# 4. 设置矩形框架
frame.setFrameRect(QRect(20, 20, 60, 60))

window.show()

sys.exit(app.exec_())
