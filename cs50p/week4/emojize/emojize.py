from emoji import emojize

text = input("Input: ").split(":")

for i, t in enumerate(text):
    if i % 2 == 0:
        print(emojize(f":{t}:"), end="")
    else:
        print(t, end="")