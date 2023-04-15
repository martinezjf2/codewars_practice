# Starter

def make_string(s):
    # Your code here
    pass

# Final

def make_string(s):
    words = s.split(' ')
    newList = []
    for word in words:
        newList.append(word[0])
    return ''.join(newList)


# Link to codewars: https://www.codewars.com/kata/return-string-of-first-characters