from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("颜色选择对话框")
        self.resize(500, 500)
        self.static_func()
        # self.setup_ui()

    def setup_ui(self):
        btn = QPushButton('选择颜色', self)
        btn.move(100, 100)
        btn.clicked.connect(lambda: cd.open(color_func))

        # 初始化
        # cd = QColorDialog(self)
        cd = QColorDialog(QColor(100, 200, 150), self)  # 设置初始选中颜色

        # 信号
        def color_sel(color):
            # 直接用setStyleSheet会给子控件也设置背景色
            palette = QPalette()
            palette.setColor(QPalette.Background, color)  # 给窗口背景设置颜色
            self.setPalette(palette)

        def color_func():
            # 直接用setStyleSheet会给子控件也设置背景色
            palette = QPalette()
            palette.setColor(QPalette.Background, cd.selectedColor())  # 给窗口背景设置颜色
            self.setPalette(palette)

        # cd.colorSelected.connect(color_sel)

        # if cd.exec():
        #     color_func()

        # 可选项设置
        '''
            DontUseNativeDialog = 4 使用Qt的标准颜色对话框而不是系统原生颜色选择对话框
            NoButtons = 2  
            ShowAlphaChannel = 1  显示透明度选择框
        '''
        cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        cd.setOption(QColorDialog.NoButtons, on=False)

    def static_func(self):
        # 静态方法

        # 自定义颜色数目
        print(QColorDialog.customCount())
        # 设置自定义颜色
        QColorDialog.setCustomColor(1, QColor(255, 0, 0))  # 第一个参数是索引位置，第二个是颜色
        # 设置标准颜色
        QColorDialog.setStandardColor(1, QColor(0, 255, 255))  # 第一个参数是索引位置，第二个是颜色
        # 获取自定义颜色
        print(QColorDialog.customColor(1))  # 获取索引位置的自定义颜色
        # 获取标准颜色
        print(QColorDialog.standardColor(1))  # 获取索引位置的自定义颜色

        """ getColor(initial: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white, parent: QWidget = None, title: str = '', options: Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption] = QColorDialog.ColorDialogOptions()) -> QColor """
        # 点确定返回选中颜色，点取消返回黑色

        btn = QPushButton('按钮', self)
        btn.move(100, 100)

        def color():
            result = QColorDialog.getColor(QColor(255, 0, 0), self, '选择颜色')
            palette = QPalette()
            palette.setColor(QPalette.Background, result)  # 给窗口背景设置颜色
            self.setPalette(palette)

        btn.clicked.connect(color)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
