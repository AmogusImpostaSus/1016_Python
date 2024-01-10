result = []

def divider(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    if a < b:
        raise ValueError("a should be greater than or equal to b")
    if b > 100:
        raise IndexError("b should be less than or equal to 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError) as e:
        print(f"Exception: {e}")

print(result)
