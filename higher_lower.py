

import Testing

ask_answer = int(input('What should the answer be? '))

attempt_limit = int(input('How many guesses? '))


guess_attempt = int(input('Guess a number: '))

guesses = 0

if ask_answer == -1:
    ask_answer = Testing.randrange(0, 101)

while guess_attempt != ask_answer and guesses < attempt_limit:
    guesses += 1

    if guesses < attempt_limit:
        if guess_attempt > ask_answer:
            print('The number is lower than that.')
            guess_attempt = int(input('Guess a number: '))
        elif guess_attempt < ask_answer:
            print('The number is higher than that.')
            guess_attempt = int(input('Guess a number: '))

if guess_attempt == ask_answer:
    print('You Win')

else:
    print('You lose, the number was', ask_answer)
