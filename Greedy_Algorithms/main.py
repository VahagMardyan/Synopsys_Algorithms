def activity_selector(s:list, f:list):
    n = len(s)
    selected_activities = [0]
    last_finish_time = f[0]

    for i in range(1, n):
        if s[i] >= last_finish_time:
            selected_activities.append(i)
            last_finish_time = f[i]
    return selected_activities

activities = [(1, 2), (5, 7), (3, 4), (0, 6)]

# # sorting by finish time
activities.sort(key=lambda x: x[1])

s = [a[0] for a in activities]
f = [a[1] for a in activities]

result = activity_selector(s, f)
print(result)