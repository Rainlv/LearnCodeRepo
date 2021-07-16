from PyQt5.Qt import *


class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())
        link_str = self.anchorAt(me.pos())  # 获取鼠标点击位置的链接
        if len(link_str) > 0:
            QDesktopServices.openUrl(QUrl(link_str))  # 打开链接地址
        return super(MyTextEdit, self).mousePressEvent(me)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("常用API")
        self.resize(500, 500)
        self.run()

    def run(self):
        self.setup_ui()
        self.placeHolderText()
        # self.content()
        self.sign()

    def sign(self):
        # self.te.textChanged.connect(lambda: print('文本改变'))
        # self.te.selectionChanged.connect(lambda: print('选中文本改变'))
        self.te.copyAvailable.connect(lambda x: print('复制%s可用' % x))

    def setup_ui(self):
        # TextEdit初始化
        te = MyTextEdit(self)
        self.te = te
        te.move(50, 50)
        te.resize(200, 200)
        te.setText('xxx')
        te.setStyleSheet('background-color:cyan;')
        te.insertHtml('<a name="anchor" href="https://www.baidu.com">百度</a>')
        # 按钮初始化
        btn_content = QPushButton('文本内容测试按钮', self)
        self.btn_content = btn_content
        btn_content.move(100, 280)
        btn_content.pressed.connect(self.func_content)

        btn_cursor = QPushButton('光标文本测试按钮', self)
        self.btn_cursor = btn_cursor
        btn_cursor.move(100, 320)
        btn_cursor.pressed.connect(self.func_cursor_text)

        btn_cursor_img = QPushButton('光标图片测试按钮', self)
        self.btn_cursor_img = btn_cursor_img
        btn_cursor_img.move(100, 360)
        btn_cursor_img.pressed.connect(self.func_cursor_img)

        btn_cursor_list = QPushButton('光标列表测试按钮', self)
        self.btn_cursor_list = btn_cursor_list
        btn_cursor_list.move(100, 400)
        btn_cursor_list.pressed.connect(self.func_cursor_list)

        btn_cursor_table = QPushButton('光标表格测试按钮', self)
        self.btn_cursor_table = btn_cursor_table
        btn_cursor_table.move(100, 440)
        btn_cursor_table.pressed.connect(self.func_cursor_table)

        btn_cursor_get = QPushButton('内容与格式获取按钮', self)
        self.btn_cursor_get = btn_cursor_get
        btn_cursor_get.move(250, 280)
        btn_cursor_get.pressed.connect(self.func_cursor_get)

        btn_cursor_select = QPushButton('内容选中与光标移动按钮', self)
        self.btn_cursor_select = btn_cursor_select
        btn_cursor_select.move(250, 320)
        btn_cursor_select.pressed.connect(self.func_cursor_select)

        btn_cursor_position = QPushButton('光标位置按钮', self)
        self.btn_cursor_position = btn_cursor_position
        btn_cursor_position.move(250, 360)
        btn_cursor_position.pressed.connect(self.func_cursor_position)

        btn_cursor_edit = QPushButton('开始结束编辑按钮', self)
        self.btn_cursor_edit = btn_cursor_edit
        btn_cursor_edit.move(250, 400)
        btn_cursor_edit.pressed.connect(self.func_cursor_edit)

        btn_autoFormat = QPushButton('文本框下的功能按钮', self)
        self.btn_autoFormat = btn_autoFormat
        btn_autoFormat.move(250, 440)
        btn_autoFormat.pressed.connect(self.func_te)

    def func_cursor_edit(self):
        tc = self.te.textCursor()
        # 一次编辑内的内容在撤回时是一起撤回的
        tc.beginEditBlock()  # 开始编辑

        tc.insertText('123')
        tc.insertBlock()  # 换行用
        tc.insertText('456')
        tc.insertBlock()  # 换行用

        tc.endEditBlock()  # 结束编辑

        tc.insertText('789')

    def func_cursor_position(self):
        tc = self.te.textCursor()
        print('段落结尾', tc.atBlockEnd())
        print('段落开始', tc.atBlockStart())
        print('文档结尾', tc.atEnd())
        print('文档开始', tc.atStart())
        print('第几列', tc.columnNumber())
        print('光标相对文档位置', tc.position())
        print('光标相对段落位置', tc.positionInBlock())

    def func_cursor_get(self):
        tc = self.te.textCursor()

        '''选中内容获取'''
        print(tc.selectedText())  # 返回str

        print(tc.selection())  # 返回QTextDocumentFragment对象
        print(tc.selection().toPlainText())  # 获取的内容转换成普通文本

        print(tc.selectedTableCells())  # 获取表格选中的内容，返回元组（选中起始行，选中几行，选中起始列，选中几列）

        print(tc.selectionStart())  # 选中内容，光标起始位置
        print(tc.selectionEnd())  # 选中内容，光标结束位置
        return
        # print(tc.block())  # QTextBlock对象
        print(tc.block().text())  # 获取光标所在段落文本（每段的QTextBlock对象地址相同，但获取得的文本不同）
        print(tc.blockNumber())  # 获取光标所在文本是第几段，从0开始

        print(tc.currentList())  # QTextList对象
        print(tc.currentList().count())  # 列表条目数

        '''
            blockFormat()  文本块格式
            blockCharFormat()   文本块字符格式
            charFormat()    文本字符格式
            currentFrame()  光标所在框架
            currentTable()  当前的表格
        '''

    def func_cursor_select(self):
        tc = self.te.textCursor()

        '''
            KeepAnchor  固定光标锚点（会选中）
            MoveAnchor  移动光标锚点（不会选中）
        '''
        # 按位置设置光标
        """ setPosition(self, int, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor) """
        # tc.setPosition(3, QTextCursor.KeepAnchor)

        # 按方法移动光标
        """
         movePosition(QTextCursor.MoveOperation, 
                        QTextCursor.MoveMode = QTextCursor.MoveAnchor,
                        int = 1)        -> bool 
        """
        # tc.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)

        # 按类型选中
        '''
        Document  整个文档
        BlockUnderCursor  文本块
        LineUnderCursor  文本行
        WordUnderCursor  单词
        '''
        # tc.select(QTextCursor.Document)

        # 清除选中
        # tc.clearSelection()

        # 是否选中文本
        print(tc.hasSelection())  # 返回布尔类型

        '''删除操作'''
        # 删除选中文本--没选中则不操作
        # tc.removeSelectedText()
        # 删除选中文本--没选择则删除光标后的字符
        # tc.deleteChar()
        # 删除选中文本--没选择则删除光标前的字符
        tc.deletePreviousChar()

        # 设置光标
        self.te.setTextCursor(tc)

    # 光标--插入文本和内容设置
    def func_cursor_text(self):
        '''设置文本格式（鼠标选中需要设置的文本再点击按钮生效）'''
        tc = self.te.textCursor()

        tcf = QTextCharFormat()
        tcf = QTextCharFormat()
        tcf.setFontFamily('幼圆')
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)  # 设置上划线
        tcf.setFontUnderline(True)  # 设置下划线

        tc.setCharFormat(tcf)
        '''合并格式'''
        tcf2 = QTextCharFormat()
        tcf2.setFontStrikeOut(True)  # 删除线设置
        # tc.setCharFormat(tcf2)  # 会覆盖之前设置的格式
        tc.mergeCharFormat(tcf2)  # 会合并与之前的格式，两种格式共存
        return
        '''设置文本块内的文本格式'''
        tc = self.te.textCursor()

        tcf = QTextCharFormat()
        tcf.setFontFamily('幼圆')
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)  # 设置上划线
        tcf.setFontUnderline(True)  # 设置下划线

        tc.setBlockCharFormat(tcf)

        '''设置文本块内的段落格式'''
        # 1. 创建段落（文本块）格式对象
        tbf = QTextBlockFormat()
        # 2. 设置段落格式
        tbf.setAlignment(Qt.AlignRight)  # 右对齐
        tbf.setIndent(2)
        tc.setBlockFormat(tbf)
        return

        tc = self.te.textCursor()
        tff = QTextFrameFormat()
        # 设置框架样式
        tff.setBorder(10)  # 设置边框
        tff.setBorderBrush(QColor(100, 20, 200))  # 边框样式
        tff.setRightMargin(100)  # 右外间距
        # 插入框架
        tc.insertFrame(tff)

        return
        '''文本块插入（段落格式设置）'''
        tc = self.te.textCursor()
        # 1. 创建段落（文本块）格式对象
        tbf = QTextBlockFormat()
        # 2. 设置段落格式
        tbf.setAlignment(Qt.AlignRight)  # 右对齐
        tbf.setIndent(3)
        # 3. 文本内容格式设置
        # 3.1 获取格式设置对象
        tcf = QTextCharFormat()
        # 3.2 设置悬停提示字符
        # 3.3 设置字体类型
        tcf.setFontFamily('隶书')
        # 3.4 设置字体大小
        tcf.setFontPointSize(25)
        """
             insertBlock(self)
             insertBlock(self, QTextBlockFormat)
             insertBlock(self, QTextBlockFormat, QTextCharFormat)
         """
        # 4. 插入文本块
        tc.insertBlock(tbf, tcf)
        return

        '''文本语句插入'''
        tc = self.te.textCursor()
        # tdf = QTextDocumentFragment.fromHtml('<h1>html代码</h1>')
        tdf = QTextDocumentFragment.fromPlainText('<h1>html代码</h1>')
        tc.insertFragment(tdf)
        return
        '''文本插入'''
        # 1. 获取文档对象
        print(self.te.document())
        # 2. 获取文本光标（不是鼠标cursor）
        tc = self.te.textCursor()
        # 3.. 设置插入文本格式
        # 3.1 获取格式设置对象
        tcf = QTextCharFormat()
        # 3.2 设置悬停提示字符
        tcf.setToolTip('悬停提示字符')
        # 3.3 设置字体类型
        tcf.setFontFamily('隶书')
        # 3.4 设置字体大小
        tcf.setFontPointSize(25)
        # 4. 光标插入内容，带格式
        """
            insertText(str)
            insertText(str, QTextCharFormat)
        """
        tc.insertText('光标插入的文本', tcf)

    # 光标--插入图片和格式设置
    def func_cursor_img(self):
        # 1. 获取光标
        tc = self.te.textCursor()
        # 2. 插入图片
        # 2.1 获取图片格式设置对象
        tif = QTextImageFormat()
        # 2.2 设置图片路径
        tif.setName('../../2_Widget/xxx.png')
        # 2.3 设置图片尺寸
        tif.setWidth(100)
        tif.setHeight(100)
        # 2.4 使用光标插入图片
        tc.insertImage(tif)
        '''
            FloatLeft = 1
            FloatRight = 2
        '''
        # tc.insertImage(tif, QTextFrameFormat.FloatRight)  # 第二个参数是图片浮动
        # tc.insertImage('../../2_Widget/xxx.png')  # 可以直接写路径，大小要重新设置

    # 光标--插入列表和格式设置
    def func_cursor_list(self):
        tc = self.te.textCursor()
        '''
            ListCircle = -2    一个空心圆圈
            ListDecimal = -4    十进制升序排列
            ListDisc = -1   一个实心黑圆圈
            ListLowerAlpha = -5    小写拉丁字母按字母顺序排列
            ListLowerRoman = -7    小写罗马字母按字母顺序排列
            ListSquare = -3    一个方块
            ListUpperAlpha = -6    大写拉丁字母按字母顺序排列
            ListUpperRoman = -8    大写拉丁罗马按字母顺序排列
        '''
        # 1. 插入列表（光标右侧内容作为第一项）
        """
        insertList(self, QTextListFormat) -> QTextList
        insertList(self, QTextListFormat.Style) -> QTextList
        """
        # 1.1 带样式插入
        # t1 = tc.insertList(QTextListFormat.ListDisc)
        # print(t1)  # 返回值是QTextList对象
        # __1.2 自定义格式样式
        # ____1.2.1 创建格式对象
        tlf = QTextListFormat()
        # ____1.2.2 设置格式
        tlf.setIndent(3)  # 缩进设置，数字代表几个tab键
        tlf.setStyle(QTextListFormat.ListDecimal)  # 设置列表前的样式
        tlf.setNumberPrefix('<')  # 数字行标前缀（只有在样式是ListDecimal时生效）
        tlf.setNumberSuffix('>')  # 数字行标后缀（只有在样式是ListDecimal时生效）
        tc.insertList(tlf)
        # 2. 创建列表（光标所在段落作为第一项）
        # t1 = tc.createList(QTextListFormat.ListCircle)

    def func_cursor_table(self):
        tc = self.te.textCursor()
        # 2. 表格格式
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)  # 对齐方式
        ttf.setCellPadding(6)  # 单元格内边距
        ttf.setCellSpacing(3)  # 单元格间距
        '''
            FixedLength = 1  固定长度
            PercentageLength = 2    占表格的百分比长度
            VariableLength = 0
        '''
        # 设置单元格长度,传入一个元组，元组内每个元素表示一列单元格长度
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50),
                                       QTextLength(QTextLength.PercentageLength, 40),
                                       QTextLength(QTextLength.PercentageLength, 10)))
        # 1. 插入表格
        """
            insertTable(self, int, int, QTextTableFormat) -> QTextTable
            insertTable(self, int, int) -> QTextTable
        """
        # tc.insertTable(5, 3)  # 行列
        t1 = tc.insertTable(5, 3, ttf)  # 行 列 格式
        print(t1)  # 返回一个QTable对象
        t1.appendColumns(2)  # 获取对象，追加列

    # 占位文本设置
    def placeHolderText(self):
        self.te.setPlaceholderText('请输入个人简介信息')
        print(self.te.placeholderText())

    def func_te(self):
        # 不是光标的方法了，是文本框下的方法

        return
        # tab键功能设置
        # self.te.setTabChangesFocus(True)  # 设置使tab键功能为改变焦点
        self.te.setTabStopDistance(100)  # 设置制表距离，默认为100
        print(self.te.tabStopDistance())
        return
        # 只读功能设置
        self.te.setReadOnly(True)
        self.te.insertPlainText('aaa')  # 只读状态下也能通过代码插入文字
        print(self.te.isReadOnly())
        return
        # 滚动到锚点
        self.te.insertHtml('aaa' * 300 + '<a name="anchor" href="#">锚点</a>' + 'aaa' * 200)
        self.te.scrollToAnchor('anchor')  # 锚点名称要写name属性
        return
        # 一些常用的编辑操作
        # self.te.copy()  # 复制
        # self.te.paste()  # 粘贴
        # self.te.canPaste()  # 能否粘贴
        # self.te.selectAll()  # 全选
        '''
            QTextDocument.FindBackward  向右搜索
            QTextDocument.FindCaseSensitively  区分大小写
            QTextDocument.FindWholeWords  仅匹配完整的单词
        '''
        print(self.te.find('xx', QTextDocument.FindWholeWords | QTextDocument.FindCaseSensitively))  # 多个筛选条件用或运算连接

        return
        # 设置光标宽度（一般结合覆盖模式使用，开启时光标宽度增大）
        self.te.setCursorWidth(10)
        print(self.te.cursorWidth())
        print(self.te.cursorRect(self.te.textCursor()))
        return
        # 输入覆盖模式（想当与键盘ins按钮）
        self.te.setOverwriteMode(True)
        print(self.te.overwriteMode())
        return
        # 换行
        '''
            FixedColumnWidth = 3    填充列的宽度（超过这个列宽度就会自动换行）
            FixedPixelWidth = 2  填充像素宽度（超过这个像素宽度就会自动换行）
            setLineWrapColumnOrWidth  设置列/像素宽度限制

            NoWrap = 0  没有软换行，超过控件宽度会产生滚动条
            WidgetWidth = 1  以控件宽度为限制，但会保持单词完整性
        '''
        self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.te.setLineWrapColumnOrWidth(30)  # 设置列/像素宽度限制（取决于设置的模式）

        # 设置单词换行模式
        print(self.te.lineWrapMode())
        '''
         WordWrap = 1  保持单词完整性
         NoWrap = 0  没有包装
         ManualWrap = 2  与WordWrap相同
         WrapAnywhere = 3  宽度够了后，随意在任何位置换行（结合FixedPixelWidth）
         WrapAtWordBoundaryOrAnywhere = 4   尽肯能赶在单词的边界，否则就任意换行(结合FixedColumnWidth)
        '''
        self.te.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)  # 会覆盖换行模式

        return
        # 自动格式化
        '''
            AutoAll = -1    应用所有自动格式。（目前仅支持自动项目符号列表）
            AutoBulletList = 1  自动创建项目符号列表，在最左侧输入*号创建
            AutoNone = 0  不做任何格式化（默认）
        '''
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)

    def func_content(self):
        # 字符设置
        tcf = QTextCharFormat()
        tcf.setFontItalic(True)
        tcf.setForeground(QColor(10, 50, 200))
        '''字体大小写
            MixedCase = 0  默认
            AllUppercase = 1    大写
            AllLowercase = 2    小写
            SmallCaps = 3   前几个字母变大变小？试试就知道
            Capitalize = 4  单词首字母大写
        '''
        tcf.setFontCapitalization(QFont.SmallCaps)  # 字体大小写设置
        self.te.setCurrentCharFormat(tcf)

        tcf2 = QTextCharFormat()
        tcf2.setFontStrikeOut(True)
        self.te.mergeCurrentCharFormat(tcf2)  # 合并样式

        return
        # 文本颜色（字体色，背景色）
        self.te.setTextBackgroundColor(QColor(200, 20, 30))  # 字体背景色
        self.te.setTextColor(QColor(10, 200, 30))  # 字体颜色
        return
        # 字体设置
        """
           QFont()
           QFont(str, pointSize: int = -1, weight: int = -1, italic: bool = False)
           QFont(QFont, QPaintDevice)
           QFont(QFont)
           QFont(Any)
       """
        font = QFont()
        font.setBold(True)
        self.te.setCurrentFont(font)
        return
        # 字体设置

        # QFontDialog.getFont()  # 会弹出一个字体选择的设置页面
        self.te.setFontFamily('幼圆')  # 设置字体
        '''字体粗细
        
            Thin = 0
            ExtraLight = 12
            Light = 25
            Normal = 50
            Medium = 57
            DemiBold = 63
            ExtraBold = 81
            Bold = 75
            Black = 87
        '''
        self.te.setFontWeight(QFont.Black)  # 字体粗细设置
        self.te.setFontItalic(True)  # 倾斜设置
        self.te.setFontUnderline(True)  # 下划线
        # 对齐方式设置
        # 会在鼠标所在段落生效，其他段落不影响
        self.te.setAlignment(Qt.AlignRight)

        return
        # 清空文本框内容
        # self.te.clear()
        self.content()

    # 文本内容设置
    def content(self):
        # 1. 设置普通文本（会清空原本文本框内的内容，设置完后光标在设置的内容最前面）
        self.te.setPlainText('<h1>普通文本</h1>')
        print(self.te.toPlainText())
        # 1.1 插入普通文本（不会清空原本文本框的内容，插入完后光标在插入的文本前）
        self.te.insertPlainText('<h1>插入的文本</h1>')
        # 2. 设置富文本
        self.te.setHtml('<h1>富文本</h1>')
        self.te.insertHtml('<h2>插入的富文本</h2>')
        print(self.te.toHtml())  # 获取的是html的源码，不只是富文本内容
        # 3. 设置文本（根据内容自动判定是否为富文本）
        self.te.setText('<h1>自动判定</h1>')
        self.te.setText('<h1xxx>普通文本</h1xxx>')
        # 4. 追加文本内容（会在文本最后插入，无论光标在哪，自动识别富文本，好像会默认换行）
        self.te.append('<h3>追加的文本</h3>')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
