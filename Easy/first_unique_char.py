class Solution:
    def firstUniqChar(self, s: str) -> int:
        character=[]
        duplicate=[]
        for letters in s:
            if(letters in character):
                duplicate.append(letters)
            else:
                character.append(letters)
        '''
        "leetcode"
        character=[l,e,t,c,o,d]
        duplicate=[e,e]
        '''
        i=0
        for letters in s:
            if(letters not in duplicate):
                return i
            i+=1
        return -1
        