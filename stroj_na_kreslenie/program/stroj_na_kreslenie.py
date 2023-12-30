from turtle import *
def ovladac_kor(rob, hod):
    rob = rob.upper()
    if rob == "F":
        forward(hod)
    elif rob == "B":
        backward(hod)
    elif rob == "R":
        right(hod)
    elif rob == "L":
        left(hod)
    elif rob == "U":
        penup()
    elif rob == "D":
        pendown()
    elif rob == "N":
        reset()
    else:
        print("Neznamy prikaz")
def retazcovy_umelec(program):
    prikazy = program.split("-")
    for prikaz in prikazy:
        prik_dlz = len(prikaz)
        if prik_dlz == 0:
            continue
        prik_typ = prikaz[0]
        cis = 0
        if prik_dlz > 1:
            cis_retaz = prikaz[1:]
            cis = int(cis_retaz)
        print(prikaz, ":", prik_typ, cis)
        ovladac_kor(prik_typ, cis)
pomocka = '''Zadaj program pre korytnacku:
napr. F100-R45-U-F100-L45-D-F100-R90-B50
N - Nová kresba
U/D = Pero hore/dole
F100 - dopredu 100
B50 - dozadu 50
R90 - doprava 90 stupnov
L45 - dolava 45 stupnov'''
obr = getscreen()
while True:
    prikazy = obr.textinput("Stroj na kreslenie", pomocka)
    print(prikazy)
    if prikazy == None or prikazy.upper() == "KONIEC":
        break
    retazcovy_umelec(prikazy)

    
