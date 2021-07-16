from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("案例")
        self.resize(500, 500)
        self.setup_ui()


    def setup_ui(self):
        # 创建复选框
        for i in range(30):
            cb = QCheckBox(self)
            cb.setText('{}'.format(i))
            cb.move(10 + i % 4 * 50, 10 + i // 4 * 60)

        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, evt):
        self.pos_origin = evt.pos()
        #
        self.rb.setGeometry(QRect(self.pos_origin, QSize()))

        self.rb.show()

    def mouseMoveEvent(self, evt):
        self.rb.setGeometry(QRect(self.pos_origin, evt.pos()).normalized())
        # normalized作用是保证长宽为正数
        # normalized()保证反向拖动不会bug

    def mouseReleaseEvent(self, evt):
        rect = self.rb.geometry()
        for child in self.children():
            # 判定控件是否在橡皮筋控件内部
            if rect.contains(child.geometry()) and child.inherits('QCheckBox'):
                child.toggle()  # 切换选中状态
        self.rb.hide()




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
