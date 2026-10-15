# Day 55: basic multithreading

import threading
import time

def task(name):
    print(f"{name} starting")
    time.sleep(1)
    print(f"{name} done")

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

t1.start()
t2.start()
t1.join()
t2.join()
print("Both tasks complete")