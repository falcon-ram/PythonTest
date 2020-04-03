import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

#do_something()
#do_something()

# old way of doing threading
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
# Starts the threads
t1.start()
t2.start()
# ensures that the threads finish before code execution continues
t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')