'''
this method receives an string
and formats it if its a valid board.

filter method is for removing whitespaces in array
'''
def parse_string_to_game_format(string):
    result_string = ''
    string_arr = string.split(' ')
    print(string_arr, len(string_arr))
    string_arr = list(filter(None, string_arr))
    if (len(string_arr)!= 9):
        result_string = 'not a computable board'
        return result_string
    for i, l, in enumerate(string_arr):
        if l == 'e':
            l = ' '
        result_string += str(l)
        if(i+1) %3 != 0:
            result_string += ' |'
        if (i+1) %3 == 0:
            result_string += '\n'

    return result_string


def main():
    print(parse_string_to_game_format('e e e x o x o o o      '))



if __name__ == "__main__":
    # execute only if run as a script
    main()
