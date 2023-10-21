text = input("Input: ")
print("Output:", end=" ")

for t in text:
    if t.lower() in ['a', 'i', 'u', 'e', 'o']:
        continue
    print(t, end="")
print()