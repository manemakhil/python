T = int(input())

while T>0:
    S = input()
    A = []
    A.append(S[0])
    A.append(1)
    check = 0

    for n in range(1, len(S)):
        if(S[check] == S[n]):
            A.append(int(A.pop()) + 1)
        else:
            A.append(str(A.pop()))
            A.append(S[n])
            A.append(1)
            check = n
    A.append(str(A.pop()))

    if(len(''.join(A)) < len(S)):
        print("YES")
    else:
        print("NO")
    T = T - 1
