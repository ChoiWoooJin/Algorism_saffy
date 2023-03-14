#<연습문제>
exp = '2+3*4/5'
# goal = '234*5/+'
isp = {'+':1, '-':1, '*':2, '/':2}  #우선순위 만들어주기

ST = [ ]
for c in exp:
    if c.isdigit():    #숫자면 그냥 출력
        print(c)
    else:
        if len(ST)>0 and isp[ST[-1]] > isp[c]:
            print(ST.pop())
            ST.append(c)
        else:
            ST.append(c)

while ST:
    print(ST.pop())

##########################################
#<연습문제>
# exp = '(6+5*(2-8)/2)'
# goal = '6528-2/*+'
# def step1(exp):
#     isp = {'+':1, '-':1, '*':2, '/':2, '(':0}  #우선순위 만들어주기
#     icp = {'+':1, '-':1, '*':2, '/':2, '(':3}  #왼쪽 가로 때문에 우선순위 2개
#     ST = [ ]
#     result =[]
#     for c in exp:
#         if c.isdigit():    #숫자면 그냥 출력
#             result.append(c)
#         # elif '(':   처리되서 필요없음
#
#         elif c == ')':
#             while ST and ST[-1] != '(':  #while ST: -> while len(ST)>0:
#                 result.append(ST.pop())
#             ST.pop()
#
#         else:
#             if len(ST)>0 and isp[ST[-1]] > icp[c]:
#                 print(ST.pop())
#                 ST.append(c)
#             else:
#                 ST.append(c)
#
#     while ST:
#         result.append(ST.pop())
#
#     return result
#
# def cal(v1, v2, op):
#     if op == '+':
#         return v1+v2
#     if op == '-':
#         return v1-v2
#     if op == '*':
#         return v1*v2
#     if op == '/':
#         return v1//v2
#
# def step2(exp):
#     ST =[]
#     for c in exp:
#         if c.isdigit():
#             ST.append(int(c))
#         else:
#             v2 = ST.pop()
#             v1 = ST.pop()
#             ST.append(cal(v1, v2, c))
#
#     return ST[-1]
#
#
# exp = '(6+5*(2-8)/2)'
# post = step1(exp)
# # print(post)
# print(step2(post))



