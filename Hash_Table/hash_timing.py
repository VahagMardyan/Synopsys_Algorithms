import time
from hash_table import Hash_Table

data_size = 10000
keys = [i for i in range(data_size)]
values = [i**2 for i in range(data_size)]

ht = Hash_Table(100)

for i in range(data_size):
    ht.insert(keys[i], values[i])

target_key = 9999

iterations = 10000

start_time = time.perf_counter()
for _ in range(iterations):
    result = ht[target_key]
ht_time = time.perf_counter() - start_time

# print(f"Total time for {iterations} searches: {ht_time:.6f} seconds")
# print(f"Average time for per search is: {(ht_time / iterations):.10f} seconds")

# ht.get_stats()
# print()
print(ht)