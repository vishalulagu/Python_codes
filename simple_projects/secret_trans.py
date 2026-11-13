
key_letter = " abcdefghijklmnopqrstuvwxyz"
encript_value_letter = "3z6xwv2t5r1p4nmlkjihgfedcba"
decript_value_letter = " abcdefghijklmnopqrstuvwxyz"
#print(value_letter)

while True:
    mode = input("\t1 -> for Encript\n\t2 -> for Decript\nChoose one from above: ")
    if mode == "stop":
        break
    if not mode.strip():
        continue

    if mode.lower() in ["1", "encript", "encription"]:
        while True:
            text = input("Type your Normal message: ")
            if text == "stop":
                break
            if not text.strip():
                continue
            table = str.maketrans(key_letter, encript_value_letter)
            print(text.lower().translate(table))

    if mode.lower() in ["2", "decript", "decription"]:
        while True:
            text = input("Type your Encripted message: ")
            if text == "stop":
                break
            if not text.strip():
                continue
            table = str.maketrans(encript_value_letter, decript_value_letter)
            print(text.lower().translate(table))

    else:
        print("Type only '1' or '2' and click 'Enter'")
        continue