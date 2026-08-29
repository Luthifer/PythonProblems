'''Goal is, to create a letter grading based
on the score given by the user.'''



def letter_grade(score):
    '''A function that gives back grades  based on the
    score'''
    if score >= 89:
        if score >= 107:
            return "A+"
        else:
            return 'A'
    elif score >=45:
        if score <=62:
            return 'C-'
        else:
            return 'C'
    else:
        return 'F'

print(letter_grade(50))
print(letter_grade(90))
print(letter_grade(108))
