def activity_selection(activities):
    activities.sort(key=lambda x: x[2])
    selected = [activities[0]]
    last_finish = activities[0][2]

    for i in range(1, len(activities)):
        name, start, finish = activities[i]
        if start >= last_finish:
            selected.append(activities[i])
            last_finish = finish

    return selected

activities = [
    ("A1", 0, 6),
    ("A2", 3, 4),
    ("A3", 1, 2),
    ("A4", 5, 8),
    ("A5", 5, 7),
    ("A6", 8, 9),
]

print("Activities (Name, Start, Finish):")
for a in activities:
    print(f"  {a}")

selected = activity_selection(activities)
print("\nSelected Activities (Greedy - Maximum Non-overlapping):")
for a in selected:
    print(f"  {a}")
print(f"\nTotal Activities Selected: {len(selected)}")
