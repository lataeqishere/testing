def alternate(s):
    # Write your code here
    char_list = list(set(s))

    maximum = 0
    for i in range(len(char_list)):
        for j in range(i+1, len(char_list)):
            z = ""
            for k in range(len(s)):
                if s[k] == char_list[i] or s[k] == char_list[j]:
                    z += s[k]
            if len(z) > maximum and len(set(z[::2])) == 1 and len(set(z[1::2])) == 1:
                maximum = len(z)
    return maximum