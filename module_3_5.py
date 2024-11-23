# Рекурсивное умножение

def get_multiplied_digits(number):
    if number == 0: # это если о
        return 0
    str_number = str(number)
    if all(digit == '0' for digit in str_number): # если все нули
        return 0
    str_number = str_number.replace('0', '')  # удалили все '0' из строки
    first = int(str_number[0])
    if len(str_number) > 1:
        return first*get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result1 = get_multiplied_digits(402030)
result2 = get_multiplied_digits(00000)
result3 = get_multiplied_digits(0)
print(result1)
print(result2)
print(result3)
