
def check(card_number):
    divide = str(card_number)[::-1]
    first_series = divide[::2]
    first_sum = 0
    for i in first_series:
        first_sum += int(i)

    second_series = str(card_number)[-2::-2]
    second_series_2 = ''
    second_sum = 0
    for s in second_series:
        second_series_2 += str(2*int(s))
    for w in second_series_2:
        second_sum += int(w)

    total = first_sum + second_sum
    #return total % 10 == 0
    if total % 10 == 0:
        return True
    else:
        return False
