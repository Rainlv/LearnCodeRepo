from PyQt5.Qt import *


class Btn(QPushButton):
    # 声明一个信号，实现要在事件函数中发射信号，参数写信号传出参数的数据类型
    rightClicked = pyqtSignal(str)
    # rightClicked = pyqtSignal([str], [int])  # 发射字符串或int数据
    # rightClicked = pyqtSignal([str], [int, str])  # 发射字符串或int+str数据

    def mousePressEvent(self, evt):
        super(Btn, self).mousePressEvent(evt)
        
        if evt.button() == Qt.RightButton:
            print('右击按钮了')
            # 发射自定义信号,参数写发射信号时传出的参数
            self.rightClicked.emit(self.text())

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自定义信号")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = Btn('按钮', self)
        btn.rightClicked.connect(lambda x: print('槽函数触发', x))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
