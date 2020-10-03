def inc(date):
    #Non-month end and non-feb increment
    if( (date[1] in (1, 3, 5, 6, 7, 8, 10, 12) and date[2] != 31) or (date[1] in (4, 6, 9, 11) and date[2] != 30) or date[1] != 2):
        date[2] += 1
    #month end increment
    elif( date[2] in (30, 31) ):
        if( date[1] == 12):
            date[0] += 1
            date[1] = 1
            date[2] = 1
        else:
            date[1] += 1
            date[2] =1
    else:
        if(date[2] not in (28, 29)):
            date[2] += 1
        elif( ((date[0]%4 == 0 and date[0]%100 != 0) or date[0]%400 == 0) and date[2] == 28):
            date[2] += 1
        else:
            date[1] += 1
            date[2] = 1
    #feb condition

    return date      
        
x = int(input())

while(x >= 1):
    x-=1
    tempDate = input()
    date = []
    for n in range(3):
        date.append(int(tempDate.split(':')[n]))
    while(input("Press n to stop") != "n"):
        date = inc(date)
        print(date)
    
