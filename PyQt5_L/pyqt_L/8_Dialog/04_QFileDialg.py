from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件对话框")
        self.resize(500, 500)
        self.setup_ui()
        # self.get_dir()
        # self.get_file()

    def setup_ui(self):
        btn = QPushButton('测试按钮', self)
        btn.move(100, 100)

        def file_func():
            # 初始化
            """
               QFileDialog(QWidget, Union[Qt.WindowFlags, Qt.WindowType])
               QFileDialog(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '')
           """
            fd = QFileDialog(self, '窗口标题', './', 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)')
            fd.show()

            # 设置打开模式（打开or保存）
            fd.setAcceptMode(QFileDialog.AcceptOpen)  # 打开
            # fd.setAcceptMode(QFileDialog.AcceptSave)  # 保存

            # 设置文件模式（打开文件/文件夹）
            '''
                Directory 文件夹
                AnyFile 文件，无论是否存在
                ExistingFile  单个现有的文件
                ExistingFiles 单个或多个现有文件
            '''
            fd.setFileMode(QFileDialog.ExistingFile)

            # 设置默认后缀（不是默认过滤器）
            fd.setDefaultSuffix('txt')

            # 设置过滤器
            # 会覆盖初始化设置
            # 设置一个
            # fd.setNameFilter('IMG(*.jpg *.png)')
            # 设置多个
            # fd.setNameFilters(['IMG(*.jpg *.png)', 'Python(*.py)'])

            # 设置指定元素名称
            fd.setLabelText(QFileDialog.FileName, '自定义的文件名')
            fd.setLabelText(QFileDialog.Accept, '自定义的接受')
            fd.setLabelText(QFileDialog.Reject, '自定义的拒绝')
            fd.setLabelText(QFileDialog.FileType, '自定义的文件类型')
            fd.setLabelText(QFileDialog.LookIn, '自定义的浏览')

            # 信号
            # 文件选择确定后
            fd.fileSelected.connect(lambda file_path: print('单个文件被选择', file_path))
            fd.filesSelected.connect(lambda file_path: print('多个文件被选择', file_path))
            fd.urlSelected.connect(lambda file_path: print('单个文件url被选择', file_path))
            fd.urlsSelected.connect(lambda file_path: print('多个文件url被选择', file_path))
            # 文件改变（选中就会变）
            fd.currentChanged.connect(lambda path: print('当前路径改变', path))
            fd.currentUrlChanged.connect(lambda path: print('当前路径url改变', path))
            # 进入文件夹
            fd.directoryEntered.connect(lambda path: print('进入文件夹', path))
            fd.directoryUrlEntered.connect(lambda path: print('进入文件夹url', path))
            # 过滤器被选择
            fd.filterSelected.connect(lambda filter_: print('过滤器被选择', filter_))

        btn.clicked.connect(file_func)

    def get_dir(self):
        # 参数： 父控件，窗口标题，打开路径
        # result = QFileDialog.getExistingDirectory(self, '窗口标题', './')
        # 返回字符串：文件夹路径
        result = QFileDialog.getExistingDirectoryUrl(self, '窗口标题', QUrl('./'))
        # 返回QUrl对象
        print(result)

    def get_file(self):
        # 参数： 父控件，窗口标题，打开的路径，过滤器，默认过滤器
        # 文件类型过滤器字符串写法： 名称1(*.png *.jpg);;名称2(*.py)

        # 打开一个文件
        # result = QFileDialog.getOpenFileName(self, '窗口标题', './', 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)', 'Python(*.py)', )
        # 返回元组：（文件路径，过滤器）

        # 打开多个文件
        # result = QFileDialog.getOpenFileNames(self, '窗口标题', './', 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)', 'Python(*.py)', )
        # 返回元组：（列表[多个文件路径]，过滤器）

        # 打开一个文件url
        # 参数中，路径要改为QUrl对象
        # result = QFileDialog.getOpenFileUrl(self, '窗口标题', QUrl('./'), 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)', 'Python(*.py)')
        # 返回元组：（QUrl对象，过滤器）

        # 打开多个文件url
        # result = QFileDialog.getOpenFileUrls(self, '窗口标题', QUrl('./'), 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)','Python(*.py)')

        # 保存文件
        # result = QFileDialog.getSaveFileName(self, '窗口标题', './', 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)','Python(*.py)')
        # 返回元组（文件保存路径，过滤器）

        # 保存文件-url
        result = QFileDialog.getSaveFileUrl(self, '窗口标题', QUrl('./'), 'ALL(*.*);;Images(*.png*.jpg);;Python(*.py)',
                                            'Python(*.py)')

        print(result)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
