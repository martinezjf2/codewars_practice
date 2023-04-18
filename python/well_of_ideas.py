# Starter

def well(x):
    pass

# Final

def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"

# Link to codewars: https://www.codewars.com/kata/well-of-ideas-easy-version