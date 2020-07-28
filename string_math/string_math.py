
from functools import reduce

###### The Following Modules Belong to add() ######

def add(n1, n2):
    """
    Adds two strings of digits representing numbers
    """
    # ensure n1 is the longest
    if len(n2) > len(n1):
        n1, n2 = n2, n1

    diff = len(n1) - len(n2)
    n1 = list(n1)
    n2 = ["0"] * diff + list(n2)
    # output
    output = ["0"] * (len(n1) + 1)

    carry_over = 0
    for i in range(len(n1)-1, -1, -1):
        s = int(n1[i]) + int(n2[i]) + carry_over
        carry_over = 0
        if s > 9:
            s = str(s)
            carry_over = int(s[0])
            output[i+1] = s[1]
        else:
            output[i+1] = str(s)
    if carry_over != 0:
        output[0] = str(carry_over)

    j = 0
    while output[j] == "0":
        j += 1        
    return "".join(output[j::])

###### The Following Modules Belong to multiply() ######

def format_and_arrange_input(input1, input2):
    if len(input1) > len(input2):
        return list(input1), list(input2)
    else:
        return list(input2), list(input1)

def initialize_products_list(number1_length, number2_length):
    return [ [0] * (number1_length + i) for i in range(number2_length, 0, -1) ]

def get_digit_product(digit1, digit2, carry_over):
    return int(digit1) * int(digit2) + carry_over

def update_products_and_carry_over(digit_product, carry_over, products, idx, j):
    if digit_product > 9:
        number = str(digit_product)
        products[idx][j+1] = int(number[1])
        carry_over = int(number[0])
    else:
        products[idx][j+1] = digit_product
        carry_over = 0
    return products, carry_over

def add_zeros_to_product(products, idx):
    products[idx] = [0] * (len(products[0]) - len(products[idx])) + products[idx]

def handle_remaining_carry_over(carry_over, products, idx):
    if carry_over != 0:
            products[idx][0] = carry_over

def convert_products_to_strings(products):
    products = [ ["".join(list(map(str, p)))] for p in products]

def multiply(input1, input2):

    number1, number2 = format_and_arrange_input(input1, input2)
    products = initialize_products_list(len(number1), len(number2))

    idx = len(products) - 1

    for i in range(len(number2)-1,-1,-1):
        carry_over = 0
        for j in range(len(number1)-1,-1,-1):
            digit_product = get_digit_product(number2[i], number1[j], carry_over)
            products, carry_over = update_products_and_carry_over(digit_product, carry_over, products, idx, j)

        handle_remaining_carry_over(carry_over, products, idx)
        add_zeros_to_product(products, idx)
        idx -= 1

    convert_products_to_strings(products)
    return reduce( (lambda a,b: add(a,b)), products)
