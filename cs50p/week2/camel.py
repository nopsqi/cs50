for s in input("camelCase: ").strip():
    if s.isupper():
        print(f"_{s.lower()}")
        continue
    print(s)