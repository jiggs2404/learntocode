class Solution:
    def reverseWords(self, s: str) -> str:
        snew=s.split(' ')
        res=[]
        for word in snew:
            word=list(word)
            for i in range(len(word)//2):
                word[i], word[len(word)-1-i] = word[len(word)-1-i], word[i]
            res.append(''.join(word))
        return ' '.join(res)
            