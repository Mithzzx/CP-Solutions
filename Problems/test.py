class Solution:
    def minimumPushes(self, word: str) -> int:
        word = "abcde"
        d = {'a': 1}
        print(d['a'])
        for i in word:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        print(d)
        dd = {}
        l = []
        for key in d:
            if d[key] in dd:
                dd[d[key]].append(key)
            else:
                dd[d[key]] = [key]
                l.append(d[key])
        l.sort(reverse=True)
        print(dd, l)

        count = 0
        x = 0
        print(9 // 8)
        for i in l:
            for j in dd[i]:
                print(j, i, count // 8 + 1)
                x += i * (count // 8 + 1)
                count += 1
                print(x)

        return x-1
