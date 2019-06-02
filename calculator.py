

def binop(input_string):
    if input_string.find("+") != -1:
        position = input_string.find("+")
        return int(input_string[0:position]) + int(input_string[position + 1:len(input_string)])

    if input_string.find("-") != -1:
        position = input_string.find("-")
        return int(input_string[0:position]) - int(input_string[position + 1:len(input_string)])

    if input_string.find("*") != -1:
        position = input_string.find("*")
        return int(input_string[0:position]) * int(input_string[position + 1:len(input_string)])

    if input_string.find("/") != -1:
        position = input_string.find("/")
        return int(input_string[0:position]) / int(input_string[position + 1:len(input_string)])

