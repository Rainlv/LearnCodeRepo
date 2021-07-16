from PyQt5.Qt import *


class MyASB(QAbstractSpinBox):
    # 设置步长调节器是否可用
    def __init__(self, parent=None):
        super(MyASB, self).__init__(parent)
        self.lineEdit().setText('0')

    def stepEnabled(self):
        # 0-9
        # current_num = int(self.text())
        # if current_num == 0:
        #     return QAbstractSpinBox.StepUpEnabled  # 向上可用
        # elif current_num == 9:
        #     return QAbstractSpinBox.StepDownEnabled  # 向下可用
        # elif current_num < 0 or current_num > 9:
        #     return QAbstractSpinBox.StepNone  # 都不可用
        # else:
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled  # 向上向下都可用

    def stepBy(self, p_int):
        # p_int 在点↑时为1，↓时为-1
        current_num = int(self.text()) + p_int
        # 没有直接设置文本的功能，要先获取文本框对象，再设置文本
        self.lineEdit().setText(str(current_num))

    # 通过下面两个函数实现文本框内内容验证
    # def validate(self, p_str, p_int):
    #     pass
    #
    # def fixup(self, p_str):
    #     pass


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AbstractSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 抽象类中步长调节功能没有实现，要自己定义
        asb = MyASB(self)
        self.asb = asb
        asb.move(100, 100)
        asb.resize(100, 30)

        # 长按↑↓箭头加速数据变化
        asb.setAccelerated(True)
        print(asb.isAccelerated())

        # 只读设置，只能通过步长调节器调节
        # asb.setReadOnly(True)
        print(asb.isReadOnly())

        # 获取文本框对象，进行一系列设置
        le = asb.lineEdit()
        cl = QCompleter(['adas', '123', '18'], self.asb)
        le.setCompleter(cl)
        le.setText('10')
        # 对齐方式设置
        # le.setAlignment(Qt.AlignHCenter)
        asb.setAlignment(Qt.AlignRight)

        # 周边框架（默认有）
        asb.setFrame(False)
        print(asb.hasFrame())

        # 清空文本
        # asb.clear()

        # 设置上下按钮样式
        '''
            UpDownArrows = 0
            NoButtons = 2
            PlusMinus = 1
        '''
        asb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        print(asb.buttonSymbols())

        # 信号
        asb.editingFinished.connect(lambda: print('结束编辑'))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
