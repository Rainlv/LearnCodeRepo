from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("错误消息框")
        self.resize(500, 500)
        # self.setup_ui()

    def setup_ui(self):
        em = QErrorMessage(self)

        em.setWindowTitle('错误信息')

        # 显示信息，以非模态窗口
        em.showMessage('相同错误信息')
        em.showMessage('相同错误信息')
        em.showMessage('相同错误信息')
        em.showMessage('不同信息')

        # 手动设置为模态窗口
        em.open()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    # 静态方法
    QErrorMessage.qtHandler()
    qDebug('xxx')  # 调试信息
    qWarning('warn')  # 警告信息

    sys.exit(app.exec_())
