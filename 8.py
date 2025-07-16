class Solution:
    def myAtoi(self, s: str) -> int:
        char_str = '-+'
        num_check= set('0123456789')
        
        int_min, int_max = -2**31, 2**31-1
        s =s.strip()
        i = 0
        neg = 1
        num = 0

        print(len(s))
        if i< len(s) and s[i] not in char_str and s[i] not in num_check:
            return 0
        
        if i < len(s) and s[i] in char_str and s[i] == '-':
            neg = -1
            i+=1
        elif i < len(s) and s[i] in char_str and s[i] == '+':
            neg ==1
            i+=1

        while i < len(s):
            if s[i] in num_check:
                num = num*10 + int(s[i])
            else:
                break
            i +=1

        if neg ==-1:
            return max(int_min, neg*num)
        else: 
            return min(int_max, num)

s = Solution()
print(s.myAtoi(''))



        
