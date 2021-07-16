from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器介绍")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 0. 初始化子控件
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:red')
        # 1. 初始化子元素
        # 可以不写父控件，之后用布局管理器添加即可
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:red')

        # 2. 创建布局管理器对象
        # v_layout = QHBoxLayout()  # 水平排列
        v_layout = QVBoxLayout()  # 垂直排列

        # 3. 往布局管理器中添加子元素
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        # 4. 布局相关设置
        v_layout.setContentsMargins(20, 10, 30, 40)  # 外边距：左上右下
        v_layout.setSpacing(60)  # 设置控件间的间距

        # 窗口设置布局
        '''
            LeftToRight
            RightToLeft
            LayoutDirectionAuto  自动排列
        '''
        self.setLayout(v_layout)
        self.setLayoutDirection(Qt.RightToLeft)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
