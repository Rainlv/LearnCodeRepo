class QssTool(object):
    @staticmethod  # 外部调用qss文件
    def setQss(file_path, widget_name):
        with open(file_path, 'r') as w:
            content = w.read()
            widget_name.setStyleSheet(content)
