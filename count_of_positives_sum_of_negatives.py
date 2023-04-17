# Starter

def count_positives_sum_negatives(arr):
    pass

# Final

def count_positives_sum_negatives(arr):
    total_of_negative_numbers = 0
    how_many_positives = 0
    if arr:
        for x in arr:
            if x > 0:
                how_many_positives += 1
            elif x < 0:
                total_of_negative_numbers += x
    else:
        return []
            
    return [how_many_positives, total_of_negative_numbers]

# Link to codewars: https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives