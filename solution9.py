x = input("Type your value: ")

if x == "0":
    x = bool(False)
elif x == "1":
    x = bool(True)
else:
    x = "hi!"

print("Your entered value is now", x)