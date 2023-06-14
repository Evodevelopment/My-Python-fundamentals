from pom import znak, cti, klavesa, vymaz
from pom import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random
import time

# obrazovka je X: 0..70
#              Y: 0..30

# vymazat z obrazovky vsechno od predtim
vymaz()

# ohradka pro hada
for o in range(0, 70):
    znak(o, 0, "#")
    
for o in range(0, 70):
    znak(o, 30, "#")

for o in range(0, 30):
    znak(0, o, "#")

for o in range(0, 30):
    znak(70, o, "#")


# papani pro hada
for p in range(5):
    x = random.randint(1, 69)
    y = random.randint(1, 29)
    znak(x, y, "$")

# had
hlavickaX = 10
hlavickaY = 10
znak(hlavickaX, hlavickaY, "*")



# platnej smer je: dolu, nahoru, doleva, doprava
smer = "dolu"

while True:
    ## --- popojedem hadem --- ##

    # na zacatku kazdeho cyklu (kazdeho pohybu hada)
    # zjistime jestli byla stisknuta nejaka klavesa a pokud ano,
    # tak upravime smer
    posledniKlavesa = klavesa() 
    if posledniKlavesa == KEY_RIGHT:
        smer = 'doprava'
    if posledniKlavesa == KEY_LEFT:
        smer = 'doleva'
    if posledniKlavesa == KEY_UP:
        smer = 'nahoru'
    if posledniKlavesa == KEY_DOWN:
        smer = 'dolu'

    # spocitame si novou hlavicku
    # souradnice nove hlavicky zavisi na tom kam had miri
    # nahoru, dolu, doleva, doprava
    # pro kazdej smer se vypocita nova hlavicka jinak
    # my ji vypocitame podle toho jakej smer je aktualni
    if smer == "dolu":
        novaHlavickaX = hlavickaX
        novaHlavickaY = hlavickaY + 1
    if smer == "nahoru":
        novaHlavickaX = hlavickaX
        novaHlavickaY = hlavickaY - 1
    if smer == "doprava":
        novaHlavickaX = hlavickaX + 1
        novaHlavickaY = hlavickaY
    if smer == "doleva":
        novaHlavickaX = hlavickaX - 1
        novaHlavickaY = hlavickaY

    # kontrola jestli je souradnice nove hlavicky zradlo
    znakNaNoveHlavicce = cti(novaHlavickaX, novaHlavickaY)
    if znakNaNoveHlavicce == '$':
        hadPapal = True
    else:
        hadPapal = False


    # zkontrolujeme jestli bylo zradlo a ted muzem prekreslit
    # novou hlavickou 
    znak(novaHlavickaX, novaHlavickaY, "*")

    # vymazat starou hlavicku
    if hadPapal == False:
        znak(hlavickaX, hlavickaY, " ")

    # smrt hada
    if novaHlavickaX == 70 or novaHlavickaX == 0 or novaHlavickaY == 0 or novaHlavickaY == 30:
        znak(novaHlavickaX, novaHlavickaY, ' ')
        print('Umrel jsi')
        break
    
    # napsat novou hlavicku jako starou pro pristi cykl
    hlavickaX = novaHlavickaX
    hlavickaY = novaHlavickaY

    time.sleep(.1)



# pomucka random.randint(a, b)
# pomucka: znak(x, y, "*")
# pomucka: cti(x, y)
# pomucka: klavesa() vraci posledni stisknutou klavesu
# KEY_RIGHT
# KEY_LEFT
# KEY_UP
# KEY_DOWN
