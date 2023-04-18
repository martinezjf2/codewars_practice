# Starter

def first_non_repeated(s):
    pass


# Final

def first_non_repeated(s):
    for a in s:
        if s.count(a) == 1:
            return a
    return None

# Link to Codewars: https://www.codewars.com/kata/the-first-non-repeated-character-in-a-string