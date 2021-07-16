# 多线程使用
import time
import threading

def coding():
    for x in range(3):
        print('正在写代码{}'.format(threading.current_thread()))   # 当前线程名字
        time.sleep(1)

def drawing(n):
    for x in range(n):
        print('正在画画{}'.format(threading.current_thread()))
        time.sleep(1)



if __name__ == "__main__":

    t1 = threading.Thread(target=coding)  # 传入的函数不含(),是coding不是coding()
    t2 = threading.Thread(target=drawing,name='drawingThread',args=(3,))
                            # name参数给线程命名,arg=()参数是在函数需要传参时用的


    t1.start()
    t2.start()

    print(threading.enumerate())  # 查看当前所有的线程

    t1.join()       # 插队，在主线程前，先运行t1、t2线程，保证先运行完t1和t2再进行下面的print
    t2.join()

    # 这是主线程
    print(threading.enumerate())  # 查看当前所有的线程
