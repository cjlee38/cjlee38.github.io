import math

def lis(arr):
    arr = [-math.inf] + arr
    N = len(arr)
    cache = [-1] * N

    def find(start):
        if cache[start] != -1:
            return cache[start]

        ret = 0
        for nxt in range(start+1, N):
            if arr[start] < arr[nxt]:
                ret = max(ret, find(nxt) + 1)

        cache[start] = ret
        return ret

    ans = find(0)
    print(cache)
    return ans

lst = [3, 5, 7, 9, 2, 1, 4, 8]
print(lis(lst))