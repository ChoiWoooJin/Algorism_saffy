'''
5
55 7 78 12 42
for i : N-1 -> 1 #각 구간의 끝
    for i : 0 -> i-1  # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1]  # 큰 원소 오른쪽으로
##################################################
교수님 코드
i=4:
   [55, 7, 78, 12, 42] 0-1: [7, 55, 78, 12, 42]
   [7, 55, 78, 12, 42] 1-2: [7, 55, 78, 12, 42]
   [7, 55, 78, 12, 42] 2-3: [7, 55, 12, 78, 42]
   [7, 55, 12, 78, 42] 3-4: [7, 55, 12, 42, 78]
i=3
   [7, 55, 12, 42, 78] 0-1: [7, 55, 12, 42, 78]
   [7, 55, 12, 42, 78] 1-2: [7, 12, 55, 42, 78]
   [7, 12, 55, 42, 78] 2-3: [7, 12, 42, 55, 78]
i=2
i=1
i=0
# i가 달라질 수록 비교 횟수가 달라질 것

i=i: -> 0부터 i-1까지
for i in range(N-1, 0, -1):
   for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(*nums) # *는 언패킹
'''

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):  # 각 구간의 끝
    for j in range(0, i):     # 정렬될 구간의 끝
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)


# 자율 실습. 끝부터 채우기, 0번째부터 채운다면, 작은수에서 큰수로 bubble 정렬





