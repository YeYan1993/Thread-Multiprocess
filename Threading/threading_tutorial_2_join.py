import threading
import time

"""join能够让多个线程等待之前thread运行完成之后，再运行后面代码"""

def thread_job():
    print("T1 start!\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finished!\n")

def thread_job_2():
    print("T2 start!\n")
    print("T2 finished!\n")

def main():
    thread_1 = threading.Thread(target=thread_job,name='T1')
    thread_2 = threading.Thread(target=thread_job_2,name = 'T2')
    thread_1.start()
    thread_2.start()
    thread_1.join() #加上join()之后，发现All done再T1 finish之后了
    print("All done!\n")

if __name__ == '__main__':
    main()