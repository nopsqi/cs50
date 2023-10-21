grocery_list = {}

while True:
    try:
        item = input()
    except EOFError:
        grocery_list = {k: v for k, v in sorted(grocery_list.items(), key=lambda item: )}
        for item in grocery_list:
            print(grocery_list[item], item.upper())
        break
    else:
        if grocery_list.get(item) is None:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1