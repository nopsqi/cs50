from emoji import emojize

text = input("Input: ").split(":")
print(text)

for i, t in enumerate(text):
    if i % 2 == 1:
        print(emojize(f":{t}:"), end="")
    else:
        print(t, end="")
print()