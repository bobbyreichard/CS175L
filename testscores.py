#define test scores
score1 = int(input('Enter a score for test 1: '))
score2 = int(input('Enter a score for test 2: '))
score3 = int(input('Enter a score for test 3: '))
score4 = int(input('Enter a score for test 4: '))
score5 = int(input('Enter a score for test 5: '))
#calclulate average
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5)/5

    return average
#determine grades
def grade(score1, score2, score3, score4, score5):
    for i in score1, score2, score3, score4, score5:
        if 90 <= i:
            print('The grade of', i, 'is A')
        elif 80 <= i:
            print('The grade of', i, 'is B')
        elif 70 <= i:
            print('The grade of', i, 'is C')
        elif 60 <= i:
            print('The grade of', i, 'is D')
        elif 60 > i:
            print('The grade of', i, 'is F')
#final prints
average = calc_average(score1, score2, score3, score4, score5)
print('The average of the test scores is', average)
grade(score1, score2, score3, score4, score5)
