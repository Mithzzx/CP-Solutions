class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        sl = sentence.split(" ")
        for i in dictionary:
            for ind, j in enumerate(sl):
                print((i, j))
                if i in j[0:len(i)]:
                    print([i, "=", j])
                    sl[ind] = i

        return ' '.join(sl)