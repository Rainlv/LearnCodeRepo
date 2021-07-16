from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("装饰器连接信号与槽")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton('按钮', self)
        btn.setObjectName('btn')
        btn.resize(200, 210)
        btn.move(100, 100)

        btn2 = QPushButton('按钮2', self)
        btn2.setObjectName('btn2')
        btn2.resize(100, 300)

        # 将指定控件的子孙控件连接槽函数
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot(bool)  # 传递的参数数据类型
    def on_btn_clicked(self, val):  # 函数名：on_要连接信号的控件名_信号名称。  参数是传递的参数
        print('按钮被点击了', val)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
