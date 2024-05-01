import random
import matplotlib.pyplot as plt
import time

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

sizes = [100000 * i for i in range(1, 21)]
linear_times = []
binary_times = []

for size in sizes:
    data = list(range(size))
    target = random.randint(0, len(data) - 1)

    start_time = time.perf_counter()
    linear_search(data, target)
    linear_times.append(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    binary_search(data, target)
    binary_times.append(time.perf_counter() - start_time)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, linear_times, label='Linear Search')
plt.plot(sizes, binary_times, label='Binary Search', linestyle='--')
plt.xlabel('Dataset Size')
plt.ylabel('Time in seconds')
plt.title('Search Algorithm Performance')
plt.legend()
plt.grid(True)
plt.show()
