from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit的学习")
        self.resize(500, 500)
        # self.time_demo()
        self.setup_ui()

    def setup_ui(self):
        """
            QDateTimeEdit(parent: QWidget = None)
            QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
            QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
            QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)
        """
        dte = QDateTimeEdit(QDateTime.currentDateTime(), self)
        # 也有独立的dateEdit和timeEdit控件
        dte.move(100, 100)
        '''时间日期格式符
        d 没有前导零的数字的日期（1到31）
        dd 有前导零的数字的日期（01到31）
        ddd 缩写的本地化时期名称（‘周一’到‘周日’）
        dddd 完整本地化的时期名称（‘星期一’到‘星期日’）
    
        M 没有前导零的数字的月份（1到12）
        MMM （4月）
        MMMM （四月）
        其他同上面
        
        yy 年份的两位数字（00-99）
        yyyy 年份的四位数字
        
        
        h 没有前导零的小时（显示AM/PM时会转为12小时）
        hh 有前导零的小时
        
        H 没有前导零的小时（显示AM/PM时不会转为12小时）
        HH 有前导零的小时
        
        m 分钟（有无前导零同上）
        
        s 秒
        
        z 毫秒
        zzz 有前导零的毫秒
                
        AP/A 使用AM/PM显示
        ap/a 使用am/pm显示
        
        t 时区
        
    '''
        dte.setDisplayFormat('yy/MMMM/ddd__m:s:zzz t A')
        print(dte.displayFormat())

        '''section'''
        # 1.1 section个数
        print(dte.sectionCount())
        # 1.2 当前处于第几个section(从0开始)
        btn = QPushButton('测试', self)
        btn.move(200, 200)
        # btn.clicked.connect(lambda: print(dte.currentSectionIndex()))

        # 设置焦点处于某个section
        # 2.1 按索引位置（0开始）
        # btn.clicked.connect(lambda: dte.setCurrentSectionIndex(2))
        # 2.2 按section类型
        btn.clicked.connect(lambda: dte.setCurrentSection(QDateTimeEdit.DaySection))

        # 获取操作
        # 3.1 获取指定索引位置的section
        print(dte.sectionAt(0))  # 返回的枚举类型（类似QDateTimeEdit.DaySection）的值
        # 3.2 获取指定section的文本内容
        print(dte.sectionText(QDateTimeEdit.MonthSection))

        '''最大最小日期时间范围'''
        # dte.setMaximumDateTime(QDateTime(3000, 12, 30, 23, 59, 59))
        # dte.setMinimumDateTime(QDateTime.currentDateTime())
        # dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3))

        print(dte.maximumDateTime())
        dte.clearMaximumDateTime()  # 清空范围设置

        '''日历'''
        dte.setCalendarPopup(True)  # 会把步长调节器替换成一个下拉日历

        '''日期时间获取'''
        print(dte.dateTime())

        '''信号'''
        dte.dateTimeChanged.connect(lambda val: print(val))
        # 也有相应的date和time信号

    def time_demo(self):
        """年月日 时分秒
        QDateTime()
        QDateTime(Union[QDateTime, datetime.datetime])
        QDateTime(Union[QDate, datetime.date])
        QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], timeSpec: Qt.TimeSpec = Qt.LocalTime)
        QDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
        QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], Qt.TimeSpec, int)
        QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], QTimeZone)
        """
        dt = QDateTime(2018, 12, 12, 12, 30)
        self.dt = dt
        now = QDateTime.currentDateTime()
        # 时间设置
        # 1.1 增减
        self.dt = self.dt.addYears(2)  # 要接收返回值
        self.dt = self.dt.addDays(-2)
        # 1.2设置
        dt.setDate(QDate(2012, 1, 1))
        dt.setTime(QTime(12, 12, 12))
        print(dt)
        # 计算时区时差（和utc的时差）
        print('utc时差', self.dt.offsetFromUtc())  # 返回是 秒
        # 时差
        print('秒差', dt.secsTo(now))
        print('毫秒差', dt.msecsTo(now))


        """年月日
        QDate()
        QDate(int, int, int)
        QDate(int, int, int, QCalendar)
        QDate(QDate)
        """
        d = QDate()
        self.d = d
        # 设置时间
        d.setDate(2012, 12, 12)
        d.addYears(5)
        print(d)
        # 时差
        print('天数差', d.daysTo(QDate(2011, 1, 1)))
        # 时间获取
        print('今天日期', QDate.currentDate())
        print('天', d.day())
        print('这一周第几天', d.dayOfWeek())
        print('这一年第几天', d.dayOfYear())
        print('这一月有几天', d.daysInMonth())
        print('这一年有几天', d.daysInYear())


        """时分秒
        QTime()
        QTime(int, int, second: int = 0, msec: int = 0)
        QTime(QTime)
        """
        t = QTime(12, 12, 12)
        now = QTime.currentTime()
        # 调整时间
        t = t.addSecs(10)
        t = t.addMSecs(10)
        print(t)
        # 秒差
        print(t.secsTo(now))
        # 获取时间
        print('时', t.hour())
        # 计时
        t.start()
        btn = QPushButton('结束', self)
        btn1 = QPushButton('开始', self)
        btn1.move(50, 50)
        btn.clicked.connect(lambda: print(t.elapsed()))  # 单位ms
        btn1.clicked.connect(lambda: t.restart())  # 重新计时


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
