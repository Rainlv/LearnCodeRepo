import threading
import queue
import time
import random

# 生产者与消费者，线程间的通信即数据交换

def consumer(q):
    i = 0
    while i < 10:
        get_num = q.get()
        print('消费者获得数字{}'.format(get_num))
        i += 1
        time.sleep(3)
        

def producer(q):
    i = 0
    while i < 10:
        num = random.randint(0,100)
        print('生产者生产数字{}'.format(num))
        q.put(num)
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    q = queue.Queue(10)

    t1 = threading.Thread(target=producer, args=(q,), name='producer')
    t2 = threading.Thread(target=consumer, args=(q,), name='consumer')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('end')
