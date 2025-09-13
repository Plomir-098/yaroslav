from math import factorial

def main():
    try:
        n = int(input().strip())
        if n < 0:
            print("Ошибка: факториал определен только для неотрицательных чисел")
        else:
            result = factorial(n)
            print(result)
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()