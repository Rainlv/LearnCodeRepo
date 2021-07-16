from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("网格布局")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:red')

        gl.addWidget(label1, 0, 0)  # 控件，行，列位置
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 1, 2)  # 控件，起始行，起始列，占几行，占几列
        # gl.addLayout()

        # 设置
        # 1. 最小列宽，行高（拉伸到最小时的尺寸）
        gl.setColumnMinimumWidth(0, 100)  # 参数：第几行，最小尺寸
        gl.setRowMinimumHeight(0, 100)
        # 2. 拉伸系数
        gl.setColumnStretch(0, 1)
        gl.setColumnStretch(1, 0)
        gl.setRowStretch(0, 1)
        gl.setRowStretch(1, 0)
        # 3. 间距设置
        gl.setVerticalSpacing(20)
        gl.setHorizontalSpacing(30)
        # gl.setSpacing(50)  # 统一设置
        # 4. 原点角设置（原点设置）
        '''
            BottomRightCorner
            BottomLeftCorner
            TopRightCorner
            ToptomLeftCorner
        '''
        gl.setOriginCorner(Qt.BottomRightCorner)

        # 获取
        # 获取位置
        print(gl.getItemPosition(1))  # 参数代表第几个子控件，返回元组（起始行，起始列，占几行，占几列）
        # 根据行列位置获取子控件
        print(gl.itemAtPosition(0, 1).widget())
        # 行列数
        print(gl.columnCount())
        print(gl.rowCount())

        self.setLayout(gl)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
