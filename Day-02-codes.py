# Day-02-1
'''
n, ln = map(int, input().split())
prev = n
sm = 0
if (n > 2 and n < 10) and (ln > 1 and ln < 20):
    for i in range(ln):
        prev = n - 1
        sm = n + prev
    print(sm)
else:
    print("INPUT OUT OF RANGE")
'''


# Day-02-2
'''
a = input()
b = input()
c = input()

sample = ["a", "e", "i", "o", "u"]
res1 = ""
res2 = ""
res3 = ""
for i in a:
    if i in sample:
        res1 = res1 + "*"
    else:
        res1 = res1 + i

for i in b:
    if i not in sample:
        res2 = res2 + "@"
    else:
        res2 = res2 + i

res3 = c.upper()

print(res1 + res2 + res3)
'''
