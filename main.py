# 1-m
h = input("Hujjat topshirdingizmi? ")
s = input("Suhbatdan o'tingizmi? ")
t = input("Testdan o'tingizmi? ")

if h == "Ha" and s == "Ha" and t == "Ha":
    print("Siz ishga qabul qilindingiz!")

elif h == "Yoq" and s == "Ha" and t == "Ha":
    print("Avvalo hujjatlaringizni topshiring.")

elif h == "Ha" and s == "Yoq" and t == "Ha":
    print("Suhbatdan o‘tmagansiz.")

elif h == "Ha" and s == "Ha" and t == "Yoq":
    print("Test natijalari yetarli emas.")

else:
    print("Jarayon davom etmoqda.")


# 2-m
i = input("Jumla kirit: ")

text = ""
for a in i.split():
    text += a[0]

print(text)


# 3-m
royxat = [4, 7, 2, 5, 1, 10]
print(royxat)

yangi = []

for i in range(len(royxat)):
    yangi.append(i * royxat[i])

print(yangi)


# 4-m
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

b = ""
i = ""

for w in words:
    if len(w) > len(b):
        i = b
        b = w
    elif len(w) > len(i):
        i = w

print("1-chi:", b)
print("2-chi:", i)



# 5-m
matn = input("So‘z kiriting: ")

for i, harf in enumerate(matn, 1):
    print(i, "-", harf)
