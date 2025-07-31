def ekstra(fonk):
    def ekstra_ozellik():
        print("Mükemmel sayılar: ")
        for sayi in range(1, 1001):
            toplam = 0
            i = 1
            while i < sayi:
                if sayi % i == 0:
                    toplam += i
                i += 1
            if toplam == sayi:
                print(sayi)
        fonk()
    return ekstra_ozellik


@ekstra
def asal_sayilar():
    print("Asal sayılar: ")
    for sayi in range(2, 1001):
        i = 2
        counter = 0
        while i < sayi:
            if sayi % i == 0:
                counter += 1
            i += 1
        if counter == 0:
            print(sayi)


asal_sayilar()
