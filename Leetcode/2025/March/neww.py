skill = [1,1,1]
mana = [1,1,1]



t = 0
st = 0

def compute(s,j):
    global st
    for i in range(len(skill)-2, -1, -1):
        s -= (skill[i] * mana[j])
    if s>st:
        st = s
    else:
        st += (skill[0] * mana[j-1])+1

for i in range(len(mana)):
    for j in range(len(skill)):
        t += (skill[j] * mana[i])
    compute(t,min(len(mana)-1,i+1))
    if i < len(mana)-1: t = st

print(t)


