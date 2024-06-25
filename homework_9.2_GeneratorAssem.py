# Задача 1: Фабрика функций
def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            if y == 0:
                return "Error: Division by zero"
            return x / y
        return divide
    else:
        return None

# Примеры использования фабрики функций
multiply_func = create_operation("multiply")
print('Задача 1: Фабрика функций')
print(multiply_func(3, 2))

divide_func = create_operation("divide")
print(divide_func(6, 3))
print(divide_func(6, 0))

# Задача 2: Лямбда-Функции

# Лямбда-функция для возведения числа в квадрат
square_lambda = lambda x: x * x
print("Задача 2: Лямбда")
print(square_lambda(4))
# Эквивалентная функция, определённая с использованием def
def square_def(x):
    return x * x

print(square_def(4))

# Задача 3: Вызываемые Объекты

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b
print('Задача 3: Вызываемые Объекты')
# Пример использования вызываемого объекта
rectangle = Rect(2, 4)
print(f"Стороны: {rectangle.a}, {rectangle.b}")
print(f"Площадь: {rectangle()}")