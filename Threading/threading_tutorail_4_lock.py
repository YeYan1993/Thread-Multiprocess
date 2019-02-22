import threading
import time

"""加入lock之后能够让哪一个线程先运行，后运行"""

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1 is {}'.format(A))
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2 is {}'.format(A))
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock() #定义全局lock
    A = 0 # 定义全局变量A
    thread1 = threading.Thread(target=job1,name = 'T1')
    thread2 = threading.Thread(target=job2,name = 'T2')
    thread1.start()
    thread2.start()