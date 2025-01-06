nums = [1,2,3,3]
n = len(nums) /2
s={}
for i in nums:
    if i in s:
        s[i] += 1
        if s[i] == n: print(i)
    else:
        s[i] = 1