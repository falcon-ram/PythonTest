# new way of doing multiprocessing
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    # the context manager below automatically joins the processes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result())
        # print(f1.result())
        secs = [5,4,3,2,1]
        #results = [executor.submit(do_something, 1) for _ in range(10)]
        #results = [executor.submit(do_something, sec) for sec in secs]
        results = executor.map(do_something, secs)

        # prints the results in the order that they completed
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        # map returns results in the order that they were started
        for result in results:
            print(result)


    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')