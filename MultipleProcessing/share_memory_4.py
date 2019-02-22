import multiprocessing as mp
import time
"""定义共享内存变量（全局变量），能够在多核计算中共享变量"""

def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print("value : {}".format(v.value))
    l.release()
def multiCore():
    # 定义进程锁(先p1计算好之后的value，
    # p2基于p1最后结果再进行计算，不相互干扰)
    lock = mp.Lock()
    # 定义共享内存value
    value = mp.Value('i',0)
    array = mp.Array('i',[1,2,3]) # 只能一维
    p1 = mp.Process(target=job,args=(value,1,lock))
    p2 = mp.Process(target=job,args=(value,3,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All done!")

if __name__ == '__main__':
    multiCore()