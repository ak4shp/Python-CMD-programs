k = input("Ent: ")

# if k > 1 :
#     print(k)
try:
    if (not isinstance(int(k), int)):
        print("not int")
    else: 
        print(type(k))
        print("Not")

except(ValueError):
    print("Enter int only")
