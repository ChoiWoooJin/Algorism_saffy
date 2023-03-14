# 트리
""" def preOrder(root):
    print(root)
    if len(TREE[root]):
        preOrder(TREE[root][0])
    if len(TREE[root]) == 2:
        preOrder(TREE[root][1])

def inOrder(root):
    if len(TREE[root]):
        inOrder(TREE[root][0])
    if len(TREE[root]) ==2:
        inOrder(TREE[root][1])
    print(root)

N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))

TREE = [[] for _ in range(N+1)]
for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]

TREE[p].append(c)
inOrder(1) """

# 왼쪽과 오른쪽의 자식노드 구별
""" def preOrder(root):
    if root:
        print(root)

    #if leftC[root]:
    preOrder(leftC[root])
    #if rightC[root]:
    preOrder(rightC[root])
def findA(c):
    while c!=0:
        print(parent[c])
        c = parent[c]

N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))

leftC = [0] * (N+1)
rightC = [0] * (N+1)
parent = [0]*(N+1)

for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]

parent[c] = p
if leftC[p] == 0:
    leftC[p] = c
else:
    rightC[p] = c
preOrder(1)
findA(10) """

""" def inOrder(rootIdx):
    if lst[rootIdx]:
        inOrder(rootIdx2)
        print(lst[rootIdx])
        inOrder(rootIdx2+1) """

""" def inOrder(rootIdx):
    if rootIdx < len(lst):
        inOrder(rootIdx2)
        print(lst[rootIdx])
        inOrder(rootIdx2+1)

lst = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
print(lst)
inOrder(1) """