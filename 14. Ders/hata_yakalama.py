# try, except, finally

# try:
#   pass
#   # bizim kod bloğumuz
# except:
#   print("Kodlarınızda hata oluştu.")


# scope 1
# hata yakalama - exception handling
# try:
#     # scope 2
#     a = int("123akjsjdfjdsjkjfd")
# except:
#     print("Hata oluştu.")


# print("Bloklar sona erdi.")
# print("Bloklar sona erdi.")
# print("Bloklar sona erdi.")
# print("Bloklar sona erdi.")

# a = int("slökdmjfldkfdkfjg")

# print(2/0)

# try:
#     # a = int("123 sldkfjskdfjg")
#     print(2/0)
#     print("Program burada")
# except ValueError:
#     print("Value error hatasını yakaladık")
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası oldu.")
# finally:
#     print("Her durumda çalışıyorum")

# print("Bloklar sona erdi.")

def ters_cevir(yazi):
    if type(yazi) != str:
        raise ValueError("Lütfen string bir input gönderin.")
    else:
        return yazi[::-1]


# handle etmek - kontrol altına almak
try:
    print(ters_cevir(888888))
except (ZeroDivisionError, ValueError) as e:
    print(e)
except TypeError:
    print("Type error...")
except:
    print("genel except bloğu")
