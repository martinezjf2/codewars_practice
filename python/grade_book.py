
# Starter Code:

def get_grade(s1, s2, s3):
    return 'F'


# Final Code:
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3

    if average >= 90 and average <= 100:
        return 'A'
    elif average >= 80 and average < 90:
        return 'B'
    elif average >= 70 and average < 80:
        return 'C'
    elif average >= 60 and average < 70:
        return 'D'
    elif average < 60:
        return 'F'
    
    
# Link to Codegrade: https://www.codewars.com/kata/grasshopper-grade-book