# 自定义多线程
import time
import threading


class CodeThreading(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码{}'.format(threading.current_thread()))
            time.sleep(1)
            
class DrawThreading(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画画{}'.format(threading.current_thread()))
            time.sleep(1)

def main():
    t1 = CodeThreading()
    t2 = DrawThreading()

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()