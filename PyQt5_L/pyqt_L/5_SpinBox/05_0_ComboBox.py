from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 一个下拉选框和单行文本的组合控件
        cb = QComboBox(self)

        btn = QPushButton('测试按钮', self)
        btn.move(100, 150)

        # 1. 添加条目项
        # 1.1 添加一条
        """
           addItem(self, str, userData: Any = None)
           addItem(self, QIcon, str, userData: Any = None)
        """
        cb.addItem('xx1')
        cb.addItem('xx2')
        # 1.2 添加一条带图标的
        cb.addItem(QIcon('../2_Widget/xxx.png'), 'xx3')
        # 1.2 添加多条
        cb.addItems(['1', '2', '3'])

        # 2. 插入条目
        # 2.1 指定位置插入一条
        cb.insertItem(1, '插入的')  # 第一个参数表示索引位置0开始
        # 2.2 插入带图标的
        cb.insertItem(1, QIcon('../2_Widget/xxx.png'), '插入的')  # 第一个参数表示索引位置0开始
        # 2.3 插入多条
        cb.insertItems(2, ['插入1', '插入2', '插入3'])

        # 3. 修改条目项
        # 3.1 修改图标
        cb.setItemIcon(0, QIcon('../2_Widget/ooo.png'))
        # 3.2 修改文本
        cb.setItemText(0, '修改的')

        # 4. 删除条目项
        cb.removeItem(10)

        # 5. 插入分割线
        cb.insertSeparator(2)

        # 6. 设置默认显示的文本
        # 6.1 索引设置
        cb.setCurrentIndex(1)
        # 6.2 文本设置，若文本不在条目中，无法匹配，默认显示为第一条
        # cb.setCurrentText('插入1')

        # 7. 编辑文本设置
        # 7.1 文本框编辑状态设置
        cb.setEditable(True)  # 文本框可编辑，编辑结束后文本内容会加入到条目项中
        # 7.2 设置编辑框文本
        cb.setEditText('编辑文本')

        # 8. 数据
        # 8.1 插入带数据条目
        cb.insertItem(0, '数据测试', {'数据': "Data"})
        # 8.2 设置数据
        cb.setItemData(1, '设置的数据')

        # 9. 获取
        # btn.clicked.connect(lambda: print('Data', cb.currentData()))
        # btn.clicked.connect(lambda: print('Index', cb.currentIndex()))
        # btn.clicked.connect(lambda: print('Text', cb.currentText()))
        # btn.clicked.connect(lambda: print('Icon', cb.itemIcon(cb.currentIndex())))
        # btn.clicked.connect(lambda: print('Text', cb.itemText(cb.currentIndex())))
        # btn.clicked.connect(lambda: print('Data', cb.itemData(cb.currentIndex())))

        # 10. 条目数量限制
        cb.setMaxCount(5)  # 最多存储5条条目
        cb.setMaxVisibleItems(3)  # 最多展示5条条目信息，多的会被折叠
        print(cb.maxCount())
        print(cb.maxVisibleItems())

        # 11. 一些操作
        cb.setDuplicatesEnabled(True)  # 条目可重复
        print(cb.duplicatesEnabled())

        cb.setFrame(False)  # 文本框有无边框
        print(cb.hasFrame())

        cb.setIconSize(QSize(60, 60))  # 图标尺寸设置
        print(cb.iconSize())

        '''
            AdjustToContents = 0  根据内容调整大小
            AdjustToContentsOnFirstShow = 1  根据第一次展示的内容调整大小
            
            AdjustToMinimumContentsLength = 2   根据最小内容长度调整
            cb.setMinimumContentsLength()  设置最小内容长度
            AdjustToMinimumContentsLengthWithIcon = 3  根据最小内容长度加图标尺寸调整
        '''
        cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)  # 尺寸调整策略

        # btn.clicked.connect(lambda: cb.clearEditText())  # 清空编辑内容
        # btn.clicked.connect(lambda: cb.clear())  # 清空所有条目

        btn.clicked.connect(lambda: cb.showPopup())  # 展示下拉菜单

        cb.setCompleter(QCompleter(['1230', '23156']))  # 设置完成器
        print(cb.completer())

        # cb.setValidator(QValidator)  # 设置验证器（要自己写规则）

        # 12. 信号

        # 这两个信号仅在用户交互时会触发
        cb.activated.connect(lambda index: print(index, '条目被选择'))  # 参数是选择条目的索引.
        cb.activated[str].connect(lambda text: print(text, '条目被选择'))  # 参数是选择条目的文本.

        # 下面两个无论代码修改还是交互都会触发
        cb.currentIndexChanged.connect(lambda index: print(index, '当前条目索引改变'))
        cb.currentIndexChanged[str].connect(lambda text: print(text, '当前条目索引改变'))

        cb.currentTextChanged.connect(lambda text: print(text, '当前条目文本改变'))
        cb.editTextChanged.connect(lambda text: print(text, '编辑文本改变'))

        cb.highlighted.connect(lambda index: print(index, '该条目高亮（鼠标悬浮）'))
        cb.highlighted[str].connect(lambda text: print(text, '该条目高亮（鼠标悬浮）'))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
