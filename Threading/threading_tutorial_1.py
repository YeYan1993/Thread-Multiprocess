import threading
import time

def thread_job_1():
    print("Thread_1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("Thread_1 end\n")

def thread_job_2():
    print("Thread_2 start\n")
    print("Thread_2 end\n")

def main():
    print(threading.enumerate())
    print(threading.active_count())
    print(threading.current_thread())

if __name__ == '__main__':
    main()
    """不能加()，因为要传的是函数名（Python一切皆对象，函数也是对象，可以当参数传递，
    传的是这个函数的引用），如果加（）表示执行函数，再将结果赋值给target"""
    thread_1 = threading.Thread(target=thread_job_1,name="Thread_1")
    thread_2 = threading.Thread(target=thread_job_2,name = "Thread_2")
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print("All done!\n")