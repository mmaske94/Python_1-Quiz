print('Welcome To The Harry Ptter Quiz')

playing = input('Do You Want To Play? ')

if playing.lower() != "yes":
    quit()
print ('Okay! Put Yur Sorting Hat On ')
score = 0

house = input('Choose Your House ')

answer = input("Who is Harry's Godfather? ")
if answer == 'Sirius Black':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

answer = input("What is Voldemort's Real Name? ")
if answer == 'Tom Marvolo Riddle':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

answer = input("What is the British Term for Non-Magical Person? ")
if answer == 'Muggle':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

answer = input("What Magazine doez Xenophilius Lovegood Publish? ")
if answer == 'The Quibbler':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

answer = input("What Incantation can Levitate Objects? ")
if answer == 'Wingardium Leviosa':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

answer = input("What is the Name of Hargrid's Pet Dragon? ")
if answer == 'Norbert':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

answer = input("What Potion gives Good Luck to those who Drink It? ")
if answer == 'Felix Felicis':
    print(f'Ten Points To {house}')
    score +=  10
else:
    print('Ten Points Lost')

print('You got ' + str(score) + ' points!!!')