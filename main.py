import math


def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("0. Выход")

        choice = input("Введите номер операции: ")

        if choice in ('1', '2', '3', '4', '5'):
            while True:
                try:
                    num1 = int(input("Введите первое число: "))
                    num2 = int(input("Введите второе число: "))
                    break
                except ValueError:
                    print("Invalid")

        elif choice in ('6', '7', '8', '9', '10'):
            while True:
                try:
                    num1 = int(input("Введите число: "))
                    break
                except ValueError:
                    print("Invalid")

        if choice == '0':
            print("До свидания!")
            break

        elif choice == '1':
            result = num1 + num2
            print("Результат: ", result)

        elif choice == '2':
            result = num1 - num2
            print("Результат: ", result)

        elif choice == '3':
            result = num1 * num2
            print("Результат: ", result)

        elif choice == '4':
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно.")
                continue
            result = num1 / num2
            print("Результат: ", result)

        elif choice == '5':
            result = num1 ** num2
            print("Результат: ", result)

        elif choice == '6':
            if num1 < 0:
                print("Ошибка: Квадратный корень из отрицательного числа невозможен.")
                continue
            result = math.sqrt(num1)
            print("Результат: ", result)
        elif choice == '7':
            result = math.factorial(num1)
            print("Результат: ", result)

        elif choice == '8':
            result = math.sin(num1)
            print("Результат: ", result)

        elif choice == '9':
            result = math.cos(num1)
            print("Результат: ", result)

        elif choice == '10':
            result = math.tan(num1)
            print("Результат: ", result)
        else:
            print("Ошибка пиши правильно")


main()
