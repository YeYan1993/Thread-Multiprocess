import multiprocessing as mp

def job(x):
    return x*x

def multiCore():
    # pool 默认是所有的核
    pool = mp.Pool(processes=3) # 这里用3个核
    result = pool.map(job,range(10))
    print(result)
    result2 = pool.apply_async(job,(2,)) #需要迭代的，必须有逗号
    print(result2.get())
    # 迭代一个list
    multi_result = [pool.apply_async(job,(i,)) for i in range(10)]
    print([multi_result_single.get() for multi_result_single in multi_result])
if __name__ == '__main__':
    multiCore()