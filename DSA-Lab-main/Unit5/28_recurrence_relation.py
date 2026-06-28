def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, lc = merge_sort_count(arr[:mid])
    right, rc = merge_sort_count(arr[mid:])
    merged = []
    comparisons = lc + rc
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons

def recurrence_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = recurrence_fibonacci(n - 1, memo) + recurrence_fibonacci(n - 2, memo)
    return memo[n]

print("Recurrence Relation Demo: T(n) = 2T(n/2) + n  (Merge Sort)")
print(f"{'Array Size':<15} {'Comparisons'}")
print("-" * 30)
import random
for size in [4, 8, 16, 32]:
    data = random.sample(range(1000), size)
    _, comparisons = merge_sort_count(data)
    print(f"{size:<15} {comparisons}")

print("\nRecurrence Relation Demo: F(n) = F(n-1) + F(n-2)  (Fibonacci)")
print(f"{'n':<10} {'F(n)'}")
print("-" * 20)
for n in range(1, 11):
    print(f"{n:<10} {recurrence_fibonacci(n)}")
