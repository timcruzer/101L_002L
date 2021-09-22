#CS 101 Lab
#Lab Assignment 2
#Tim Cruz
#tcc3t7@umsystem.edu
#Create a Lab grade calculator.
print('****Welcome to the LAB grade calculator! ****\n')
name=input('Who are we calculating grades for? ==> ')
labs=int(input('\nEnter the Labs grade ==> '))
if labs > 100:
    labs=100
    print('The lab value should have been 100 or less. It has been changed to 100.')
elif labs < 0:
    labs=0
    print('The lab value should have been zero or greater. It has been changed to zero.')
exams=int(input('\nEnter the EXAMS grade ==> '))
if exams > 100:
    exams=100
    print('The exam value should have been 100 or less. It has been changed to 100.')
elif exams < 0:
    exams=0
    print('The exam value should have been zero or greater. It has been changed to zero.')
a=int(input('\nEnter the Attendance grade ==> '))
if a > 100:
    a=100
    print('The attendance value should have been 100 or less. It has been changed to 100.')
elif a < 0:
    a=0
    print('The attendance value should have been zero or greater. It has been changed to zero.')
grade = labs*.7+exams*.2+a*.1
print(f'\nThe weighted letter grade for {name} is {grade}')
if grade >= 90:
    print(f'{name} has a letter grade of A')
elif grade <=89.9 and grade >=80:
    print(f'{name} has a letter grade of B')
elif grade <=79.9 and grade >=70:
    print(f'{name} has a letter grade of C')
elif grade <=69.9 and grade >=60:
    print(f'{name} has a letter grade of D')
else:
    print(f'{name} has a letter grade of F')
print('\n**** Thanks for using the Lab grade calculator ****')
