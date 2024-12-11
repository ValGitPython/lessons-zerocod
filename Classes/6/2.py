import math

def square(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Сторона квадрата должна быть числом")
    if side <= 0:
        raise ValueError("Сторона квадрата должна быть положительным числом")
    
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal

def main():
    while True:
        try:
            side = float(input("Введите длину стороны квадрата: "))
            perimeter, area, diagonal = square(side)
            print(f"Периметр: {perimeter:.2f}")
            print(f"Площадь: {area:.2f}")
            print(f"Диагональ: {diagonal:.2f}")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
