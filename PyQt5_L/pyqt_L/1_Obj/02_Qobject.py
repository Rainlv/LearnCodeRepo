from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.name_property_operate()
        # self.inherits_api()
        # self.inherits_operate()
        # self.signal_api()
        # self.signal_test()
        # self.type_judging()
        self.delete_obj()

    def name_property_operate(self):
        # *******测试API*********开始
        obj = QObject()
        obj.setObjectName('notice')
        print(obj.objectName())

        obj.setProperty('notice_level1', 'error')
        obj.setProperty('notice_level2', 'warning')
        print(obj.property('notice_level1'))
        print(obj.dynamicPropertyNames())
        # *******测试API*********结束

        # *******案例演示*********开始
        with open(r'01_basic\Qobject.qss') as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setText('lbwnb')
        label.setObjectName('notice')
        label.setProperty('notice_level', 'warning')
        # label.setStyleSheet('font-size:25px;color:red;')

        label2 = QLabel(self)
        label2.setText('伞兵一号')
        label2.setObjectName('notice')
        label2.setProperty('notice_level', 'error')
        label2.move(100, 100)

        label3 = QLabel(self)
        label3.setText('xxx')
        label3.move(150, 150)

        btn = QPushButton(self)
        btn.setText('起飞')
        label2.setObjectName('notice')
        btn.move(50, 50)

        # *******案例演示*********结束

    def inherits_api(self):
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        print('obj0', obj0)
        print('obj1', obj1)
        print('obj2', obj2)
        print('obj3', obj3)

        # 设置父对象
        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj3.setParent(obj2)
        obj2.setObjectName('333')
        obj3.setObjectName('333')

        # 获取父对象
        print('obj1.parent():', obj1.parent())

        # 获取直接子对象
        print('obj0.children():', obj0.children())

        # 获取一个符合条件的子对象
        # 参数一：子对象类型；    参数二：子对象名称；
        # 参数三：查询方法，是否递归查找   FindDirectChildrenOnly，FindChildrenRecursively
        print('obj0.findChild():', obj0.findChild(QObject, '333', Qt.FindDirectChildrenOnly))

        # 获取多个符合条件的子对象
        print('obj0.findChildren():', obj0.findChildren(QObject, '333', Qt.FindChildrenRecursively))

    def inherits_operate(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label1.setText('label1')
        label2.setText('label2')
        label2.move(50, 50)
        btn = QPushButton(self)
        btn.move(100, 100)
        for sub in self.findChildren(QLabel):
            sub.setStyleSheet('background-color:cyan')

    def signal_api(self):
        self.obj = QObject()

        # self.obj.objectNameChanged()
        # self.obj.destroyed()

        def destroy_cao(obj):  # 会默认传入一个被销毁的对象作为参数，可以不接收
            print('对象被销毁', obj)

        self.obj.destroyed.connect(destroy_cao)  # 连接槽函数

        def name_cao(obj):  # 默认会传入修改后的对象名称作为参数，可不接收
            print('名字改变了', obj)

        def name_cao2(obj):
            print('名字改变了2', obj)

        self.obj.objectNameChanged.connect(name_cao)  # 连接槽函数
        self.obj.objectNameChanged.connect(name_cao2)  # 连接槽函数
        print('连接数:', self.obj.receivers(self.obj.objectNameChanged))  # 返回该信号连接的槽函数数量

        self.obj.setObjectName('xxx')

        self.obj.blockSignals(True)  # 会暂时阻止信号与槽函数的连接
        self.obj.setObjectName('xxoo')  # 不打印
        print(self.obj.signalsBlocked())  # 返回信号是否处于阻塞状态
        self.obj.blockSignals(False)  # 恢复连接
        self.obj.setObjectName('ooxx')
        print(self.obj.signalsBlocked())

        self.obj.objectNameChanged.disconnect()  # 取消连接
        self.obj.setObjectName('ooo')  # 不打印

        # receivers

    def signal_test(self):
        btn = QPushButton(self)
        btn.setText('点我点我')
        btn.resize(100, 100)
        btn.move(200, 200)

        def click_cao():
            print('点我也没用')

        btn.clicked.connect(click_cao)

    def type_judging(self):
        # ************API**************开始
        def api_test():
            obj = QObject()
            btn = QPushButton()
            w = QWidget()
            label = QLabel()
            objects = [obj, w, btn, label]
            for o in objects:
                print('是否为控件类型', o.isWidgetType())
                print('是否继承自按钮', o.inherits('QPushButton'))
                print('是否继承自QWidget', o.inherits('QWidget'))

        # api_test()
        # ************API**************结束

        # ************案例演示**************开始
        label1 = QLabel(self)
        label1.setText('lbwnb')
        label1.move(150, 150)
        label2 = QLabel(self)
        label2.setText('超级加倍')
        label2.move(50, 50)
        btn = QPushButton(self)
        btn.setText('起飞')
        btn.move(100, 100)

        for widget in self.children():
            if widget.inherits('QLabel'):
                widget.setStyleSheet('background-color:cyan;')
        # ************案例演示**************结束

    def delete_obj(self):
        # obj.deleteLater()  稍后删除，在下一次消息循环时删除，本次循环中仍能引用

        obj = QObject()

        obj.destroyed.connect(lambda: print('对象被删除'))

        obj.deleteLater()
        print(obj)  # 仍然可以打印出来


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()


    def win_title_cao(title):
        window.blockSignals(True)
        window.setWindowTitle('这是设置的标题：' + title)
        window.blockSignals(False)


    window.windowTitleChanged.connect(win_title_cao)

    window.setWindowTitle('信号与槽测试')

    window.show()

    sys.exit(app.exec_())
