def solution():
    A = [5, 1, 3, 7]
    B = [2, 2, 6, 8]

    answer = 0
    a = sorted(A, reverse=True)
    b = sorted(B, reverse=True)

    idx = 0
    for i in a:
        cur = i
        if cur < b[idx]:
            idx += 1
            answer += 1

    return answer