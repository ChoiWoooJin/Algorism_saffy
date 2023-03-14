# def bfs(v,N):  # G = 그래프 , v = 탐색 시작점
#     visited = [0]*(N+1)  # n = 정점의 개수
#     queue = []
#     #queue = [v] # 시작점 인큐
#     queue.append(v) #시작점 인큐
#     visited[v] = 1 # 시작점 인큐 표시
#     while queue:
#         t = queue.pop(0)  # 디큐
#         print(t, end=' ') # t에서 처리한 일
#         for v in adjL[t]: # t에 인접이고 방문한 적 없는 v
#             if visited[v] == 0:
#                 queue.append(v) # v 인큐
#                 visited[v] = visited[t] + 1  # v 인큐되었음 표시
#     print()
#     print(visited)
#
#
#
#
#
#         # if not visited[t]:
#         #     visited[t] = True
#         #     visit(t)
#         #     for i in G[t]:
#         #         if not visited[i]:
#         #             queue.append(i)
#
#
# #연습문제 3
# # 7 8
# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# V, E =  map(int, input().split())
# arr = list(map(int, input().split()))
# adjL = [[]for _ in range(V+1)]
# for i in range(E):
#     n1, n2 = arr[i*2], arr[i*2+1]
#     adjL[n1].append(n2)
#     adjL[n2].append(n1)
# # print(adjL)
#
# #탐색 순서
# bfs(1,V) #시작정점 1, v는 마지막 정점



######################################################
#교수님 코드 BFS(큐)

def bfs(s):
    Q = []
    visited = [0]* (N+1)
    Q.append(s)
    visited[s] = 1
    while Q:
        v = Q.pop(0)
        print(v)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
#
N = 7
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'

lst = list(map(int, s.split()))
G = [[] for _ in range(N+1)]
for idx in range(0, len(lst), 2):
    p1 = lst[idx]
    p2 = lst[idx+1]
    G[p1].append(p2)
    G[p2].append(p1)
print(G)

bfs(7)

# ###########################################
#교수님 코드 DFS(스택)

# def dfs(s):
#     ST = []
#     visited = [False] * (N+1)
#     ST.append(s)
#     visited[s] = True
#     while ST:
#         v = ST.pop(-1)
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[w] = True
#
# N = 7
# s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
#
# lst = list(map(int, s.split()))
# G = [[] for _ in range(N+1)]
# for idx in range(0, len(lst), 2):
#     p1 = lst[idx]
#     p2 = lst[idx+1]
#     G[p1].append(p2)
#     G[p2].append(p1)
# print(G)
#
# dfs(1)




