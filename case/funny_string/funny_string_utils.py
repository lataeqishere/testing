def funnyString(s):
    # Write your code here
    List = []
    for i in range(1,len(s)):
        List.append(abs(ord(s[i])-ord(s[i-1])))
    
    if List == list(reversed(List)):
        return "Funny"
    else :
        return "Not Funny"