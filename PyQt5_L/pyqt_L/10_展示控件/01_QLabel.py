from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("标签控件")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel('测试文字', self)
        label.setStyleSheet('background-color:cyan')
        label.resize(300, 300)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        label.setIndent(20)  # 缩进
        label.setMargin(20)  # 四周外边距

        label.setText('<h1>xx&x</h1>')  # &设置快捷键用
        '''
        PlainText
        RichText
        AutoText
        '''
        label.setTextFormat(Qt.PlainText)  # 设置文本类型

        le = QLineEdit(self)
        le.move(250, 250)
        le2 = QLineEdit(self)
        le2.move(250, 300)
        label.setBuddy(le)  # 作用在标签上的快捷键会把焦点转移到相应的关联控件上

        # label.setPixmap(QPixmap('../2_Widget/xxx.png'))  # 给控件加图片
        # label.setScaledContents(True)  # 仅对图片有效，根据控件大小缩放图片
        '''
        TextSelectableByMouse  鼠标选中
        TextSelectableByKeyboard  键盘选中
        NoTextInteraction  不可交互
        TextEditable  文本可编辑
        
        TextEditorInteraction 文本编辑器默认值 == Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable
        
        '''
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)  # 与标签内文本交互模式

        label.setSelection(1, 2)  # 选中字符（前提可选中），参数：起始位置，选择字符长度

        label.setText('<a href="www.baidu.com">百度</a>')
        label.setTextFormat(Qt.AutoText)
        label.setOpenExternalLinks(True)  # 设置超链接能否直接打开

        label.setText('12 3456789' * 6)
        label.setWordWrap(True)  # 换行，会保证单词完整性

        # 添加gif图
        movie = QMovie('snow.gif')
        label.setMovie(movie)
        movie.start()
        movie.setSpeed(200)  # 设置播放速度，100是1倍速

        # label.clear()  # 清空

        # 信号
        label.setText('<a href="www.baidu.com">百度</a>')
        # 1. 鼠标点击超链接触发（若设置了点击会跳转到网页则不会触发该信号）
        label.linkActivated.connect(lambda a: print(a))  # 参数是链接地址
        # 2. 鼠标悬停超链接上触发
        label.linkHovered.connect(lambda a: print(a))  # 参数是链接地址



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
