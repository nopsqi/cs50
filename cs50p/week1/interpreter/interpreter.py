x, y, z = input("Expression: ").strip().split(" ")
x, z = float(x), float(z)

match y:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x - y)
    case "/":
        print(x / y)