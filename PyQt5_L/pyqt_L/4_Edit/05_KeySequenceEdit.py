from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 获取键盘输入
        kse = QKeySequenceEdit(self)
        """
        QKeySequence()
        QKeySequence(Union[QKeySequence, QKeySequence.StandardKey, str, int])
        QKeySequence(str, format: QKeySequence.SequenceFormat = QKeySequence.NativeText)
        QKeySequence(int, key2: int = 0, key3: int = 0, key4: int = 0)
        QKeySequence(Any)
        """
        # ks = QKeySequence('Ctrl+C')
        # ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_S, Qt.CTRL + Qt.Key_D)
        kse.setKeySequence(ks)
        # kse.clear()  # 清空框

        btn = QPushButton('测试按钮', self)
        btn.move(100, 100)
        # 返回框内的文本和个数
        btn.clicked.connect(lambda: print(kse.keySequence().toString(), kse.keySequence().count()))

        # 信号
        # 结束编辑时
        kse.editingFinished.connect(lambda: print('结束编辑'))
        # 键位序列改变时，会传出一个QKeySequence对象
        kse.keySequenceChanged.connect(lambda key_val: print('键位序列发生改变', key_val.toString()))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
