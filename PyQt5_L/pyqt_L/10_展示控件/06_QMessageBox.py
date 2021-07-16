from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("消息框‘")
        self.resize(500, 500)
        self.setup_ui()
        # self.static_func()

    def setup_ui(self):
        """
          QMessageBox(parent: QWidget = None)
          QMessageBox(QMessageBox.Icon, str, str,
          buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.NoButton,
          parent: QWidget = None,
          flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
          """
        # mb = QMessageBox(self)
        mb = QMessageBox(QMessageBox.Warning, '窗口标题', '<h2>内容主标题</h2>', QMessageBox.Ok | QMessageBox.Discard, self)

        # 默认是模态窗口，即使调用的是show方法，可以用强制改为非模态
        # mb.setModal(False)
        # mb.setWindowModality(Qt.NonModal)

        # 图标设置
        '''
            NoIcon = 0  无图标
            Information = 1     图标i
            Warning = 2     黄色三角！
            Critical = 3    红×
            Question = 4    问号？
        '''
        # mb.setIcon(QMessageBox.Warning)
        # mb.setIconPixmap(QPixmap('图标路径').scaled(50, 50))  # 自定义图标，后面是缩放

        # 子元素设置
        # 1. 主标题设置
        mb.setText('<h1>这是主标题</h1>')
        # 1.1 主标题文本类型设置
        mb.setTextFormat(Qt.AutoText)
        # 2. 副标题设置
        mb.setInformativeText('<h2>副标题设置</h2>')
        # 3. 复选框设置
        mb.setCheckBox(QCheckBox('下次是否提醒', mb))
        # 4. 详情文本设置
        mb.setDetailedText('详情文本，会添加一个详情页展示按钮，不支持富文本')

        # 按钮设置
        # 1. 添加标准按钮
        mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # 2. 添加（自定义）按钮，参数：按钮，按钮功能（Role）
        btn_r = QPushButton('自定义拒绝按钮', mb)
        mb.addButton(btn_r, QMessageBox.RejectRole)
        btn_s = mb.addButton('重置按钮', QMessageBox.ResetRole)  # 返回一个按钮对象
        # 3. 删除按钮
        # mb.removeButton(btn_s)
        # 4. 设置默认按钮（默认获取焦点）
        mb.setDefaultButton(btn_r)
        # 5. 设置退出按钮（按esc键触发的按钮）
        mb.setEscapeButton(btn_s)

        # 获取按钮对象（标准按钮导出地址）
        yes_btn = mb.button(QMessageBox.Yes)
        no_btn = mb.button(QMessageBox.No)
        print(yes_btn, 'yes')
        print(no_btn, 'no')

        # 获取按钮功能对象
        r_btn = mb.buttonRole(btn_r)
        s_btn = mb.buttonRole(btn_s)

        # 获取被点击的按钮
        print(mb.clickedButton())

        # 信号
        print(btn_s, 'reset')
        print(btn_r, 'reject')
        mb.buttonClicked.connect(lambda btn: print(btn))

        def cao(btn):
            role = mb.buttonRole(btn)
            if role == QMessageBox.YesRole:
                print('yes按钮被点击')
            if btn == no_btn:
                print('no按钮被按下')

        mb.buttonClicked.connect(cao)


        mb.show()

    def static_func(self):
        # 返回值是标准按钮对象的枚举数值
        # QMessageBox.about(self, '窗口标题', '主标题')
        # QMessageBox.aboutQt(self, 'Qt')
        # QMessageBox.critical(self, '窗口', '主标题')
        # 其他几个也有information，question，warning
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
