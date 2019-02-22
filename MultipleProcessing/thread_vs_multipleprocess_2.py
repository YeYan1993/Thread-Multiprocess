import multiprocessing as mp
import threading as td
import time

def job(q):
    result = 0
    for i in range(1000000):
        result += i + i**2
    q.put(result)

def mulcore():
    """多进程必须要再main下运行，不然会报错"""
    start_time = time.time()
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    result1 = q.get()
    result2 = q.get()
    end_time = time.time()
    print("MultCore Using Time: {}".format(end_time - start_time))
    print("MultiCore: {}".format(result1 + result2))

def normal():
    start_time = time.time()
    result = 0
    for _ in range(2):
        for i in range(1000000):
            result += i + i ** 2
    end_time = time.time()
    print("Normal Using Time: {}".format(end_time - start_time))
    print("Normal: {}".format(result))

def multithread():
    start_time = time.time()
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    result1 = q.get()
    result2 = q.get()
    end_time = time.time()
    print("MultThread Using Time: {}".format(end_time - start_time))
    print("MultiThread: {}".format(result1 + result2))
if __name__ == '__main__':
    multithread()
    normal()
    mulcore()