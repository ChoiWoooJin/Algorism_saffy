# stack = [0]*3
# top = -1
#
# top += 1
# stack[top] = 10
#
# top += 1
# stack[top] = 20
#
# if top > -1:
#     top += 1
#     stack[top] = 30
#
#
# if top > -1:
#     top -= 1
#     print(stack[top+1])
# if top > -1:
#     top -= 1
#     print(stack[top+1])
# if top > -1:
#     top -= 1
#     print(stack[top+1])

####################################################
# def push(item):
#     global top
#     if top == Size-1:
#         print('overflow')
#         return -1  #혹은 0
#
#     top += 1
#     stack[top] = item
#     return 1
#
# def push(item):
#     stack.append(item)  # 위에거 정확히 알고 있을 때
#
# def peek():
#     if top == -1:
#         return -1
#
#     return stack[top]
#
#
# def pop():
#     global top
#
#     if top == -1:
#         print('underflow')
#         return -1
#
#     t = stack[top]  # 데이터 잠깐 보내놓고
#     top -= 1
#     return t
#
# def pop():
#     if len(stack) > 0:
#         return stack.pop(-1)  # 데이터가 하나도 없을 때 사용하면 오류
#
#
# def isEmpty():
#     if top == -1:
#         print('empty')
#
#
# def isFull():
#     if top != -1:
#         print('full')
#
#
#
#
# Size = 10
# stack = [-1]*Size
# top = -1  # 현재 들어 있는 마지막 위치
#
# push('a')
# print(stack)
#
# push('b')
# print(stack, top)
#
#
# r = pop()
# print(r, stack, top)
# r = pop()
# r = pop()

##########################################
#연습문제 3

input_s = '( )( )((( )))'
# input_s = '((( )((((( )( )((( )( ))((( ))))))'
# input_s = '())'
# input_s = '(()'

# 짝이 맞으면 True, 아니면 False를 return합니다.
def isPair(input_s):
    stack = []
    for c in input_s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False

            t = stack.pop(-1)
            if t != '(':
                return False
    if len(stack)>0:   # if stack: 랑 같은 의미
        return False
    return True

print(isPair(input_s))


