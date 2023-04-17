# Starter:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    pass

# Final:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    new_list = []
    for bird in birds:
        if bird not in geese:
            new_list.append(bird)
#   print(new_list)
    return new_list

# Link to CodeWars: https://www.codewars.com/kata/filter-out-the-geese