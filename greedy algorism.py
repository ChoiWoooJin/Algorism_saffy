#Baby-gin Game

# list(map(int, input().split())) '444555'리스트로
# list(map(int, input()))   -> 444555리스트로


s = '444345'
l = list(map(int,s))
print(l)

counts = [0] * 10
for num in l:
    counts[num] += 1

print(counts)

tri = 0
run = 0
i = 0
while i<10:
    if counts[i] >= 3:
        counts[i] -= 3
        continue
    elif counts[i]>0 and counts[i+1]>0 and counts[i+2]>0:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue
    i += 1
print(tri, run)