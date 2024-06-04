s = "bb"
lis = {x: int(s.count(x)) for x in s}
l = list(lis.values())
single = True
x = 0
for i in l:
    if i >= 2:
        x += (i - i % 2)
        i = 1
    if single and i == 1:
        single = False
        x += 1

print(x)
