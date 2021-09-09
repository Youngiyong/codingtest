def solution():
    arr = [[1, 4], [2, 6], [4, 7]]
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])

    cnt = 1
    end = arr[0][1]

    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            cnt += 1
            end = arr[i][1]
    return cnt