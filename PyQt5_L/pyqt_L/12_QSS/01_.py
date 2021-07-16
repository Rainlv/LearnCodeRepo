from PyQt5.Qt import *
from Tool import QssTool


class Btn(QPushButton):
    pass

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS简介和选择器")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        '''
            .表示只匹配当前类，不匹配其子类，默认是会匹配的
            例： .QPushButton{
                background-color: yellow;
                }


            * 通配符，全局设置
            例： * {
                background-color: gray;
                }


            #objName Id选择器，匹配对应id控件
                    配合btn1.setObjectName('b1')使用
            例1：QPushButton#b1{
                    background-color: cyan;
                    border: 4px solid;
                }
            例2：#pink{
                    background-color:pink;
                }


            [属性名=属性值]或者[属性名]  属性选择器，匹配对应属性/属性值
                配合label1.setProperty('notice_level', 'warning')使用
            例1：QLabel[notice_level='warning']{
                    border:3px solid yellow;
                }
            例2：QLabel[notice_level]{
                    background-color:pink;
                }


            后代选择器，选择所有后代（包括直接和间接）
            例：#box1 QLabel{
                background-color:white;
            }

            子选择器，选择直接后代
            例：#box1>QLabel{
                background-color:white;
            }


            子控件选择器，选择复合控件里的子控件
            例：控制QCheckBox的复选框子控件
            QCheckBox::indicator{
                    width:20px;
                    height:20px;
                }
        '''
        '''伪状态：
            :hover 鼠标悬停
            :checked  button控件被选中
            :unchecked  button控件未被选中
            :pressed  控件被按下
            :focus  控件获取焦点
            :disable  控件不可用
            :enable  控件可用
            :indeterminate  CheckBox或RadioButton部分选中时
            :on  控件处于on状态
            :off  控件处于off状态
            
        !伪状态 表示否定
            !:focus  没有获取焦点
            !:checked  未被选中
            ......
        伪状态连用
            :hover:checked  被选中且鼠标悬停时
        '''
        w1 = QWidget(self)
        w1.setObjectName('box1')
        w2 = QWidget(self)
        w2.move(100, 0)
        w3 = QWidget(w1)

        label1 = QLabel('标签1', w1)
        label2 = QLabel('标签2', w2)
        label1.setProperty('notice_level', 'warning')
        label2.setProperty('notice_level', 'error')
        label1.resize(200, 60)
        label2.resize(200, 60)
        label3 = QLabel('标签3', w3)
        label3.resize(200, 60)


        btn1 = QPushButton('按钮1', w1)
        btn1.setObjectName('b1')
        btn1.move(50, 50)
        btn2 = Btn('按钮2', w2)
        btn2.setObjectName('pink')
        btn2.move(50, 0)

        cb = QCheckBox('python', w1)
        cb.move(100, 110)
        # self.setStyleSheet('QPushButton#b1 {background-color:red;}')  # 对指定ObjectName的对象设置样式

        QssTool.setQss('style.qss', self)  # 自己封装的类

        lable3 = QLabel(self)
        label3.move(0, 100)

        self.QssBorder(label3)


    def QssBorder(self, label):
        '''
            四线统一设置：上右下左   上下 + 左右

            border-style:
                none 无
                dotted  点状
                solid   实线
                dashed  虚线
                doubled 双线
                groove  3D凹槽边框
                ridge  3D垄状边框
                inset   3Dinset边框
                outset   3Doutset边框
        '''
        label.setStyleSheet('''
            QLabel{
                background-color:red;
                border-width: 6px 10px;
                border-style:groove ridge inset outset;
                border-top-style:doubled;
                border-left-color:rgb(12, 55, 233);
                border-right-color:#ff00ff;
            }
        ''')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
