# def LongestPalindrome(string):
#     max_len=0
#     for i in range (len(string)):
#         #The center is at a single character(odd)
        
#         left = right = i
        
#         while left >= 0 and right < len(string) and string[left] == string[right]:
#             left -= 1
#             right += 1
#         len1 = right - left - 1
        
#          #The center is between two characters(even)
#         left = i
#         right = i + 1
#         while left >= 0 and right < len(string) and string[left] == string[right]:
#             left -= 1
#             right += 1
#         len2 = right - left - 1
#         cur_len = max(len1, len2)
#         max_len=max(max_len,cur_len) 
#     return max_len

# string=input("enter string: ")
# print(LongestPalindrome(string))

def longest_palindromic_substring(s):
    res=1
    str_res=s[0]
    for i in range(0,len(s)):
        #odd polindromes
        left=i
        right=i
        while(left>=0 and right<len(s) and s[left]==s[right]):
            if(right-left+1>res):
                res=right-left+1
                str_res=s[left:right+1]
                # print(str_res)
            left-=1
            right+=1
        #even polindromes
        left=i
        right=i+1
        while(left>=0 and right<len(s) and s[left]==s[right]):
            if(right-left+1>res):
                res=right-left+1
                str_res=s[left:right+1]
                # print(str_res)
            left-=1
            right+=1
        
    return str_res
s=input()
print(longest_palindromic_substring(s))