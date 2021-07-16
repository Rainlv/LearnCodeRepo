from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("表单布局")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        form_layout = QFormLayout()

        name_le = QLineEdit()
        age_sb = QSpinBox()
        submit = QPushButton('提交')

        sex_layout = QBoxLayout(QBoxLayout.LeftToRight)
        female_btn = QRadioButton('女')
        male_btn = QRadioButton('男')
        sex_layout.addWidget(female_btn)
        sex_layout.addWidget(male_btn)

        age_label = QLabel('年龄(&age)')
        age_label.setBuddy(age_sb)

        form_layout.addRow('姓名(&name)', name_le)
        form_layout.addRow(age_label, age_sb)
        # form_layout.addRow(submit)
        # form_layout.addRow('性别', sex_layout)

        form_layout.insertRow(1, '性别'*10, sex_layout)

        self.setLayout(form_layout)

        # 获取一些位置信息
        # 1. 获取总行数
        print(form_layout.rowCount())
        # 2. 获取指定控件位置（控件不在布局内返回-1位置），返回（第几行，功能枚举值（role））,
        '''
            LabelRole = 0  标签（左侧）
            FieldRole = 1  输入框（右侧）
            SpanningRole = 2  单独占一整行
        '''
        print(form_layout.getWidgetPosition(submit))
        print(form_layout.getLayoutPosition(sex_layout))
        # 3. 获取指定位置的控件
        # 3.1 获取label
        print(form_layout.labelForField(name_le))

        # 指定位置设置控件  参数：行号，功能（左右），控件
        # 位置上有控件会添加不成功
        form_layout.setWidget(4, form_layout.FieldRole, submit)
        # form_layout.setLayout()

        # 移除控件
        # 1. 删除行
        # form_layout.removeRow(1)  # 直接从内存释放掉行内的所有控件
        # form_layout.removeRow(age_sb)  # 删除控件所在行的所有控件
        # 2. 移除行（不删除子控件，子控件要隐藏），返回一个对象
        # print(form_layout.takeRow(0).labelItem.widget())
        # print(form_layout.takeRow(0).fieldItem)
        # name_le.hide()
        # age_label.hide()

        # 行的包装策略
        '''
            DontWrapRows = 0  默认，字段总在标签旁边
            WrapLongRows = 1  保证标签显示完整，空间不足右侧区域会换行
            WrapAllRows = 2  左右区域，上下排列
        '''
        form_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        # 对齐方式
        # 1. 表单相对父控对齐方式
        form_layout.setFormAlignment(Qt.AlignVCenter | Qt.AlignRight)
        # 2. 标签对齐方式
        form_layout.setLabelAlignment(Qt.AlignRight)

        # 间距
        # 1. 行间距
        form_layout.setVerticalSpacing(20)
        # 2. 列间距
        form_layout.setHorizontalSpacing(10)

        # 右侧控件增长策略（会不会跟着父控件尺寸变化）
        '''
            FieldsStayAtSizeHint = 0  不变
            ExpandingFieldsGrow = 1  会变
            AllNonFixedFieldsGrow = 2
        '''
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
