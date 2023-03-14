# def bf2(p, t, N, M):
#     for i in range(N-M+1):
#         for j in range(M):
#             if t[i+j] != p[j]:
#                 break
#         else:
#             return i
#     return -1
#
# print(bf(p,t,N,M))
T = "This pattern matching algorithms"

def brute(P):
    lenP = len(P)
    lenT = len(T)
    for idxT in range(0, lenT-lenP+1):
        idxP = 0
        while idxP<lenP and T[idxT +idxP] == P[idxP]:
            idxP += 1
        if idxP == lenP:
            return idxT

    return -1


T = "This pattern matching algorithms"

print(brute('patt'))
print(brute('aaaa'))

#print(T.find('patt'))
#print(T.find('aaaa'))









