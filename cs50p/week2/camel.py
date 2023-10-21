camel_case = input("camelCase: ").strip()
print("snake_case:", end=" ")
for s in camel_case:
    if s.isupper():
        print(f"_{s.lower()}", end="")
        continue
    print(s, end="")
print()