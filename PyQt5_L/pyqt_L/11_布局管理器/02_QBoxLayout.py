from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QBoxLayout")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 0. 初始化子控件
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label4 = QLabel('标签4')
        label1.setStyleSheet('background-color:cyan')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:red')
        label4.setStyleSheet('background-color:purple')
        # 1. 创建一个布局管理器对象
        layout = QBoxLayout(QBoxLayout.LeftToRight)  # 传一个方向参数
        # 2. 给父控件设置布局对象
        self.setLayout(layout)
        # 3. 把父控件中的子控件添加到布局中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        # layout.addWidget(label4)
        # 3.1 插入控件
        layout.insertWidget(1, label4)  # 参数：索引位置，控件

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
