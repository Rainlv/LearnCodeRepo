from PyQt5.Qt import *


class SB(QSpinBox):
    # 格式化输出的字符
    def textFromValue(self, p_int):
        print(p_int)  # p_int是框内原本应该输出的字符
        return str(p_int) + '*' + str(p_int)  # 格式化数值输出，不影响前后缀，会自动添加显示


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = SB(self)
        sb.move(100, 100)
        sb.resize(100, 25)
        self.sb = sb

        self.api()

        btn = QPushButton('按钮', self)
        btn.move(150, 150)
        btn.clicked.connect(self.func_btn)

    def api(self):
        # 信号
        self.sb.valueChanged.connect(lambda val: print(type(val), val))  # 返回整型数据，只返回相应数值
        self.sb.valueChanged[str].connect(lambda val: print((type(val), val)))  # 返回str，返回文本框内的所有内容

        # 前后缀设置
        # 1.1 后缀
        self.sb.setSuffix('月')
        print(self.sb.suffix())
        # 1.2 前缀
        self.sb.setPrefix('周')
        print(self.sb.prefix())

        # 最小值对应的特殊文本（不会应用前后缀）
        self.sb.setSpecialValueText('周日')  # 显示就是周日，没有前后缀

        # 设置步长
        self.sb.setSingleStep(3)
        print(self.sb.singleStep())

        # 数值循环（数字最小后变为最大）
        self.sb.setWrapping(True)
        self.sb.wrapping().__repr__()

        # return

        # 设置最大最小值（默认0-100）
        # 1.1 最大值
        self.sb.setMaximum(180)
        print(self.sb.maximum())
        # 1.2 最小值
        self.sb.setMinimum(18)
        print(self.sb.minimum())
        # 范围设置
        # self.sb.setRange(18, 180)

        return
        # 显示的进制设置
        self.sb.setDisplayIntegerBase(2)
        print(self.sb.displayIntegerBase())

    def func_btn(self):
        # 设置数值
        self.sb.setValue(66)  # 设置的数字会保留前后缀，显示效果为 周66月。超过范围会设定为最大值
        # 获取数值
        print(self.sb.value())  # 只显示数值，无前后缀
        print(self.sb.text())  # 显示文本框内的完整内容，包括前后缀


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
