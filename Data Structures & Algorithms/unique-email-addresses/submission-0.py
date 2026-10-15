class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        def avant_arob(s:str):
            l = s.split("@")
            local = l[0]
            
            res = ""
            for i in range(len(local)):
                if local[i] != ".":
                    res += local[i]

            final = ""
            for i in res:
                if i != "+":
                    final += i
                else:
                    break
            return final
        
        def apres_arob(s:str):
            return s.split("@")[1]
        
        for i in emails:
            local = avant_arob(i)
            domain = apres_arob(i)
            seen.add(local+"@"+domain)
        
        return len(seen)