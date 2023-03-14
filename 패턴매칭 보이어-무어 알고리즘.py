T = "This pattern matching algorithms"

def bmoor(P):
    lenP = len(P)
    lenT = len(T)
    # 점프 몇번할건지
    SKIP = [len(P)] * 128
    for i in range(lenP - 1):
        # P의 시작점 P[i]
        SKIP[ord(P[i])] = lenP - 1 - i
    # 점프할 숫자 print(SKIP[ord('p')])

    idxT = 0
    # for문은 한번씩 가게되므로 사용 못함
    while idxT + lenP <= lenT:
        # 인덱스는 뒤부터 조사하기로했으니까

        idxP = lenP - 1
        while idxP >= 0 and T[idxT + idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:
            return idxT
        # ascii = ord(T[idxT+idxP])
        # j = SKIP[ascii]
        idxT += SKIP[ord(T[idxT + idxP])]
    return -1

print(bmoor('pat'))
print(bmoor('algor'))