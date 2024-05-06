print('Welcome to the Quiz !')

playing = input('Would you like to play? ')
if playing.lower() != 'yes':
    quit()

print('Thanks for playing! :) ')
score = 0

answer = input('What is the currency of India ?  ')
if answer.lower() == 'rupee':
    print('Correct !')
    score += 1
else:
    print('Incorrect !')

answer = input('Who created Bitcoin ?  ')
if answer.lower() == 'satoshi nakamoto':
    print('Correct !')
    score += 1
else:
    print('Incorrect !')

answer = input('Which is the largest organ in the human body ?  ')
if answer.lower() == 'skin':
    print('Correct !')
    score += 1
else:
    print('Incorrect !')

answer = input('Which is the largest flower in the world ?  ')
if answer.lower() == 'rafflesia':
    print('Correct !')
    score += 1
else:
    print('Incorrect !')

answer = input('How many continents are there in the world ?  ')
if answer.lower() == '7' or answer.lower() == 'seven':
    print('Correct !')
    score += 1
else:
    print('Incorrect !')

print('You got ' + str(score) + ' questions correct !')
print('You got ' + str((score / 5) * 100) + '%')
