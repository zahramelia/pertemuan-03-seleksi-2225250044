# Program menentukan jenis segitiga

a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b:
        if b == c:
            print("Segitiga sama sisi.")
        else:
            print("Segitiga sama kaki.")
    else:
        if a == c or b == c:
            print("Segitiga sama kaki.")
        else:
            print("Segitiga sembarang.")
else:
    print("Bukan segitiga.")