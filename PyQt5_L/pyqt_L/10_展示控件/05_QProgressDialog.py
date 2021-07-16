from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("进度对话框")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 初始化
        # pd = QProgressDialog('标签内容', '按钮文本', 0, 100, self)
        pd = QProgressDialog(self)
        pd.setLabelText('标签')
        pd.setCancelButtonText('取消按钮')
        pd.setWindowTitle('进度')

        # 子控件设置
        # pd.setBar(QProgressBar)
        # pd.setCancelButton(QPushButton)
        # pd.setLabel(QLabel)

        pd.setAutoClose(False)  # 设置进度100后自动关闭，
                                # 触发，自动重置必须为True，达到100%
        pd.setAutoReset(False)  # 设置100后重置进度

        pd.setValue(50)

        # 弹出进度条对话框（不设置也会自动弹，有弹出延迟）
        # pd.setMinimumDuration(0)
        pd.open(lambda: print('进度条被关闭'))  # 槽函数在对话框被关闭触发

        pd.canceled.connect(lambda: print('取消了'))

        print(pd.wasCanceled())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
