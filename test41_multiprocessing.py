# old way of doing multiprocessing
import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

if __name__ == '__main__':
    # do_something()
    # do_something()
    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    # Have to do it this was cause if you added the join to the loop above
    # the process whould have to finish before the loop continues execution
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')
