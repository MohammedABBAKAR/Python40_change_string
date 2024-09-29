
# todo Change the Word
# ? Given a string, reverse its order, change lowercase letters to uppercase and 
# ? increment uppercase letters by one (e.g. A becomes B, C becomes D, Z becomes A).

# * Examples
# * change_string("ApPle") ➞ "ELQPB"

# * change_string("draGON") ➞ "OPHARD"

# * change_string("ZebrA") ➞ "BRBEA"
# ! Notes
# ? Remember capital "Z" becomes "A".



# def change_string(word):
#      uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#      reversed_string = word[::-1]
#      for x in reversed_string:
#           if x.isupper():
#                return x
# print(change_string("ApPle"))


def change_string(s):
    result = []
    # Reverse the string
    s = s[::-1]
    
    # Iterate through each character in the reversed string
    for char in s:
        if char.islower():
            # Convert lowercase to uppercase
            result.append(char.upper())
        elif char.isupper():
            # Increment uppercase letters and handle the special case for 'Z'
            if char == 'Z':
                result.append('A')
            else:
                result.append(chr(ord(char) + 1))
    
    # Join the result list into a string and return it
    return ''.join(result)

# Test cases
print(change_string("ApPle"))  # ➞ "ELQPB"
print(change_string("draGON"))  # ➞ "OPHARD"
print(change_string("ZebrA"))  # ➞ "BRBEA"
