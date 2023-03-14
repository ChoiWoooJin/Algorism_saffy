# def enqueue(data):
#     global rear
#     rear += 1
#     queue[rear] = data
#
# def dequeue():
#     global front
#     front += 1
#     return queue[front]
#
#
# queue = [0]*3
# front = -1
# rear = -1
#
# rear += 1
# queue[rear] = 1
#
# enqueue(2)
# enqueue(3)
#
# print(dequeue())
# print(dequeue())
# if front != rear:
#     print(dequeue())
# if front != rear:
#     print(dequeue())
# ##################################################33
#
# #이렇게 하면 덩치가 큰 탐색해야 할 때 느려질 가능성이 있음
# q = []
# q.append(10)
# q.append(10)
# q.append(10)
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))
# ##################################################33
# from collections import deque
# q1 = deque()
# q1.append(10)
# q1.append(20)
# q1.append(30)
# print(q1.popleft())
# print(q1.popleft())
# print(q1.popleft())

##################################################
#마이쭈 연습문제
Q = []
no = 1
M = 20
Q.append((no, 1))   #1번 줄, 마이쭈 1개
total = 0

while Q:
    print(Q)
    curNo, curMychu = Q.pop(0) #1번이 받아감
    total += curMychu
    print(curNo, curMychu)

    if total >= M:
        break
    Q.append((curNo, curMychu+1)) #1번 줄, 마이쭈 2개
    no += 1
    Q.append((no, 1)) #2번 줄

# corNo = Q.pop(0) #1번이 받아감
# Q.append(curNo) #1번 줄
# no += 1

#####################################################



