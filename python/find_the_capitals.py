# Starter:
def capital(capitals): 
    # your code here
    pass

# Final

def capital(capitals): 
    
    new_list = []
    for obj in capitals:
        if 'state' in obj:
            sentence = f"The capital of {obj['state']} is {obj['capital']}"
            new_list.append(sentence)
        elif 'country' in obj:
            sentence = f"The capital of {obj['country']} is {obj['capital']}"
            new_list.append(sentence)

    return new_list

# Link to CodeWars: https://www.codewars.com/kata/find-the-capitals