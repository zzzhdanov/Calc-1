class Convert:
    def __init__(self):
        pass

    def get_code(a):
        if a.isdigit():
            return int(a)
        else:
            return int(ord(a) - ord('A') + 10)

    def convert_n_to_10(a, b):
        int(b)
        pow = 1
        result = 0
        for i in a[::-1]:
            result += Convert.get_code(i) * pow
            pow *= b
        return result

    def recover_code(e):
        if int(e) <= 9:
            return str(e)
        else:
            return chr(int(e) - 10 + ord('A'))

    def convert_10_to_n(a, b):
        int(a)
        int(b)
        ans = ""
        while (a > 0):
            ans = Convert.recover_code(str(a % b)) + ans
            a //= b
        return ans


###############################################################

digit1 = input()  # число1
convert_from1 = int(input())  # указание системы счисления числа 1
operation = input()  # операция
digit2 = input()  # число2
convert_from2 = int(input())  # указание системы счисления числа 2
convert_result = int(input())  # итоговая система счисления результата

################################################################
first = str(Convert.convert_n_to_10(digit1, convert_from1)) + operation + str(Convert.convert_n_to_10(digit2, convert_from2))
last = Convert.convert_10_to_n(eval(first), convert_result)

print(last)  # РЕЗУЛЬТАТ <----------------------------------------
