# new way of threading using thread pools
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # this schedules our function and returns a future object 
    # which encapsulates the execution of the function
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())

    secs = [5,4,3,2,1]
    # this is a list comprehension
    # this creates a list of objects just like the for loop below
    # results = [executor.submit(do_something, 1) for _ in range(10)]
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # using map method
    # submit returns the futures object but map returns the results
    # map returns the results in the order that the thread was started
    # as_completed returns the results as the threads were completed
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

# old way of doing threading
# threads = []
# for _ in range(10):     # the underscrore is a throw away variable
#     t = threading.Thread(target=do_something, args=[1.5]) # argumets are passed as a list
#     t.start()
#     #t.join()   # Don't do this because then the 
#                 # thread would have to finish before the loop can proceed
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')