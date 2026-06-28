import time

def o1_operation(n):
    return n * n

def on_operation(n):
    total = 0
    for i in range(n):
        total += i
    return total

def on2_operation(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total

sizes = [100, 500, 1000, 5000]

print(f"{'N':<10} {'O(1) time':<20} {'O(N) time':<20} {'O(N^2) time'}")
print("-" * 70)

for n in sizes:
    t1_start = time.perf_counter()
    o1_operation(n)
    t1 = time.perf_counter() - t1_start

    t2_start = time.perf_counter()
    on_operation(n)
    t2 = time.perf_counter() - t2_start

    t3_start = time.perf_counter()
    on2_operation(n)
    t3 = time.perf_counter() - t3_start

    print(f"{n:<10} {t1:<20.8f} {t2:<20.8f} {t3:.8f}")
