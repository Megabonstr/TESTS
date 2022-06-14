import time
from multiprocessing import Pool


def countup(N):
    n = 0
    while n < N:
        n += 1


def countup_time(N):
    start = time.time()
    n = 0
    while n < N:
        n += 1
    end = time.time()
    total = end - start
    print(n)
    print(f'Время выполнения: {total}', flush=True)


if __name__ == '__main__':
    print('Обычный вызов функции:', flush=True)
    countup_time(30000000)
    time.sleep(2)

    start = time.time()
    print('\nЧетыре процесса:', flush=True)
    max_for_process = 30000000 // 4
    process_pool = Pool(processes=4)

    process1 = process_pool.apply_async(countup, [max_for_process])
    process2 = process_pool.apply_async(countup, [max_for_process])
    process3 = process_pool.apply_async(countup, [max_for_process])
    process4 = process_pool.apply_async(countup, [max_for_process])

    process_pool.close()
    process_pool.join()

    end = time.time()
    total = end - start
    print(f'Время выполнения: {total}', flush=True)
