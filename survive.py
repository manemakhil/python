# N choclates in a box you can buy everyday. You can buy one box.
# K is the number of choclates to be eaten per day
# S is the number of days to survive
for a in range (int(input())):
    N, K, S = map(int, input().split(" "))

    need = S*K
    stock = 0
    days = 0
    
    if(N*6>=K*7):
        while stock<need:
            days = days + 1

            if(S%7!=0):
                stock = stock + N - K
            else:
                stock = stock - K

        print(days)
    else:
        print(-1)