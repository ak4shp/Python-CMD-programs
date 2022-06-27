# Candy Shop -> Displays sold and remainning candies at an instance.

N = int(input("Total Candies: "))
minLimit = int(input("Minimum Limit: "))
candies = N    

while(candies > 0):
    k = input("\nI want -> ")
    try:
        if (not isinstance(int(k), int)):
            continue
        else:
            n = int(k)
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

    except ValueError:
        print("Please Enter only Integers!\nQuitting..... :)")
        break

