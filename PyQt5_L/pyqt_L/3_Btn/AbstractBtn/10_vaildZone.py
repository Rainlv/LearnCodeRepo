from PyQt5.Qt import *  # 包含一些常用类的汇总
import sys


class Btn(QPushButton):
    def hitButton(self, point):
        # 点击按钮的右半边区域有效
        # if point.x() > self.width() // 2:
        #     return True  # 点击有效
        # else:
        #     return False

        # 点击内切圆内有效，边缘无效
        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        import math
        distance = math.sqrt(math.pow(hit_x - yuanxin_x, 2) + math.pow(hit_y - yuanxin_y, 2))

        # 如果距离小于半径，True
        if distance < self.width() / 2:
            return True
        return False

    def paintEvent(self, QPaintEvent):
        super(Btn, self).paintEvent(QPaintEvent)
        painter = QPainter(self)
        pen = QPen(QColor(100, 150, 200), 6)
        painter.setPen(pen)

        painter.drawEllipse(self.rect())


app = QApplication(sys.argv)  # sys.argv接受外部参数

window = QWidget()

window.setWindowTitle("有效区域")
window.resize(500, 500)

btn = Btn(window)
btn.move(100, 100)
btn.resize(200, 200)
btn.setText('按钮')
btn.pressed.connect(lambda: print('按钮被点击'))

window.show()

sys.exit(app.exec_())