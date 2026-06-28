import heapq

def branch_and_bound_knapsack(capacity, weights, values, n):
    items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    sorted_weights = [weights[i] for i in items]
    sorted_values = [values[i] for i in items]

    def upper_bound(level, current_weight, current_value):
        if current_weight >= capacity:
            return 0
        bound = current_value
        total_weight = current_weight
        for i in range(level, n):
            if total_weight + sorted_weights[i] <= capacity:
                total_weight += sorted_weights[i]
                bound += sorted_values[i]
            else:
                remaining = capacity - total_weight
                bound += (remaining / sorted_weights[i]) * sorted_values[i]
                break
        return bound

    max_value = 0
    pq = [(-upper_bound(0, 0, 0), 0, 0, 0)]

    while pq:
        neg_bound, level, cur_weight, cur_value = heapq.heappop(pq)
        if -neg_bound <= max_value:
            continue
        if level == n:
            max_value = max(max_value, cur_value)
            continue

        with_item_weight = cur_weight + sorted_weights[level]
        with_item_value = cur_value + sorted_values[level]

        if with_item_weight <= capacity:
            max_value = max(max_value, with_item_value)
            ub = upper_bound(level + 1, with_item_weight, with_item_value)
            if ub > max_value:
                heapq.heappush(pq, (-ub, level + 1, with_item_weight, with_item_value))

        ub = upper_bound(level + 1, cur_weight, cur_value)
        if ub > max_value:
            heapq.heappush(pq, (-ub, level + 1, cur_weight, cur_value))

    return max_value

weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
capacity = 8
n = len(weights)

result = branch_and_bound_knapsack(capacity, weights, values, n)
print("Branch and Bound - 0/1 Knapsack")
print(f"  Weights : {weights}")
print(f"  Values  : {values}")
print(f"  Capacity: {capacity}")
print(f"  Maximum Value: {result}")
