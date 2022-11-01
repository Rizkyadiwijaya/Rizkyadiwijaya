nilai_1 = float(input("masukkan nilai 1 = "))
nilai_2 = float(input("masukkan nilai 2 = "))
operator = input("masukkan operator (+,-,x,/): ")

if operator == "+":
    hasil = (nilai_1 + nilai_2)
    print(hasil)
elif operator == "-":
    hasil = (nilai_1 - nilai_2)
    print(hasil)
elif operator == "x" or operator == "*":
    hasil = (nilai_1 * nilai_2)
    print(hasil)
elif operator == "/":
    hasil = (nilai_1 / nilai_2)
    print(hasil)
else:
    print("gk ngerti puyeng")