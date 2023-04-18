# Starter

def create_dict(keys, values):
    """
    Write your code here.
    """
    pass

# Final

def create_dict(keys, values):  
    while len(keys) > len(values):
        values.append(None)
    dic = dict(zip(keys, values))
    return dic

# Link to CodeWars: https://www.codewars.com/kata/5533c2a50c4fea6832000101