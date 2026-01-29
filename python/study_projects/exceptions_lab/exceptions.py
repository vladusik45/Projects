import time
# 1. Минимум 2 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключение при определённых значениях входных параметров.
# Функции НЕ ДОЛЖНЫ содержать никаких обработчиков исключений.
def zero_division(number):
    zero = 0
    return number / zero

def index_out_of_range():
    lst = [1, 2, 3]
    return lst[3]

# 2. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик НЕ ДОЛЖЕН содержать блок finally.

def process_numbers(strng):
    try:
        return int(strng)
    except Exception as e:
        print(f"Исключение: {e}")


# 3. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик ДОЛЖЕН содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception as e:
        # Логика обработки исключения
        print(f"Исключение: {e}")
        result = None 
    finally:
        if result is None:
            result = 0  
        print("Операция завершена.")
        return result

# 4. Минимум 3 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключения при определённых значениях входных параметров.
# Функции ДОЛЖНЫ содержать НЕСКОЛЬКО обработчиков РАЗНЫХ типов исключений (минимум 3 типа исключений). Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Каждый обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def safe_divide(a, b):
    try:
        if isinstance(a, (int, float)) and a < 0:
            _ = 1 / (a + 1) 
        result = a / b
    except ZeroDivisionError as e:
        print(f"Исключени: {e} — деление на ноль невозможно.")
        result = None
    except TypeError as e:
        print(f"Исключение: {e} — входные параметры должны быть числами.")
        result = None
    except Exception as e:
        print(f"Исключение: {e} — возможно, делимое не соответствует условиям.")
        result = None
    finally:
        if result is None:
            result = 0  
        print("Операция завершена.")
        return result

def access_list_element(lst, index):
    try:
        if isinstance(index, int) and index < 0:
            _ = [][index] 
        return lst[index]
    except IndexError as e:
        print(f"Исключение: {e} — индекс за пределами списка.")
        return None
    except TypeError as e:
        print(f"Исключение: {e} — некорректный тип данных.")
        return None
    except Exception as e:
        print(f"Исключение: {e} — индекс не соответствует условиям.")
        return None
    finally:
        print("Попытка доступа к элементу списка завершена.")


def validate_string(s, min_length, must_contain):
    try:
        if not isinstance(s, str):
            _ = len(123) 
        if len(s) < min_length:
            _ = s[100]  
        if must_contain not in s:
            _ = {}[must_contain]  
        return True
    except TypeError as e:
        print(f"Исключение: {e}")
        return False
    except IndexError as e:  
        print(f"Исключение: {e} — строка слишком короткая.")
        return False
    except KeyError as e:
        print(f"Исключение: {e} — обязательный символ отсутствует.")
        return False
    finally:
        print("Проверка строки завершена.")

# 5. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА генерировать исключения при определённых условиях (в Python есть конструкция для генерации исключений).
# Функция ДОЛЖНА содержать обрабоnчики всех исключений, которые генерируются внутри этой функции. Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.

def process_number(a, b):
    try:
        a_converted = float(a) if isinstance(a, (int, float)) else int(a)
        
        result = a_converted / b
    except ZeroDivisionError as e:
        print(f"Ошибка: {e} — деление на ноль невозможно.")
        result = None
    except TypeError as e:
        print(f"Ошибка: {e} — оба параметра должны быть числами.")
        result = None
    except ValueError as e:
        print(f"Ошибка: {e} — число `a` не может быть отрицательным или некорректным.")
        result = None
    finally:
        if result is None:
            result = 0  
        print("Обработка завершена.")
        return result


# 6. Минимум 3 разных пользовательских исключения и примеры их использования
# Определение пользовательского исключения
class InvalidAgeError(Exception):
    def __init__(self, age, message="Возраст недопустим. Он должен быть от 0 до 120."):
        self.age = age
        self.message = message
        super().__init__(self.message)
def validate_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    print(f"Возраст {age} принят.")
def test_validate_age():
    try:
        validate_age(150)  
    except InvalidAgeError as e:
        print(f"Исключение: {e}")

class NegativeBalanceError(Exception):
    def __init__(self, balance, message="Баланс не может быть отрицательным."):
        self.balance = balance
        self.message = f"{message} Текущий баланс: {self.balance}"
        super().__init__(self.message)
def withdraw(balance, amount):
    new_balance = balance - amount
    if new_balance < 0:
        raise NegativeBalanceError(new_balance)
    print(f"Снятие успешно. Новый баланс: {new_balance}")
    return new_balance
def test_withdraw():
    try:
        withdraw(100, 200)  
    except NegativeBalanceError as e:
        print(f"Исключение: {e}")

class InvalidOperationError(Exception):
    def __init__(self, operation, message="Операция недопустима."):
        self.operation = operation
        self.message = f"{message} Операция: {self.operation}"
        super().__init__(self.message)
def perform_operation(operation):
    allowed_operations = ["add", "subtract", "multiply", "divide"]
    if operation not in allowed_operations:
        raise InvalidOperationError(operation)
    print(f"Операция '{operation}' выполнена успешно.")
def test_perform_operation():
    try:
        perform_operation("modulus") 
    except InvalidOperationError as e:
        print(f"Исключение: {e}")


# 7. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать пользовательское исключение, созданное на шаге 6. при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать МИНИМУМ ОДИН обработчик исключений. Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик МОЖЕТ содержать блок finally.
# Функция с обработкой исключения
def register_user(name, age):
    try:
        if not (0 <= age <= 120):
            raise InvalidAgeError(age)  
        print(f"Пользователь {name} успешно зарегистрирован с возрастом {age}.")
    except InvalidAgeError as e:
        print(f"Ошибка регистрации: {e}. Пожалуйста, проверьте возраст.")
    finally:
        print("Регистрация завершена (успешно или с ошибкой).")

# 8. Минимум 3 функции, демонстрирующие работу исключений.
# Алгоритм функций необходимо придумать самостоятельно
def check_empty_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise ValueError("Файл пуст.")  
            print(f"Файл содержат данные: {content}")
    except FileNotFoundError:
        print(f"Исключение: Файл по пути {file_path} не найден.")
    except ValueError as e:
        print(f"Исключениe: {e}")
    except Exception as e:
        print(f"Неизвестное исключение: {e}")
    finally:
        print("Проверка файла завершена.")

def check_number_in_range(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError("Ошибка: Введённое значение должно быть числом.")
        if num < 0 or num > 100:
            raise ValueError("Число должно быть в пределах от 0 до 100.")
        print(f"Число {num} в пределах допустимого диапазона.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Проверка диапазона завершена.")

def connect_to_database(connection_string):
    try:
        if not connection_string:
            raise ConnectionError("Ошибка: Строка подключения пуста.")
        
        time.sleep(2)  
        if connection_string == "wrong_connection":
            raise TimeoutError("Ошибка: Время ожидания подключения истекло.")
        
        print("Подключение к базе данных успешно.")
    except ConnectionError as e:
        print(f"Ошибка подключения: {e}")
    except TimeoutError as e:
        print(f"Ошибка подключения: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Попытка подключения завершена.")
