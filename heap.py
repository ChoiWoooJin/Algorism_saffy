# # 최대 100개의 key
# # 최대 힙
#
# def enq(n):
#     global last
#     last += 1  # 완전이진트리에 마지막 정점을 추가하고
#     heap[last] = n  # 마지막 정점에 저장
#     c = last  # 부모가 있고, 부모 > 자삭 조건 검사를 위해
#     p = c//2
#     while p>0 and heap[p] < heap[c]:
#         heap[p], heap[c] = heap[c], heap[p]
#         c = p  # 옮긴 자리에서 부모와 비교하기 위해
#         p = c//2
#     return
#
# def deq():  # 힙에서의 삭제
#     global last
#     tmp = heap[1]  # 루트 임시 저장 (루트 버리면 안됨)!!!!!!
#     heap[1] = heap[last]  # 마지막 정점의 값을 루트로 이동
#     last -= 1  # 마지막 정점 삭제
#     p = 1  # 루트를 부모로 넣고
#     c = p * 2  # 왼쪽 자식 번호
#     while c <= last:  # 자식이 하나 이상 있으면
#         if c+1 <= last and heap[c] < heap[c+1]:  # 오른쪽 자식도 있고 오른쪽 자식의 키가 더 크면
#             c += 1  # 비교대상을 오른쪽 자식으로 변경
#         if heap[c] > heap[p]:  # 자식이 부모보다 크다면
#             heap[c], heap[p] = heap[p], heap[c]
#             p = c
#             c = p * 2
#         else:
#             break
#     return tmp
#
#
# heap = [0] * 101   # 완전이진트리 1번-100번 인덱스 준비
# last = 0   # 완전이진트리의 마지막 정점 번호
#
# enq(5)
# print(heap[1])
# enq(15)
# print(heap[1])
# enq(8)
# print(heap[1])
# enq(20)
# print(heap[1])
#
# while last>0:
#     print(deq())


##########################################################
# def insert(item):
#     pos = 1
#     while tree[pos] != 0:
#         if tree[pos] == item:
#             return
#         if tree[pos] < item:
#             pos = pos*2 + 1
#         else:
#             pos = pos*2
#     tree[pos] = item
#
#
# def find(key):
#     pos = 1
#     while tree[pos] != 0:
#         if tree[pos] ==key:
#             return pos
#         if tree[pos] < key:
#             pos = pos*2 +1
#         else:
#             pos = pos*2
#     return -1
#
# tree = [0]*100
# lst = [9,4,12,3,6,15,13,17]
# for item in lst:
#     insert(item)
#     print(tree)
#
# insert(5)  # 삽입
# print(tree)
# print(find(12))
# print(find(17))
# print(find(6))
# print(find(121))
# print(find(21))


###########################################################################
# import heapq
# h = []
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     heapq.heappush(h, item)
#
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))

###########################################################################
# 최대 힙(인큐)
# def enq(item):
#     global last
#
#
#     last += 1
#     tree[last] = item
#     c = last
#     p = c//2
#     while p>=1 and tree[c] > tree[p]:
#         tree[c], tree[p] = tree[p], tree[c]
#         c = p
#         p = c//2


# tree = [0] *100
# last = 0
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     enq(item)
#     print(tree)
#
# enq(23)
# print(tree)

############################################################################
# # 최소 힙(인큐)
def enq(item):
    global last


    last += 1
    tree[last] = item
    c = last
    p = c//2
    while p>=1 and tree[c] < tree[p]:
        tree[c], tree[p] = tree[p], tree[c]
        c = p
        p = c//2
#
#
# tree = [0] *100
# last = 0
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     enq(item)
#     print(tree)
#
# enq(23)
# print(tree)
############################################################################
#최대 힙(디큐)
# def deq():
#     global last
#     tmp = tree[1]
#     tree[1] = tree[last]
#     last -= 1
#     p = 1
#     c = p*2  # 프로그램 편의를 위해 가정하고 진행
#     while c <=last:  # p가 자식노드가 하나라도 있는 동안 , 자식노드가 없다는 얘기는 비어있단 뜻
#         if c<=last and tree[c] < tree[c+1]:     # 오른쪽 자식노드가 있으면 and 오른쪽 노드가 더 크면 (왼쪽하고 오른쪽하고 비교해서 더 큰거 넣어줌)
#             c += 1
#
#         if tree[p] < tree[c]:  # heap이 깨졌으면
#             tree[p], tree[c] = tree[c], tree[p]
#             p = c
#             c = p*2
#
#         else:
#             break
#     return tmp
#
#
#
# tree = [0] *100
# last = 0
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     enq(item)
#     # print(tree)
#
# enq(23)
# # print(tree)
#
# print(deq())
# print(last, tree)
# print(deq())
# print(last, tree)
# print(deq())
# print(last, tree)



###########################################################
# 최소 힙(디큐)
def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = p * 2  # 프로그램 편의를 위해 가정하고 진행
    while c <= last:  # p가 자식노드가 하나라도 있는 동안 , 자식노드가 없다는 얘기는 비어있단 뜻
        if c <= last and tree[c] > tree[c + 1]:  # 오른쪽 자식노드가 있으면 and 오른쪽 노드가 더 크면 (왼쪽하고 오른쪽하고 비교해서 더 큰거 넣어줌)
            c += 1

        if tree[p] > tree[c]:  # heap이 깨졌으면
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2

        else:
            break
    return tmp


tree = [0] * 100
last = 0
lst = [15, 4, 13, 20, 11, 19]
for item in lst:
    enq(item)
    # print(tree)

enq(23)
# print(tree)

print(deq())
print(last, tree)
print(deq())
print(last, tree)
print(deq())
print(last, tree)
