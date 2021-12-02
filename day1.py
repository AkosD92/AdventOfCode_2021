from collections import deque

data = []

with open('data/day1_data.txt') as file:
    for line in file:
        data.append(int(line))


def task_1(arg_data):
    prev_value = None
    cnt = 0
    for x in arg_data:
        if prev_value is None:
            prev_value = x
        else:
            if x > prev_value:
                cnt += 1
            prev_value = x

    return cnt


def task_2(arg_data):
    arr = deque([None, None, None])
    prev_sum = 0
    curr_sum = 0
    cnt = 0

    for x in arg_data:
        if None in arr:
            prev_sum += x
            curr_sum = prev_sum
            arr.rotate(1)
            arr[0] = x
        else:
            curr_sum -= arr[2]
            arr.rotate(1)
            arr[0] = x
            curr_sum += arr[0]
            if curr_sum > prev_sum:
               cnt += 1
            prev_sum = curr_sum

    return cnt 


res = task_2(data)

print(res)
