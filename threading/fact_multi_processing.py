import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(1000000)

def compute_fact(number):
    print("calculation factorial = ")
    res=math.factorial(number)
    print("fact = ",res)
    return res

if __name__ == "__main__":
    numbers=[5000,6000,700,8000]
    st=time.time()

    with multiprocessing.Pool() as p:
        res=p.map(compute_fact,numbers)
        et=time.time()
    
    print("result = ",res)
    print("differences = ",et-st)