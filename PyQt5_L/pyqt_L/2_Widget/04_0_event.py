from PyQt5.Qt import *

# 事件转发机制，若子控件没有定义相关的事件方法，会默认从父控件中调用
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件机制")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass

    def showEvent(self, QShowEvent):
        print('窗口展示')

    def closeEvent(self, QCloseEvent):
        print('窗口关闭')

    def moveEvent(self, QMoveEvent):
        print('窗口移动')

    def resizeEvent(self, QResizeEvent):
        print('窗口尺寸改变')

    def enterEvent(self, QEvent):
        print('鼠标进入')
        self.setStyleSheet('background-color:cyan')

    def leaveEvent(self, QEvent):
        print('鼠标离开')
        self.setStyleSheet('background-color:green')

    def mousePressEvent(self, QMouseEvent):
        print('鼠标按下')

    def mouseReleaseEvent(self, QMouseEvent):
        print('鼠标释放')

    def mouseDoubleClickEvent(self, QMouseEvent):
        print('鼠标双击')

    def mouseMoveEvent(self, QMouseEvent):
        print('鼠标移动')

    def keyPressEvent(self, QKeyEvent):
        print('键盘有按键被按下')

    def keyReleaseEvent(self, QKeyEvent):
        print('键盘有按键被释放')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())