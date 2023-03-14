#연습문제 1
'''
00000001111000000110000001111100110000110000111100111100111111001100111
'''
# arr = list(map(int, input()))
# print(len(arr))
# N = len(arr)
# num = 0
# for i in range(N):
#     j = i % 7
#     num += arr[i] * (2**(6-j))
#     if j==6:
#         print(num, end = ' ')
######################################################################
#연습문제 2
'''
0F97A3
'''
def hexTobin2(s):
    mapping = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
               '4':'0100', '5':'0101', '6':'0110', '7':'0111',
               '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
               'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
    }
    return mapping[s]
#
a = input()
lis = []
for i in a:
    lis.append(hexTobin2(i))
# print(lis)
lis = ''.join(lis)
print(lis)
# print(lis.index('1'))

N = len(lis)
for idx in range(0, N, 7):
    for i in range(7):





# # lis2 = []
# num = 0
# for i in range(N):
#     j = i % 7
#     num += int(lis[i]) * (2**(6-j))
#     if j==6:
#         print(num, end = ' ')
#         num = 0





#######################################################################
#이진수로 바꾸기
'''
01D06019861D79F99F
'''
# arr = input()
# for x in arr:
#     num = int(x, 16)
#     for j in range(3, -1 , -1):
#         bit = 1 if num&(1<<j) else 0
#         print(bit, end = '')
#     print(' ' , end = '')


#################################################
# a = 0x10203040
# print(a)


#################################################
# s = 'F'
# def hextodec(s):
#     if s.isdigit():
#         return int(s)
#     else:
#         return ord(s) - ord('A') +10

#위에 함수랑 같은 기능
# print(int(s,16)) # s 뒤에 진수 입력 가능
# a = int(s,16)
# print(bin(a))

##################################################

# a = 0.0625
# for i in range(100):
#     a += 0.1
#     print(a) #근사치  (실수 두개가 같으냐라는 대소비교 잘 안됨) -> 해결방법 : 두개의 실수 뺴서 허용각 안에 들어오느냐 확인