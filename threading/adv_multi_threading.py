from concurrent.futures import ThreadPoolExecutor
import time

def print_nos(nos):
    time.sleep(1)
    return f"Number : {nos}"

numbers=[1,2,3,4,5,6,7,8,9,10,3]
t=time.time()
#max_worker=3 means no of threads ==3
with ThreadPoolExecutor(max_workers=3) as exe:
    results=exe.map(print_nos,numbers)

    for r in results:
        print(r)
    print(time.time()-t)