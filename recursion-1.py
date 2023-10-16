def reverse_string(string):
    if len(string) <= 1:
        print(string)
    else:
        print(string[-1], end='')
        reverse_string(string[:-1])

input_string = "qwerry"
reverse_string(input_string)