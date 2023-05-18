def hamlex(x):
    kesisim={x}
    while oyun_kume.intersection(kesisim) != {x}:
        print("hatali hamle lütfen yeniden dene !")
        x=input("x koymak istediğiniz yeri secin:")
        kesisim={x}
    oyun_kume.remove(x)
    x=oyun.index(x)
    oyun[x]="x"
    for i in range(17):
        if i==0 or i==8 or i==16:
            print(oyun[i],oyun[i+1],oyun[i+2],oyun[i+3],oyun[i+4])
        elif i==5 or i==13:
            print(oyun[i]," ",oyun[i+1]," ",oyun[i+2])
    return 0

def hamleo(o):
    kesisim={o}
    while oyun_kume.intersection(kesisim) != {o}:
        print("hatali hamle lütfen yeniden dene !")
        o=input("o koymak istediğiniz yeri secin:")
        kesisim={o}
    oyun_kume.remove(o)
    o=oyun.index(o)
    oyun[o]="o"
    for i in range(17):
        if i==0 or i==8 or i==16:
            print(oyun[i],oyun[i+1],oyun[i+2],oyun[i+3],oyun[i+4])
        elif i==5 or i==13:
            print(oyun[i]," ",oyun[i+1]," ",oyun[i+2])
    return 0


def kontrol():
    if oyun[0] == oyun[2] and oyun [2]== oyun[4]:
        print("oyunu ",oyun[0]," kazanadi")
        return 1
    if oyun[8] == oyun[10] and oyun[10] == oyun[12]:
        print("oyunu ",oyun[8]," kazanadi")
        return 1
    if oyun[16] == oyun[18] and oyun[18] == oyun[20]:
        print("oyunu ",oyun[16]," kazanadi")
        return 1
    if oyun[0] == oyun[10] and oyun[10] == oyun[20]:
        print("oyunu ",oyun[0]," kazanadi")
        return 1
    if oyun[0] == oyun[8] and oyun [8]== oyun[16]:
        print("oyunu ",oyun[0]," kazanadi")
        return 1
    if oyun[2] == oyun[10] and oyun [10]== oyun[18]:
        print("oyunu ",oyun[2]," kazanadi")
        return 1
    if oyun[4] == oyun[12] and oyun [12]== oyun[20]:
        print("oyunu ",oyun[4]," kazanadi")
        return 1
    if oyun[4] == oyun[10] and oyun [10]== oyun[16]:
        print("oyunu ",oyun[4]," kazanadi")
        return 1

oyun = [ "1","|","2","|","3","-","-","-","4","|","5","|","6","-","-","-","7","|","8","|","9"]
oyun_kume = { "1","|","2","|","3","-","-","-","4","|","5","|","6","-","-","-","7","|","8","|","9" }
toplam_hamle=0
for i in range(17):
    if i==0 or i==8 or i==16:
        print(oyun[i],oyun[i+1],oyun[i+2],oyun[i+3],oyun[i+4])
    elif i==5 or i==13:
        print(oyun[i]," ",oyun[i+1]," ",oyun[i+2])

while kontrol()!=1:
        x=input("x koymak istediginiz yeri secin:")
        hamlex(x)
        toplam_hamle=toplam_hamle+1
        if kontrol()==1:
            break
        if toplam_hamle==9:
            print("oyun berabere :)")
            break
        o=input("o koymak istediğiniz yeri secin:")
        hamleo(o)
        toplam_hamle=toplam_hamle+1
