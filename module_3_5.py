# Рекурсивное умножение

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if first == 0:
        for digit in str_number[1:]:
            if digit != 0:
                return get_multiplied_digits(int(digit + str_number[str_number.index(digit) + 1:]))
        return 0
    if len(str_number) > 1:
        return first*get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)


# ИЛИ МОЖНО ПРОСТО УБРАТЬ НОЛЬ:
# def get_multiplied_digits(number):
#     str_number = str(number)
#     str_number = str_number.replace('0', '') # удалили все '0' из строки
#     # print(str_number)
#
#     first = int(str_number[0])
#
#     if len(str_number) > 1:
#         return first*get_multiplied_digits(int(str_number[1:]))
#     else:
#         return first
#
#
# result = get_multiplied_digits(402030)
# print(result)
