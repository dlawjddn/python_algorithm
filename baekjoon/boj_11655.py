string = input()
new_string = ''
for char in string:
    if char.islower():
        new_string += chr(ord('a') + (ord(char) - ord('a') + 13) % 26)
    elif char.isupper():
        new_string += chr(ord('A') + (ord(char) - ord('A') + 13) % 26)
    else:
        new_string += char

print(new_string)