import multiprocessing
import time


def print_sq():
    print("square = ")
    for i in range(1,5):
        time.sleep(1)
        print(i*i)

def print_cube():
    print("cube = ")
    for i in range(1,5):
        time.sleep(1.5)
        print(i*i*i)


if __name__ == "__main__":
    p1=multiprocessing.Process(target=print_sq)
    p2=multiprocessing.Process(target=print_cube)

    t=time.time()

    #start process
    p1.start()
    p2.start()

    #wait for process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)

    

