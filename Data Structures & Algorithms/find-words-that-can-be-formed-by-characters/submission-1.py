class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        freq1 = {}

        for i in chars:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        
        for word in words:
            freq2 = {}
            valid = True

            for j in word:
                if j not in freq1:
                    valid = False
                    break
                else:
                    if j in freq2:
                        freq2[j] += 1
                    else:
                        freq2[j] = 1
                    if freq2[j] > freq1[j]:
                        valid = False
                    
            if valid:
                res += len(word)

        return res