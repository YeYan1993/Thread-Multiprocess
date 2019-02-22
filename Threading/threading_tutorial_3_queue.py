import threading
import time
from queue import Queue
import numpy as np
"""代码实现功能，将数据列表中的数据传入，使用四个线程处理，
将结果保存在Queue中，线程执行完后，从Queue中获取存储的结果"""

def job(list1,q):
    for i in range(len(list1)):
        list1[i] = list1[i] ** 2
    q.put(list1)

def multithreading(data):
    starttime = time.time()
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    endtime = time.time()
    print(results)
    print("MultipleThreading using time is {}".format(endtime - starttime))

def one_thread_compute(data):
    data = np.array(data)
    starttime = time.time()
    data_process = np.square(data)
    endtime = time.time()
    print(data_process)
    print("One Threading using time is {}".format(endtime - starttime))

if __name__ == '__main__':
    data = [[1, 2, 3],
            [2, 3, 4],
            [3, 4, 4],
            [3, 3, 3]]
    one_thread_compute(data)
    multithreading(data)