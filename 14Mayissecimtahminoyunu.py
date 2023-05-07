import random

parties = {
    "Ak parti": 0,
    "Mhp": 0,
    "Chp": 0,
    "İyi Parti": 0
}

cumhur_ittifaki = ["Ak parti", "Mhp"]
millet_ittifaki = ["Chp", "İyi Parti"]

for i in range(4):
    if i == 0:
        vote = int(input("Lütfen oy vermek istediğiniz partiyi seçiniz (1-4): "))
    else:
        vote = random.randint(1, 4)
    
    if vote == 1:
        parties["Ak parti"] += 1
    elif vote == 2:
        parties["Mhp"] += 1
    elif vote == 3:
        parties["Chp"] += 1
    else:
        parties["İyi Parti"] += 1

print("Ak parti: % {:.2f}".format((parties["Ak parti"] / 4) * 100))
print("Mhp: % {:.2f}".format((parties["Mhp"] / 4) * 100))
print("Chp: % {:.2f}".format((parties["Chp"] / 4) * 100))
print("İyi Parti: % {:.2f}".format((parties["İyi Parti"] / 4) * 100))

cumhur_ittifaki_toplam_oy = parties["Ak parti"] + parties["Mhp"]
millet_ittifaki_toplam_oy = parties["Chp"] + parties["İyi Parti"]

if cumhur_ittifaki_toplam_oy > millet_ittifaki_toplam_oy:
    print("Cumhur ittifakı iktidar oldu!")
elif cumhur_ittifaki_toplam_oy < millet_ittifaki_toplam_oy:
    print("Millet ittifakı iktidar oldu!")
else:
    print("Seçimler berabere sonuçlandı!")

