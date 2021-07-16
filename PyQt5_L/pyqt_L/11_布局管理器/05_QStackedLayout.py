from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("堆叠布局")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sl = QStackedLayout(self)  # 直接添加父控件，取代第二步操作

        # self.setLayout(sl)  # 对于这个布局，第二步一定给父控件是设置布局（不然会出bug）

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan')
        label2.setStyleSheet('background-color:yellow')
        label3.setStyleSheet('background-color:red')
        label4 = QLabel('标签4')
        label5 = QLabel('标签5')
        label6 = QLabel('标签6')
        label4.setStyleSheet('background-color:purple')
        label5.setStyleSheet('background-color:orange')
        label6.setStyleSheet('background-color:blue')

        # 堆叠布局，一次只显示一个控件
        print(sl.addWidget(label1))  # 返回索引位置
        print(sl.addWidget(label2))  # 返回索引位置
        print(sl.addWidget(label3))  # 返回索引位置

        print(sl.insertWidget(0, label4))  # 不会改变当前显示的控件

        # 设置当前显示控件
        # sl.setCurrentIndex(0)
        # sl.setCurrentWidget(label5)  # 标签必须被添加到到布局中，不然无效
        # 设置显示模式
        sl.setStackingMode(QStackedLayout.StackAll)  # 只显示当前页面
        label1.hide()
        # sl.setStackingMode(QStackedLayout.StackOne)  # 都显示，当前页面最前

        # 信号
        sl.currentChanged.connect(lambda val: print(val))
        # sl.widgetRemoved.connect()  # 控件被移除

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
