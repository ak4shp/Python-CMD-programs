# DAY_01_1
'''
t1 = 0
t2 = 0
t3 = 0
i = 0
while(i < 9):
    k = int(input())
    
    if (k >= 1 and k <= 100):
        if (i == 0 or i == 3 or i == 6):
            t1 = t1 + k
        
        elif (i == 1 or i == 4 or i == 7):
            t2 = t2 + k

        elif (i == 2 or i == 5 or i == 8):
            t3 = t3 + k

        else:
            print("Invalid input!")

    i += 1

a1 = round(t1 / 3)
a2 = round(t2 / 3)
a3 = round(t3 / 3)
m = max(a1, a2, a3)

if (a1 <= 70 and a2 <= 70 and a3 <= 70):
    print("All trainees are unfit")
if (a1 >= a2 and a1 >= a3):
    print("Trainee Number: 1")
if (a2 >= a1 and a2 >= a3):
    print("Trainee Number: 2")
if (a3 >= a1 and a3 >= a2):
    print("Trainee Number: 3")

print("max oxygen level :", m)
'''



# DAY_01_2
'''
low = int(input())
hi = int(input())

for i in range(low, hi + 1):
    if (i > 0 and i < 10) :
        print("{:02d}".format(i), end = " ")
    elif (i >= 10):
        print("{:03d}".format(i), end = " ")
    else:
        print("Invalid Input")
'''



# DAY_01_3

N = int(input("Total Candies: "))
minLimit = int(input("Minimum Limit: "))
candies = N    

while(candies > 0):
    n = int(input("\nI want -> "))
    
    if (n <= candies):
        candies = candies - n
        print("Number of Candies Sold: ", n)
        print("Number of Candies available: ", candies)
    else:
        print("INVALID INPUT\n   There are only {} Candies". format(candies))

    if (candies <= minLimit):
        print("\nMinimum limit reached!!\nResetting JAR...")
        candies = N
        print("JAR is filled with {0} Candies".format(N))



        


