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

        if choice == '0':
            print("До свидания!")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            try:
                num1 = float(input("Введите первое число: "))
                if choice != '6':
                    num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: Введите корректные числа.")
                continue

            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    print("Ошибка: Деление на ноль невозможно.")
                    continue
                result = num1 / num2
            elif choice == '5':
                result = num1 ** num2
            elif choice == '6':
                if num1 < 0:
                    print("Ошибка: Квадратный корень из отрицательного числа невозможен.")
                    continue
                result = math.sqrt(num1)
            elif choice == '7':
                if num1 < 0:
                    print("Ошибка: Факториал отрицательного числа невозможен.")
                    continue
                result = math.factorial(int(num1))
            elif choice == '8':
                result = math.sin(num1)
            elif choice == '9':
                result = math.cos(num1)
            elif choice == '10':
                result = math.tan(num1)

            print(f"Результат: {result}")
        else:
            print("Ошибка: Некорректная операция. Пожалуйста, выберите правильный номер операции.")

if __name__ == "__main__":
    main()