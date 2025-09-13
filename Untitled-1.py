def factorial(n):
   
    if not isinstance(n, int):
        raise TypeError("Факториал определен только для целых чисел")
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
from my_math import factorial

def main():
    try:
        n = int(input().strip())
        result = factorial(n)
        print(result)
    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()