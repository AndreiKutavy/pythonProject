# Home work 2.1
print("Programming", "Essentials", "in...Python", sep="***")
print("Programming", "Essentials", "in", sep="***", end="...Python\n")
# or
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# Home work 2.2
print()
print("     ", end="*\n")
print("    ", " ", sep="*", end="*\n")
print("   ", "   ", sep="*", end="*\n")
print("  ", "     ", sep="*", end="*\n")
print("***", "***", sep="     ", end="\n")
print("   ", "   ", sep="*", end="*\n")
print("   ", "   ", sep="*", end="*\n")
print("   ", end="*****")
# or
print()
print()
print(" " * 5, end="*\n")
print(" " * 4, " ", sep="*", end="*\n")
print(" " * 3, " " * 3, sep="*", end="*\n")
print(" " * 2, " " * 5, sep="*", end="*\n{}".format("*" * 3))
print("", "*" * 3, sep=" " * 5, end="\n")
print(" " * 3, " " * 3, sep="*", end="*\n")  # duplicate X2 ?????
print(" " * 3, " " * 3, sep="*", end="*\n")
print(" " * 3, end="*" * 5)

# Home work 2.3
print()
print("""\n"I'm"\n""learning""\n\"""Python\""\"""")
# or
print("""
"I'm"
""learning""
\"""Python\"""
""")

# Home work 2.4
john, mary, adam = 2, 3, 4
print(mary, john, adam, sep=', ')
total_apples = john + mary + adam
print("Всего яблок:", total_apples)
print()

john, mary, adam = "John", "Mary", "Adam"
print(john, mary, adam)
john, mary, adam = 2, 3, 4
total_apples = john + mary + adam
print("Количество яблок у Иоанна:", john)
print("Количество яблок у Марии:", mary)
print("Количество яблок у Адама:", adam)
print("общее количество яблок у ребят:", total_apples)

# # Home work 2.5
# print("""
# Что вы хотите конвертировать?
#     1. Километры в мили
#     2. Мили в километры
#     3. Выход из программы
# (пожалуйста сделайте выбор "1", "2" или "3")
# """)
# chose = input()
# if chose == 1:
#     kilom = float(input("Пожалуйста укажите количество километров: "))
#     total1 = kilom * 1.61
#     print("Итог:", total1)
# elif chose == 2:
#     miles = float(input("Пожалуйста укажите количество миль: "))
#     total2 = miles / 1.61
#     print("Итог:", total2)
# elif chose == 3:
#     exit(0)

# Home work 2.6
print()
x, x1, x2 = 0, 1, -1
y = ((3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1)
y1 = ((3 * x1 ** 3) - (2 * x1 ** 2) + (3 * x1) - 1)
y2 = ((3 * x2 ** 3) - (2 * x2 ** 2) + (3 * x2) - 1)
print(y, y1, y2, sep=", ", end=".\n")

# Home work 2.7
print()
print()
houre = float(input("Введите количество часов для перевода в секунды: "))
sec = houre * 3600
print("Вы ввели:", houre, " что составляет:", sec, "секунд")

# Home work 2.8
print("---Сумма чисел---")
x = float(input("Введите 1-ое число: "))
y = float(input("Введите 2-ое число: "))
print(x + y)

print("---Разность чисел---")
x = float(input("Введите 1-ое число: "))
y = float(input("Введите 2-ое число: "))
print(x - y)

print("---Разделить чисела---")
x = float(input("Введите 1-ое число: "))
y = float(input("Введите 2-ое число: "))
print(x / y)

print("---Умножение чисел---")
x = float(input("Введите 1-ое число: "))
y = float(input("Введите 2-ое число: "))
print(x * y)

print("---Возведение чисел в степень---")
x = float(input("Введите число: "))
y = float(input("Введите степень: "))
print(x ** y)

print("---Целочисленное деление чисел---")
x = float(input("Введите 1-ое число: "))
y = float(input("Введите 2-ое число: "))
print(x // y)

print("---Остаток от деления от числа---")
x = float(input("Введите 1-ое число: "))
y = float(input("Введите 2-ое число: "))
print(x % y)

# Home work 2.9
print("""
__________________
|       1        |
|   ----------   |
|          1     |
|   x + ------   |
|          1     |
|   x + ------   |
|          1     |
|    x + -----   |
|          x     |
__________________
""")
x = float(input("Введите число Х: "))
total = float(1 / (x + (1 / (x + (1 / (x + (1 / x)))))))
print(total)
print()

# Home work 2.10
print("Hello Word!")
print()

# Home work 2.11
a = int(11111)
b = int(1111111)
print(a * b)
print()

# # Home work 2.12
# a = 42 / (4 + 2 * (-2))
# print(a)

# Home work 2.13
print(2014 ** 14)

# Home work 2.14
print()
month = float(input("Введите количество месяцев для перевода в секунды: "))
sec = 30 * 24 * 3600
print("Вы ввели:", month, " что составляет:", sec, "секунд")

# Home work 2.15
print()
print(2014.0 ** 14)

# Questions
# Home work 2.3
# print(""""I'm"\n""learning""\n""Python""")

# Test
# # Здесь будет выведено: 3
# a = 1
# b = 2
# c = a + b
# print("Здесь будет выведено:", c)
#
# # Здесь будет выведено 'С': 3
# a = 1
# b = 2
# c = a + b
# print("Здесь будет выведено 'С': {}".format(c))
#
# # Здесь будет выведено: 1 + 2 = 3
# a = 1
# b = 2
# c = a + b
# print("Здесь будет выведено: {a} + {b} = {c}".format(c=c, a=a, b=b))
#
# # Здесь будет выведено: 1 + 2 = 3
# a = 1
# b = 2
# c = a + b
# print(f"Здесь будет выведено: {a} + {b} = {c}")
