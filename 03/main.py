import pathlib
from collections import defaultdict 


fn = pathlib.Path(__file__).parent / 'input.txt'


gears = defaultdict(list)

def is_symbol_in_list(input: list):
    for char in input:
        if not char.isdigit() and char != '.':
            return True
    return False

def append_to_gears_horizontal(i, start_j, input: list, number: int):
    for k, char in enumerate(input):
        if char == '*':
            gears[(i, start_j + k)].append(number)

def append_to_gears_vertical(j, start_i, input: list, number: int):
    for k, char in enumerate(input):
        if char == '*':
            gears[(start_i + k, j)].append(number)

def is_adjecent(input_array: list, number_builder: str, i: int, j: int):
    """
    i -> row 0 indexed of a string
    j -> column 0 indexed of a last digit of a number
    """
    length = len(number_builder)
    SIZE_ROW = len(input_array[0])
    SIZE_COL = len(input_array)
    # Indexes of the edges
    left = max(j - length, 0)
    right = min(j + 1, SIZE_ROW - 1)
    top = max(i - 1, 0)
    bottom = min(i + 1, SIZE_COL - 1)

    print(f"""
number_builder: {number_builder}          
left: {left}
right: {right}
top: {top}
bottom: {bottom}
          """)
    # Top layer check
    for row_index in [row_index for row_index in [top, bottom] if row_index != i]:
        list_to_check = input_array[row_index][left:right+1]
        if is_symbol_in_list(list_to_check):
            append_to_gears_horizontal(row_index, left, list_to_check, int(number_builder))
            return True
    if left != j - length + 1:
        list_to_check = [row[left] for row in input_array[top:bottom+1]]
        if is_symbol_in_list(list_to_check):
            append_to_gears_vertical(left, top, list_to_check, int(number_builder))

            return True
    if right != j:
        list_to_check = [row[right] for row in input_array[top:bottom+1]]
        if is_symbol_in_list(list_to_check):
            append_to_gears_vertical(right, top, list_to_check, int(number_builder))
            return True
    return False

def calculate_gears():
    total = 0
    for values in gears.values():
        if len(values) == 2:
            total = total + (values[0] * values[1])
    return total

if __name__ == "__main__":
    input_array = []
    

    # Get all chars into 2dim array
    result = 0
    with open(fn) as f:
        lines = f.readlines()
        for row in lines:
            row_arr = []
            for char in row:
                if char != '\n':
                    row_arr.append(char)
            input_array.append(row_arr)
    # Process rows
    for i, row in enumerate(input_array):
        number_builder = None
        for j, char in enumerate(row):
            if not char.isdigit():
                if not number_builder:
                    continue
                
                if is_adjecent(input_array, number_builder, i, j-1):
                    result += int(number_builder)
                number_builder = None
            elif not number_builder:
                number_builder = char
            else:
                number_builder += char
        if number_builder:
            if is_adjecent(input_array, number_builder, i, len(input_array[i])-1):
                result += int(number_builder)
                number_builder = None
    print(f'Result: {result}')
    total_gears = calculate_gears()
    print(f'gear ratio: {total_gears}')

        
