import math

#CONVERTING DECIMAL TO BINARY
def decimal_to_binary(decimal: int):
    result: str = ''
    print('')
    print(f'Decimal: {decimal}')
    while(decimal != 0):
        bit = str(decimal % 2)
        result = result + bit
        temp = math.floor(decimal/2)
        print(f'{decimal} / 2 = {temp} ; remainder: {bit}')
        decimal = temp
    result = result[::-1]
    print(f'Binary: {result} \n ')
    
# CONVERTING DECIMAL TO HEXIDECIMAL
def decimal_to_hexidecimal(decimal: int):
    result: str = ''
    print('')
    print(f'Decimal: {decimal}')
    while(decimal != 0):
        remainder = str(decimal % 16)
        match remainder:
            case "10": remainder = "A"
            case "11": remainder = "B"
            case "12": remainder = "C"
            case "13": remainder = "D"
            case "14": remainder = "E"
            case "15": remainder = "F"

        result = result + remainder
        temp = math.floor(decimal/16)
        print(f'{decimal} / 16 = {temp} ; remainder: {remainder}')
        decimal = temp
    result = result[::-1]
    print(f'Result: {result}')
    print('')

# CONVERTING DECIMAL TO OCTAL
def decimal_to_octal(decimal: int):
    result = ''
    print('')
    print(f'Decimal: {decimal}')
    while(decimal != 0):
        remainder = str(decimal % 8)
        result = result + remainder
        temp = math.floor(decimal/8)
        print(f'{decimal} / 8 = {temp} ; remainder: {remainder}')
        decimal = temp
    result = result[::-1]
    print(f'Binary: {result}')
    print('')
    
dec = 996956799856978956
#decimal_to_binary(dec)
decimal_to_hexidecimal(dec)
#decimal_to_octal(dec)
