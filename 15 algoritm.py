def raqamlar_yigindisi(massiv):
    yigindi = 0
    etiborsiz_qoldir = False

    for son in massiv:
        if son == 6:
            etiborsiz_qoldir = True
        if not etiborsiz_qoldir:
            yigindi += son
        if son == 7 and etiborsiz_qoldir:
            etiborsiz_qoldir = False

    return yigindi

# Misollar uchun foydalanish:
massiv1 = [1, 2, 2, 6, 99, 99, 7, 3, 4]
massiv2 = [1, 6, 7, 2, 6, 2, 7, 1, 7]
massiv3 = [1, 2, 2, 6, 99, 99, 7, 7]
massiv4 = []

print(raqamlar_yigindisi(massiv1))  # Natija: 10
print(raqamlar_yigindisi(massiv2))  # Natija: 11
print(raqamlar_yigindisi(massiv3))  # Natija: 12
print(raqamlar_yigindisi(massiv4))  # Natija: 0