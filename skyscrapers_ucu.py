'''https://github.com/be-unkind/skyscrapers_ucu'''
def read_input(path: str) -> list:
    '''
    Read game board file from path.
    Return list of str.
    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    '''
    result = []
    with open(path, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            result.append(line)
    return result

# print(read_input("check.txt"))

def left_to_right_check(input_line: str, pivot: int) -> bool:
    '''
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.
    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.
    >>> left_to_right_check("412453*", 4)
    True
    '''
    count = 0
    temporary_lst = []
    input_lst = list(input_line)
    if '*' in input_lst:
        input_lst.remove('*')
    for element in input_lst:
        if int(element) == pivot:
            idx_of_element = input_lst.index(element)
            for element1 in input_lst[idx_of_element:]:
                if len(temporary_lst) == 0:
                    temporary_lst.append(int(element1))
                else:
                    if int(element1) > temporary_lst[0]:
                        count+=1
                        del temporary_lst[0]
    if count == pivot:
        return True
    else:
        return False

# print(left_to_right_check("452453*", 5))

def check_not_finished_board(board: list) -> bool:
    '''
    Check if skyscraper board is not finished, i.e., '?' present on the game board.
    Return True if finished, False otherwise.
    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    '''
    check_lst = []
    for element in board:
        if '?' in element:
            check_lst.append('False')
        else:
            check_lst.append('True')
    if 'False' in check_lst:
        return False
    else:
        return True

# print(check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_uniqueness_in_rows(board: list) -> bool:
    '''
    Check buildings of unique height in each row.
    Return True if buildings in a row have unique length, False otherwise.
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    '''
    temporary_lst = []
    for element in board:
        element_lst = list(element)
        del element_lst[0]
        del element_lst[len(element_lst)-1]
        for count in range(len(element_lst) + 1):
            if '*' in element_lst:
                element_lst.remove('*')
        if len(element_lst) != len(set(element_lst)):
            temporary_lst.append('False')
        else:
            temporary_lst.append('True')
    if 'False' in temporary_lst:
        return False
    else:
        return True

# print(check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_horizontal_visibility(board: list):
    '''
    Check row-wise visibility (left-right and vice versa)
    Return True if all horizontal hints are satisfiable,
    i.e., for line 412453* , hint is 4, and 1245 are the four buildings
    that could be observed from the hint looking to the right.
    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    '''
    res_lst = []
    for element in board:
        element_lst = list(element)
        if (element_lst[0] == '*') and (element_lst[-1] == '*'):
            continue
        if element_lst[-1] == '*':
            if left_to_right_check(element, element_lst[0]) == True:
                res_lst.append('True')
            else:
                res_lst.append('False')
        if element_lst[0] == '*':
            element_lst.reverse()
            if left_to_right_check(element, element_lst[0]) == True:
                res_lst.append('True')
            else:
                res_lst.append('False')
    if 'False' in res_lst:
        return False
    else:
        return True

# print(check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_columns(board: list):
    '''
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice ve
    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    '''
    pass

def check_skyscrapers(input_path: str):
    '''
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    >>> check_skyscrapers("check.txt")
    True
    '''
    pass

# if __name__ == "__main__":
#     print(check_skyscrapers("check.txt"))

print(left_to_right_check("132345*", 3))
