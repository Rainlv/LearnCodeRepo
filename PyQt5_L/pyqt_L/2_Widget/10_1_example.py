from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(200, 150)
        label.hide()

        btn = QPushButton(self)
        btn.move(200, 250)
        btn.setEnabled(False)
        btn.setText('登录')

        le = QLineEdit(self)
        le.move(200, 200)

        def btn_check():
            if le.text() == 'Sz':
                label.setText('登录成功')
            else:
                label.setText('登录失败')

            label.adjustSize()
            label.show()

        def text_cao(text):
            btn.setEnabled(len(text) > 0)

        btn.pressed.connect(btn_check)
        le.textChanged.connect(text_cao)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
