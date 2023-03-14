'''
blocks = [7, 4, 2, 0, 0, 6, 0, 7, 8]
N = len(blocks)
i = 0:
    blocks[0] (7) 보다 작은 갯수를 센다. 범위는 1~N-1


i = 1:
   blocks[1] (4) 보다 작은 갯수를 센다. 범위는 2~N-1

i = 2:
   2

i:
   blocks[i] 범위는 i+1~N-1

'''
blocks = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(blocks)
a = 0
res = [0] * N

# # 1. 상단에 있는 블럭의 낙차를 구하여 저장
# for i in range(0, N):
#     cnt = 0
#     for j in range(i+1, N):
#         if blocks[i] > blocks[j]:
#             cnt += 1
#     res[i] = cnt
#
#     print(res)
#
# # 2. 저장된 낙차 중 제일 큰 값을 구한다.
#
# ma = 0
# for s in res:
#     if s > ma:
#         ma = s
# print(ma)


#####################################################
# 한번에
ma = 0
for i in range(0, N):
    cnt = 0
    for j in range(i+1, N):
        if blocks[i] > blocks[j]:
            cnt += 1

    if ma < cnt:
        ma = cnt

print(ma)







