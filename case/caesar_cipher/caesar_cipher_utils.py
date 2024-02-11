def caesarCipher(s, k):
    # Write your code here
    out = ''
    for letter in s:
        if letter.isalpha():
            upper_lower = 'A' if letter.isupper() else 'a'
            out += chr(ord(upper_lower) + (ord(letter) - ord(upper_lower) + k) % 26)
        else:
            out += letter
    return out