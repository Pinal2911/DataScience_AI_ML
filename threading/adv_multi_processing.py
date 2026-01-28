from concurrent.futures import ProcessPoolExecutor
import time

def print_sq(numbers):
    time.sleep(2)
    return f"number sq : {numbers*numbers}"

if __name__ == "__main__":
    numbers=[1,2,3,4,55,34,23,89,67,34]
    t=time.time()
    with ProcessPoolExecutor(max_workers=3) as exe:
        results=exe.map(print_sq,numbers)

    for r in results:
        print(r)
    print("end time = ",time.time()-t)