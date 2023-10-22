from emoji import emojize

text = input("Input: ").split(":")

for i, t in enumerate(text):
    if i % 2 == 1:
        print(emojize(f":{t}:", language="alias"), end="")
    else:
        print(t, end="")
print()