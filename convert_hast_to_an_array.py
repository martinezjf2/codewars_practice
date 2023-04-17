# Starter

def convert_hash_to_array(hash):
    #your code here - sort the keys
    pass



# Final

def convert_hash_to_array(hash):
    
#   print(hash)
    
#   Step 1: Create an empty list so that when iterating through each key/value pair, we will append the new list to this main list
    main_list = []
    
#   Step 2: Sort the pairs within the dictionary based on the key
    hash_to_list = list(hash.keys())
    hash_to_list.sort()
    print(hash_to_list)
    sorted = {i: hash[i] for i in hash_to_list}
    print(sorted)
    
#   Step 3: Iterate through the keys and values
    for key in sorted:
#       print(key)

#       Step 4: create a new list for each key and value pair
        new_list = [key, sorted[key]]
#       print(new_list)

#       Step 5: Append that new list within the main global List
        main_list.append(new_list)

#   Step 6: After the loop finishes, return the main global list
    return main_list

# Resources:

# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/



# Link to CodeWars: https://www.codewars.com/kata/convert-hash-to-an-array