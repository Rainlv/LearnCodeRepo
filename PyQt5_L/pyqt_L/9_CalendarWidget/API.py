from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("日历控件")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 初始化
        cw = QCalendarWidget(self)

        btn = QPushButton('测试按钮', self)
        btn.move(300, 300)
        # 日期获取
        btn.clicked.connect(lambda: print(cw.monthShown()))
        btn.clicked.connect(lambda: print(cw.yearShown()))
        btn.clicked.connect(lambda: print(cw.selectedDate()))
        # 日期范围
        # cw.setMinimumDate(QDate(1990, 1, 1))
        # cw.setMaximumDate(QDate(2022, 12, 12))
        cw.setDateRange(QDate(1990, 1, 1), QDate(2022, 12, 12))
        # 日期是否可编辑，默认可编辑
        cw.setDateEditEnabled(True)
        # 编辑日期后接收延迟
        cw.setDateEditAcceptDelay(2000)
        # 导航条是否可见
        cw.setNavigationBarVisible(True)
        # 一周第一天
        cw.setFirstDayOfWeek(Qt.Sunday)
        # 网格是否可见
        cw.setGridVisible(True)

        # 文字|格式
        tcf = QTextCharFormat()
        tcf.setFontPointSize(15)
        tcf.setFontUnderline(True)
        # 1. 头部文本格式设置
        cw.setHeaderTextFormat(tcf)
        # 2.1 水平头显示格式设置
        '''
            NoHorizontalHeader = 0  隐藏
            SingleLetterDayNames = 1
            ShortDayNames = 2
            LongDayNames = 3
        '''
        cw.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        # 2.2 垂直头设置
        '''
            NoVerticalHeader = 0  隐藏头部
            ISOWeekNumbers = 1  显示ISO周数，第几周
        '''
        cw.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
        # 3. 日期文本格式
        # 3.1 某类日期设置，比如所有周二
        t_tcf = QTextCharFormat()
        t_tcf.setToolTip('这是周二')
        t_tcf.setFontPointSize(16)
        t_tcf.setFontFamily('幼圆')
        cw.setWeekdayTextFormat(Qt.Tuesday, t_tcf)  #
        # 3.2 某个日期设置，具体某一天
        cw.setDateTextFormat(QDate(2020, 4, 20), t_tcf)

        # 设置默认选中日期
        cw.setSelectedDate(QDate(2020, 3, 10))
        # 日期选择模式设置
        # cw.setSelectionMode(QCalendarWidget.NoSelection)  # 日期无法选择
        cw.setSelectionMode(QCalendarWidget.SingleSelection)  # 日期可以单选

        # 一些方法
        '''
        showNextMonth
        showPreviousMonth
        showNextYear
        showPreviousYear
        showToday
        showSelectedDate
        setCurrentPage(2008, 8)  设置跳转到指定年月
        '''
        btn.clicked.connect(lambda: cw.setCurrentPage(2008, 8))

        # 信号
        # 1. 日期选择确定后（双击/按下回车等）
        cw.activated.connect(lambda date: print(date))  # 返回QDate对象
        # 2. 单击时
        cw.clicked.connect(lambda date: print(date))  # 返回QDate对象
        # 3. 当前页面改变时
        cw.currentPageChanged.connect(lambda y, m: print(y, m))  # 返回更改后的年月
        # 4. 选中改变
        cw.selectionChanged.connect(lambda: print('选中日期改变', cw.selectedDate()))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
