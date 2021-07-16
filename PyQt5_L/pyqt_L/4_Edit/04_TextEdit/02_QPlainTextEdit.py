from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit学习")
        self.resize(500, 500)
        self.setup_ui()
        self.run()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        self.pte = pte
        pte.move(100, 100)
        pte.resize(300, 300)

        self.gengerate_btn('块操作', 50, 30, self.func_block)
        self.gengerate_btn('缩放操作', 50, 60, self.func_zoomInOrOut)
        self.gengerate_btn('滚动操作', 150, 30, self.func_scroll)
        self.gengerate_btn('光标操作', 150, 60, self.func_cursor)
        self.gengerate_btn('信号操作', 250, 30, self.sign)

    def run(self):
        self.api()
        self.pte.setCenterOnScroll(True)  # 使光标居中，会在文本框下产生留白区域

    def gengerate_btn(self, p_str, m_x, m_y, func=None):
        btn = QPushButton(p_str, self)
        btn.move(m_x, m_y)
        btn.pressed.connect(func)

    def api(self):
        # 占位文本设置
        self.pte.setPlaceholderText('请输入个人信息')

        # 只读设置
        # self.pte.setReadOnly(True)

        # 文本格式设置
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(200, 10, 10))
        self.pte.setCurrentCharFormat(tcf)

        # 自动换行设置
        '''
            NoWrap = 0  不自动换行（水平滚动条）
            WidgetWidth = 1  自动换行（默认）
        '''
        self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)

        # 覆盖模式（键盘ins键）设置
        self.pte.setOverwriteMode(True)
        print(self.pte.overwriteMode())

        # tab键控制设置
        self.pte.setTabStopDistance(80)
        self.pte.setTabChangesFocus(False)

        # 文本操作
        # 1.1 普通文本设置
        self.pte.setPlainText('设置的普通文本')
        # 1.2 插入普通文本
        self.pte.insertPlainText('插入的普通文本')
        # 1.3 追加的普通文本
        self.pte.appendPlainText('追加的普通文本')
        # 1.4 追加html文本（仅支持部分标签，表格列表图片等不支持）
        self.pte.appendHtml('<a href="#">html文本</a> ')
        # 2. 获取文本
        print(self.pte.toPlainText())

    def func_block(self):
        # 获取当前块（段落）数目
        print(self.pte.blockCount())
        # 设置最大块数目（会删除前面的段落保留后面的段落保证段落数）
        self.pte.setMaximumBlockCount(3)
        print(self.pte.maximumBlockCount())

    def func_zoomInOrOut(self):
        # 设置缩放
        # 1.1 放大（参数填负数会缩小）
        self.pte.zoomIn(10)
        # 1.2 缩小
        # self.pte.zoomOut(10)

    def func_scroll(self):
        # 滚动区域使使光标居中
        # self.pte.centerCursor()
        # 保证光标可见，不可见会滚动区域使可见
        self.pte.ensureCursorVisible()
        self.pte.setFocus()

    def func_cursor(self):
        # 获取光标对象
        # tc = self.pte.textCursor()

        # # 获取某个位置的光标
        tc = self.pte.cursorForPosition(QPoint(100, 60))
        # # 光标位置插入文本
        # tc.insertText('光标插入的文本')
        # 获取光标矩形
        print(self.pte.cursorRect(tc))
        # 移动光标
        self.pte.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)

        self.pte.setFocus()  # 不会改变鼠标光标的位置

    def sign(self):
        # self.pte.textChanged.connect(lambda: print('文本内容改变'))
        # self.pte.selectionChanged.connect(lambda: print('选中内容改变', self.pte.textCursor().selectedText()))

        # 改变编辑状态
        # doc = self.pte.document()
        # doc.setModified(False)
        # self.pte.modificationChanged.connect(lambda val: print('编辑状态改变', val))

        # self.pte.cursorPositionChanged.connect(lambda: print('光标位置改变'))
        # self.pte.blockCountChanged.connect(lambda n: print('块的个数改变', n))
        self.pte.updateRequest.connect(lambda rect, dy: print('区域更新', rect, dy))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
