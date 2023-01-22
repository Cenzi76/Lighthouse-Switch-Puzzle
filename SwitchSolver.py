#Plus values:
begin = input("enter your current number: ")
beginarr = [*begin]
end = input("enter desired number: ")
endarr = [*end]

def Plusvalue(start,finish)
    for i in start and finish
        num1 = int(start[i])
        num2 = int(finish[i])
        if num1 > num2:
            num2 += 10
            #count is the plus value, like poker
            count = num2 - num1
        elif num1 < num2:
            count = num2 - num1
        else:
            count = 0
            
print(Plusvalue(beginarr,endarr))
