# Рекурсивное умножение
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if number == 0:
        return 0

    if len(str_number) > 1:
        a = get_multiplied_digits(int(str_number[1:]))
        if a != 0:
            return first * a
        else:
            return first
    else:
        return first


# Примеры использования функции
result = get_multiplied_digits(40203)
print(result)  # 24

result2 = get_multiplied_digits(402030)
print(result2)  # 24

result3 = get_multiplied_digits(0)
print(result3)  # 0

result4 = get_multiplied_digits(00000)
print(result4)  # 0
