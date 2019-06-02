

print("Think of a number between 1 and 100 and I'll guess it")

attempt_limit = int(input('How many guesses do I get? '))

max_range = 100
min_range = 1
guesses = 0

while attempt_limit > guesses:
    guesses += 1

    x = (max_range + min_range) // 2

    guess_attempt = input('Is the number higher, lower, or the same as ' + str(x) + '? ')

    if guess_attempt == 'lower':
        max_range = x

    if guess_attempt == 'higher':
        min_range = x

    if guess_attempt == 'same':
        print('I won!')
        break

    if max_range - 1 == min_range:
        print('Wait, how can it be higher than ' + str(min_range) + ' and lower than ' + str(max_range) + '?')
        break

if attempt_limit == guesses:
    losing = int(input('I lost; what was the answer? '))
    if min_range < losing < max_range:
        print('Well played!')
    elif losing < min_range:
        print("That can't be; you said it was higher than " + str(min_range) + '!')
    elif losing > max_range:
        print("That can't be; you said it was lower than " + str(max_range) + '!')
