
liste = ["345", "sadas", "324a", "14", "kemal"]

for i in liste:
    try:
        int(i)
        print(i, "bir sayıdır.")
    except ValueError:
        print(f"{i} bir sayı değildir.")
