class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        
        for i in s:
            if i == "[" or i == "{" or i == "(":
                result.append(i)
            else:
                if not result:
                    return False

                lastItem = result.pop()
                if i == "]" and lastItem != "[":
                    return False
                if i == "}" and lastItem != "{":
                    return False
                if i == ")" and lastItem != "(":
                    return False
        return len(result) == 0

        

