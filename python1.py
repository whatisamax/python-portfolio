def get_scores():
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    return score1,score2,score3

def average(score1,score2,score3):
    average = (score1+score2+score3)/3
    return average

def grade(average):
    if average>=90:
        return 'A'
    elif 90>average>=80:
        return 'B'
    elif 80>average>=70:
        return 'C'
    elif 70>average>=60:
        return 'D'
    else:
        return 'F'

def summary(average,grade):
    return f'Your average is' + str(average) +str(grade)
    
score1,score2,score3 = get_scores()
avg = average(score1,score2,score3)
grade_msg = grade(average)
summary_msg = summary(average,grade)
print(summary)

