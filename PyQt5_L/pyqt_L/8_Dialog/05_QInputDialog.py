from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入对话框")
        self.resize(500, 500)
        self.setup_ui()
        # self.static_func()

    def setup_ui(self):
        # 初始化
        input_d = QInputDialog(self, Qt.FramelessWindowHint)
        # 输入模式
        '''
            DoubleInput = 2
            IntInput = 1
            TextInput = 0   
        '''
        # input_d.setInputMode(QInputDialog.IntInput)
        # 界面元素设置
        input_d.setLabelText('标签内容')
        input_d.setOkButtonText('okkkk')
        input_d.setCancelButtonText('不搞了')
        # 小分类设置
        # 1. 整型
        input_d.setIntMaximum(10000)
        input_d.setIntMinimum(1)
        # input_d.setIntRange(1, 10000000)
        input_d.setIntStep(5)
        input_d.setIntValue(555)
        # 2. 浮点型
        input_d.setDoubleDecimals(2)
        input_d.setDoubleStep(0.5)
        # 3. 字符串
        input_d.setTextEchoMode(QLineEdit.Password)
        # 4. 下拉列表，输入模式要用字符串
        # input_d.setOption(QInputDialog.UseListViewForComboBoxItems)  # 下拉列表展示样式
        # input_d.setInputMode(QInputDialog.TextInput)
        input_d.setInputMode(QInputDialog.IntInput)

        input_d.setComboBoxItems(['1', '56', '8945'])
        input_d.setComboBoxEditable(True)

        # 信号，以int类型为例，其他都相同
        input_d.intValueChanged.connect(lambda val: print('整型数据改变', val))
        input_d.intValueSelected.connect(lambda val: print('整形数据最终被选中', val))

        input_d.show()

    def static_func(self):

        # 参数：父控件，窗口标题，标签内容，[默认值，最小值，最大值，步长]
        # result = QInputDialog.getInt(self, '窗口标题', '标签内容', 888, step=8)
        # 返回元组：（当前数据，点击了确定/取消返回T/F）

        # 参数：父控件，窗口标题，标签内容，[默认值，最小值，最大值，小数位数]
        # result = QInputDialog.getDouble(self, '窗口标题', '标签内容', 888.88, decimals=2)

        # 参数：父控件，窗口标题，标签内容，[显示方式（明文，密文），默认值]
        # result = QInputDialog.getText(self, '窗口标题', '标签内容', text='默认字符', echo=QLineEdit.Password)

        # 参数：父控件，窗口标题，标签内容，[默认值]
        # result = QInputDialog.getMultiLineText(self, '窗口标题', '标签内容', text='默认字符')

        # 参数：父控件，窗口标题，标签内容，[条目项（列表），默认条目索引，是否可编辑]
        result = QInputDialog.getItem(self, '窗口标题', '标签内容', ['1', '2', '3'], 2, True)
        print(result)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
