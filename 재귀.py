# def f(i,k):
#     if i == k: # 목표에 도달하면
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, k)
#
#
# A = [10, 20 , 30]
# B = [0] * 3
#
# f(0, 3)

########################################
# n! = n*(n-1)!
# def factorial(n):
#     if n==1:
#         return 1
#     t = n * factorial(n-1)
#     return t
#
# print(factorial(5))
#########################################
# 재귀
#n**m = n * n**(m-1)

# def mul(n,m):
#     if m == 1:
#         return n
#     t = n*mul(n,m-1)
#     return t
#
# print(mul(5,5))

#########################################
# 0 1 1 2 3 5 8 ...
#fibo(n) = fibo(n-1) + fibo(n-1)
# 재귀

def fibo(n):
    if n ==0 or n==1:
        return n
    t1 = fibo(n-1)
    t2 = fibo(n-2)
    return t1 + t2

print(fibo(6))
#########################################
# 메모이제이션
fi = [0]*100
fi[0] = 0
fi[1] = 1
def fibo(n):
    if n>=2 and fi[n]>0:  # 이미 계산되어 있지 않으면
        t1 = fibo(n-1)
        t2 = fibo(n-2)
        fi[n] = t1+t2
    return fi[n]

#########################################
# DP
def fibo(n):
    fi = [0]*100
    fi[0] = 0
    fi[1] = 1
    for i in range(2, n+1):
        fi[i] = fi[i-1] +fi[i-2]

    return fi[n]

