# # 부분집합 (강의 코드) 미완성
# def backtrack(a, k, input):
#     global MAXCANDIDATES
#     c = [0] * MAXCANDIDATES
#
#     if k == input:
#         for i in range(1, k+1):
#             print(a[i], end =" ")
#         print()
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a,k,input)
#
#     def construct_candidates(a, k, input, c):
#         in_perm = False *NMAX
#
#         for i in range(1,k):
#             in_perm[a[i]] =True
#
#         ncandidates = 0
#         for i in range(1, input +1):
#             if in_perm[i] == False:
#                 c[ncandidates] = i
#                 ncandidates += 1
#         return ncandidates
#
#
#
# NMAX = 11
# MAXCANDIDATES = 10
# a = [0] * NMAX
#############################################################
#bit에 0과 1을 채우는 작업  (앞에서 부터 1채우기)
# def f(i, k):
#     if i == k:
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
#
#
#
# A = {1,2,3,4,5}
# N = len(A)
# bit = [0]*N
# f(0, N)
##############################################################
#부분집합
# NUMS = [1,2,3]
# N = 3
# a = [-1] * N
#
# def construct_candidates(c):
#     c[0] = 0
#     c[1] = 1
#     return 2
#
# def backtrack(a,k):
#     c = [-1] * 2
#     if k==N:
#         print(a)
#         return
#
#     nc = construct_candidates(c)
#     for i in range(nc):
#         a[k] = c[i]
#         backtrack(a, k+1)
#
#
# backtrack(a,0)

###############################################################
#순열

NUMS = [1,2,3]
N = 3
a = [-1] * N

def construct_candidates(c,k):
    pos = 0
    for i in range(N):
        if i not in a[0:k]:
            c[pos] = i
            pos += 1
    return pos

def backtrack(a,k):
    c = [-1] * N
    if k == N:
        print(a)
        return

    nc = construct_candidates(c,k)
    for i in range(nc):
        a[k] = c[i]
        backtrack(a, k+1)


backtrack(a,0)
############################################
# nums = [1,2,3,4,5,6,7,8,9,10]
# N = 10
# # goal = [[0,0,0,0,0,0,0,0,0,0],..., [1,1,1,1,1,1,1,1,1,1]]
# c = [0, 1]
# def partial(k, curS):
#     if curS >10:
#         return
#     if k == N:
#         print(a,  '=>', end=' ')
#         print(curS)
#         if curS == 10:
#             for i in range(N):
#                 if a[i] == 1:
#                     print(nums[i], end =' ')
#         print()
#
#         # for i in range(N):
#         #     if a[i]:
#         #         sumV += nums[i]
#         # print(sumV)
#         return
#     # c = [-1] * 후보의 개수
#     # nc = c_c(c)
#     # c[0] = 0
#     # c[1] = 1
#     for i in range(2):
#         a[k] = c[i]
#         if c[i] == 1:
#             partial(k+1, curS+nums[k])
#         else:
#             partial(k+1, curS)
# a = [-1] * N
# partial(0)


##################################
# nums = [1,2,3,4,5,6,7,8,9,10]
# N = 10
# # goal = [[0,0,0,0,0,0,0,0,0,0],..., [1,1,1,1,1,1,1,1,1,1]]
# # c = [0, 1]
# def partial(k, curS):
#
#     if k == N:
#         # print(a)
#         if curS == 10:
#             for i in range(N):
#                 if a[i]:
#                     print(nums[i], end=' ')
#             print('=>', curS)
#         return
#
#     a[k] = 0
#     partial(k+1, curS)
#     a[k] = 1
#     partial(k+1, curS +nums[k])
#
#     # for i in range(2):
#     #     a[k] = c[i]
#     #     partial(k+1)
#
# a = [-1] * N
# partial(0,0)
#########################################################
