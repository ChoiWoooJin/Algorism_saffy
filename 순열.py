# 순열 백트래킹
nums = [20, 30, 40]
# goal : [[20,30,40], [20,40,30], [30,20,40], [30,]...]

def per(k):
    if k == N:
        print(a)
        for i in range(N):
            idx = a[i]
            print(nums[idx], end = ' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            a[k] = i
            per(k+1)
            visited[i] = False

N = 3
a = [-1] * N
visited = [False]*N

per(0)