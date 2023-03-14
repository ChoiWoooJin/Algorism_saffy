# nums = [1,4,1,3,1,2,4,1]
# cnt1 = cnt2 = 0
# for num in nums:
#     if num == 1:
#         cnt1 += 1
#
#     if num == 1:
#         cnt2 += 1
#
# cnt[0] => 0의개수
# cnt[1] => 1의개수
# cnt의 공간은 몇개?

K = 4
N = 8
nums = [0,4,1,3,1,2,4,1]
res = [-1] * N
counts = [0] * (K+1)
for num in nums:
    counts[num] += 1
print(counts)

for i in range(K):
    counts[i+1] = counts[i+1] + counts[i]

print(counts)

for i in range(N-1,-1,-1):
    num = nums[i]
    pos = counts[num]-1
    res[pos] = num
    counts[num] -= 1

print(res)


