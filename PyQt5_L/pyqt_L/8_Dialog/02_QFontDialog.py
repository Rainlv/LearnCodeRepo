from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("字体对话框")
        self.resize(500, 500)
        self.setup_ui()
        # self.static_func()

    def setup_ui(self):
        # 0. 初始化设置
        # fd = QFontDialog(self)
        font = QFont()
        font.setFamily('幼圆')
        font.setPointSize(36)
        fd = QFontDialog(font, self)  # 添加font，可以更改默认选中字体
        # fd.setCurrentFont(font)  # 也可以通过setCurrentFont来设置
        # 0.1 可选项
        '''
            NoButtons = 1  不显示确定取消按钮
            DontUseNativeDialog = 2  在mac上使用Qt的标准字体对话框而不是Apple的原生字体面板
            ScalableFonts = 4   仅显示可缩放字体
            NonScalableFonts = 8  仅显示不可缩放自提
            MonospacedFonts = 16  仅显示等宽字体
            ProportionalFonts = 32  仅显示比例字体
        '''
        fd.setOption(QFontDialog.ScalableFonts)  # 设置一个
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.ScalableFonts)  # 设置多个
        print(fd.testOption(QFontDialog.DontUseNativeDialog))  # 测试某个选项是否生效

        btn = QPushButton('按钮', self)
        btn.move(100, 100)
        label = QLabel('测试文字', self)
        label.move(100, 200)

        # 1. 信号设置
        # 1.1 选择完字体后
        def font_sel():
            print('字体被选择', fd.selectedFont().family())  # selectedFont方法，返回选中的字体QFont
        btn.clicked.connect(lambda: fd.open(font_sel))  # 打开后连接fontSelected信号函数，但不传出参数
        fd.fontSelected.connect(lambda _font: print(_font))  # 点击确定，选择完字体后会触发该信号

        # 当前选中字体改变
        def font_set(font_):
            label.setFont(font_)
            label.adjustSize()
        fd.currentFontChanged.connect(font_set)  # 选中字体改变时触发，传出选中字体

    def static_func(self):
        # 静态方法
        """
        getFont(QFont, parent: QWidget = None, caption: str = '', options: Union[QFontDialog.FontDialogOptions, QFontDialog.FontDialogOption] = QFontDialog.FontDialogOptions()) -> Tuple[QFont, bool]
        getFont(parent: QWidget = None) -> Tuple[QFont, bool]
        """
        btn = QPushButton('字体选择', self)
        btn.move(100, 100)
        label = QLabel('测试文字', self)
        label.move(100, 200)

        font = QFont()
        font.setFamily('幼圆')
        font.setPointSize(36)

        def font_sel():
            # QFontDialog.getFont 弹出一个字体选择控件，和上面效果差不多
            # result = QFontDialog.getFont(self)
            # 返回值-> Tuple[QFont, bool]，QFont是退出前选中的字体，bool是是否点击了确定按钮
            result = QFontDialog.getFont(font, self, '窗口标题', QFontDialog.MonospacedFonts)
            # 参数: 默认字体，父控件，窗口标题，可选项设置
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()

        btn.clicked.connect(font_sel)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
