import multiprocessing as mp
import threading as td

def job(q):
    result = 0
    for i in range(1000):
        result += i + i**2
    q.put(result)

if __name__ == '__main__':
    """多进程必须要再main下运行，不然会报错"""
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    result1 = q.get()
    print(result1)
    result2 = q.get()
    print(result2)
    print("All done!")