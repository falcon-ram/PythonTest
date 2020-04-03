import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')


# old way of doing threading
threads = []
for _ in range(10):     # the underscrore is a throw away variable
    t = threading.Thread(target=do_something, args=[1.5]) # argumets are passed as a list
    t.start()
    #t.join()   # Don't do this because then the 
                # thread would have to finish before the loop can proceed
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')