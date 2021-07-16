from PyQt5.Qt import *

'''
验证器流程：
    1. 文本框在写入的数据时，会传入验证器的validate方法中验证有效性，有效则显示，无效则不显示
    2. 结束编辑后，对文本框中的文本进行验证，若文本有效，则结束流程；无效，触发fixup方法，在其中对无效文本进行处理后在文本框中输出处理后结果（结果也要符合验证，否则不显示）
'''


# QValidator是一个抽象类，要子类化
class Age(QValidator):
    def validate(self, input_str, pos_int):  # input_str是输入文本框的值，pos_int是光标的位置
        print(input_str, pos_int)
        try:
            if 18 <= int(input_str) <= 180:
                return QValidator.Acceptable, input_str, pos_int  # 返回一个元组（数据是否有效，文本框中的文本，光标位置）
            if 1 <= int(input_str) <= 17:
                return QValidator.Intermediate, input_str, pos_int
            else:
                return QValidator.Invalid, input_str, pos_int
        except:
            if len(input_str) == 0:
                return QValidator.Intermediate, input_str, pos_int
            return QValidator.Invalid, input_str, pos_int

    def fixup(self, p_str):
        print('xxx', p_str)
        try:
            if int(p_str) < 18:
                return '无效'
            return '180'
        except:
            if len(p_str) == 0:
                return ''
            return '18'


class MyInt(QIntValidator):
    def fixup(self, p_str):
        # if int(p_str) < 18 or len(p_str) == 0:  # ×，会先执行or前的函数，当为空字符会报错
        if len(p_str) == 0 or int(p_str) < 18:  # 会先执行or前的函数，若为True，会跳过后面的函数
            return '18'


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("验证器学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(150, 150)
        le2 = QLineEdit(self)
        le2.move(150, 200)
        # 1. 创建验证器
        # 2.1 自定义验证器
        # validator = Age()
        # 2.2 系统定义的子类验证器(fixup方法需要自己重写)
        """
            QIntValidator(parent: QObject = None)
            QIntValidator(int, int, parent: QObject = None)  传一个下限，一个上限
        """
        validator = MyInt(18, 180)
        # 2. 添加验证器
        le.setValidator(validator)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
