from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LCD屏幕显示")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 初始化
        lcd = QLCDNumber(self)
        lcd.setDigitCount(7)  # 设置位数
        # lcd = QLCDNumber(5, self)  # 第一个参数指定数字位数
        lcd.move(0, 0)

        lcd.resize(300, 100)

        # 展示内容（字符串，int，float）
        lcd.display(": '")  # 单引号对应摄氏度的°
        lcd.display(12345)  # 若一多余位数，数字显示为0
        lcd.display('12345')  # 只显示最大位数，后面切断
        lcd.display(-123.12)  # 小数点和负号算一位内容，小数点后多余位数四舍五入

        # 内容展示模式（进制），保证位数够，若溢出会用十进制展示
        lcd.display(12)

        ''' 
           Bin = 3  二进制
           Dec = 1  十进制  
           Hex = 0  十六
           Oct = 2  八
    '''
        lcd.setMode(QLCDNumber.Bin)
        # lcd.setHexMode()  # 其他类推，效果同上

        # 获取数值，非数值打印0，获取到的是十进制数值
        print(lcd.value())  # 获取源数据的整数
        print(lcd.intValue())  # 获取源数据

        # 溢出判定
        print(lcd.checkOverflow(12.1235))
        # 溢出信号（先连接信号，在展示）
        lcd.overflow.connect(lambda : print('数据溢出'))

        lcd.display(123456778)

        # 初始化
        lcd1 = QLCDNumber(5, self)
        lcd1.move(0, 100)
        lcd1.resize(300, 100)
        lcd1.display(66)
        lcd2 = QLCDNumber(5, self)
        lcd2.move(0, 200)
        lcd2.resize(300, 100)
        lcd2.display(66)
        # 分段样式
        '''
            Outline = 0  变白
            Filled = 1  默认
            Flat = 2
        '''
        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd1.setSegmentStyle(QLCDNumber.Filled)
        lcd2.setSegmentStyle(QLCDNumber.Flat)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
