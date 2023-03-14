# 부분집합의 합 (강사님 코드)
# def f(i, k):
#     if i == k:
#         s = 0#하나의 부분집합 완성
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]
#
#         print(bit,s)
#
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
#
#
# A = [1,2,3]
# N = len(A)
# bit = [0]*N
# f(0, N)
####################################################
# 부분집합의 합 (교수님 코드) (미완성)  밑에서 위로 올려주는거 , 주로 최솟값 찾을 때
def f(k,curS):
    if k == N:
        s = 0#하나의 부분집합 완성
        for j in range(k):
            if bit[j]:
                s += A[j]

        print(bit,s)

    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)


A = [1,2,3]
N = len(A)
bit = [0]*N
f(0, N)

####################################################
# 합이 key와 같은 부분집합 출력
# def f(i, k, key):
#     if i == k:
#         s = 0#하나의 부분집합 완성
#         for j in range(k):
#             if bit[j]:
#                 s += A[j] #부분집합의 합
#         if s == key:  # 합이 key와 같은 부분집합 출력
#             for j in range(k):
#                 if bit[j]:
#                     print(A[j], end = ' ')
#             print()
#
#
#
#     else:
#         bit[i] = 1
#         f(i+1, k, key)
#         bit[i] = 0
#         f(i+1, k, key)
#
# A =[1,2,3,4,5,6,7,8,9,10]
# N =len(A)
# key = 10
# bit= [0]*N
# f(0, N, 8)

############################################
#부분집합의 합 중에서 찾고자 하는 합의 값의 원소들과 부분집합의 수 반환
def f(i,k,s,t):  # i = 원소, k =집합의 크기, s = i-1까지 고려한 부분집합의 합, t = 찾고자 하는 값
    global cnt
    if i ==k:
        if s == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)  # A[i] 포함
        bit[i] = 0
        f(i+1, k, s , t)      # A[i] 불포함


A =[1,2,3,4,5,6,7,8,9,10]
N =len(A)
key = 10
cnt = 0
bit= [0]*N
f(0, N, 0,key)
print(cnt)  # 합이 key인 부분집합의 수
###################################################
#부분집합의 합 중에서 찾고자 하는 값의 부분집합의 수 반환
def f(i,k,s,t):  # i = 원소, k =집합의 크기, s = i-1까지 고려한, t = 찾고자 하는 값
    global cnt
    if i ==k:
        if s == t:


            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)  # A[i] 포함
        bit[i] = 0
        f(i+1, k, s , t)      # A[i] 불포함


A =[1,2,3,4,5,6,7,8,9,10]
N =len(A)
key = 10
cnt = 0
bit= [0]*N
f(0, N, 0, key)
print(cnt)  # 합이 key인 부분집합의 수