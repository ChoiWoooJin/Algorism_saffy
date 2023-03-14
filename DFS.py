# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#
#
# # 저장 방법
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# adjM = [[0]*(V+1) for _ in range(V+1)]
# adjL = [[0] for _ in range(V+1)]
#
#
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adjM[v1][v2] = 1
#     adjM[v2][v1] = 1                # 연결 방법
#
#     adjL[v1].append(v2)
#     adjL[v2].append(v1)
#
# print()

##############################################
#연습문제 3

# 입력과정
V = 7+1 #0번은 안쓸거임
# S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# S = list(map(int,S.split()))
# G = [[0,0,0,0,0,0,0,0],
#      [0,0,1,1,0,0,0,0],
#      [0,1,0,0,1,1,0,0],
#      [0,1,0,0,0,0,0,1],
#      [0,0,1,0,0,0,1,0],
#      [0,0,1,0,0,0,1,0],
#      [0,0,0,0,0,1,0,1],
#      [0,0,0,1,0,0,0,1],]

def dfs(v):
    ST = []
    visited = [False] * V
    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop()
        print(v)
        # for w in G[v]
        for w in range(V):
            if G[v][w] and not visited[w]:
                ST.append(w)
                visited[w] = True
############################################
# G = [[0]*V for _ in range(V)]
# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1][v2] = 1
#     G[v2][v1] = 1
# print(G)
#####################################
#입력과정 2
# G = [[] for _ in range(V)]
# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1].append(v2)
#     G[v2].append(v1)
#
# print(G)
######################################
#순서 중요할 때
# G = [[], [2,3], [1,4,5], [1,7], [2,6], [2,6], [4,5,7], [3,6]]
V = 7+1
#
# def dfs(v):
#     ST = []
#     visited = [False] * V
#     ST.append(v)
#     visited[v] = True
#     while ST:  # len(ST) > 0:
#         for w in G[v]:
#             if not visited[w]:
#                 visited[w] = True
#                 print((w))
#                 ST.append(v)
#                 v = w
#                 break
#         else:
#             v = ST.pop()
# dfs(1)

#########################################
# 한번씩 들르는게 목표일 떄
G = [[], [2,3], [1,4,5], [1,7], [2,6], [2,6], [4,5,7], [3,6]]
V = 7+1

# def dfs(v):
#     ST = []
#     visited = [False] * V
#     ST.append(v)
#     while ST:
#         v = ST.pop()
#         if not visited[v]:
#             visited[v] = True
#             print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#
# dfs(1)
############################################

G = [[], [2,3], [1,4,5], [1,7], [2,6], [2,6], [4,5,7], [3,6]]
V = 7+1
#가장 쉬운 방법
# def dfs(v):
#     ST = []
#     visited = [False] * V
#
#     ST.append(v)
#     visited[v] = True
#     while ST:
#         v = ST.pop()
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[v] = True
# print(dfs(1))


##########################################
G = [[], [2,3], [1,4,5], [1,7], [2,6], [2,6], [4,5,7], [3,6]]
V = 7+1
#재귀
visited = [False] * V
def dfsr(v):
    print(v)
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfsr(w)
dfsr(1)


