
def handler(str):
    return input(str + "\n")

def process_calulation():

    a = handler("Введите первое целое число")

    try:
        if "." in a:
            a = float(a)
        else:
            a = int(a)
    except Exception:
        print("Вы ввели не целое число")
        return

    operator = handler("Введите оператор, например: +, -, *, /").strip()

    if operator not in ["+", "-", "*", "/"]:
        print("Введён некорректный оператор")
        return

    b = handler("Введите второе целое число")
    try:
        if "." in b:
            b = float(b)
        else:
            b = int(b)
    except Exception:
        print("Вы ввели не целое число")
        return

    print("Результат вычисления:")
    try:
        if operator == "+":
            print(a + b)
        elif operator == "-":
            print(a - b)
        elif operator == "*":
            print(a * b)
        elif operator == "/":
            if int(b) == 0:
                raise Exception('На ноль делить нельзя!')

            print(a / b)
        else:
            print("Ваш оператор не найден")
    except Exception as error:
        print("Вычисление не удалось. Попробуйте еще раз. Ошибка:", error)

def main():
    while True:
        operation = input(
            "Выберите поведение: начало - режим калькулятора, выход - выйти из программы \n")

        match operation:
            case "начало":
                process_calulation()
            case "выход":
                exit()
            case _:
                print("Такое поведение не корректное")

    return 0

if __name__ == '__main__':
    main()
