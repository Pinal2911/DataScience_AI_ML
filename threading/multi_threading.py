import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"this is number {i}")

def print_letters():
    for i in 'abcde':
        time.sleep(2)
        print(f"this is letter = ",{i})

#creat thread

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()
#start thread
t1.start()
t2.start()
#wait for thread to complete
t1.join()
t2.join()
finished_t=time.time()-t
print("this is finished time = ",finished_t)
    