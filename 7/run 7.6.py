def divide(x, y):
    result = None
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Division by zero")
    finally:
        print("Cleaning up...")
        del result

print(divide(3, 1))
divide(3, 0)