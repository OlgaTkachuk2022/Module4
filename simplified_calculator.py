print('-=>Калькулятор<=-')
num1 = int(input('Введіть перше число:')) # В num1 записуємо перше число
num2 = int(input('Введіть друге число:')) # В num2 записуємо друге число
symbol_i = input('Введіть символ:') # В symbol_i записуємо те що ми будемо робити

if symbol_i == '+' or symbol_i == '-' or symbol_i == '/' or symbol_i == '*': # Перевірка на правильний символ
    if symbol_i == '+':
        res = num1 + num2
    if symbol_i == '-':
        res = num1 - num2
    if symbol_i == '/':
        res = num1 / num2
    if symbol_i == '*':
        res = num1 * num2
else:
    print('exit')
print('Result: ', num1, symbol_i, num2, ' = ', res)