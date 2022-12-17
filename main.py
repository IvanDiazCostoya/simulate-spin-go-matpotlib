import numpy as np
import matplotlib.pyplot as plt
import csv

spins_data = []

with open('datos_spins_0.csv') as csvfile:

    reader = csv.reader(csvfile, delimiter=';')

    sites = []
    for i in reader:
        sites.append(i)

files =['datos_spins_1.csv',
        'datos_spins_2.csv',
        'datos_spins_3.csv',
        'datos_spins_4.csv',
        'datos_spins_5.csv',
        'datos_spins_6.csv',
        'datos_spins_7.csv']

# import data
for index, filename in enumerate(files):

    with open(filename) as csvfile:

        reader = csv.reader(csvfile, delimiter=';')

        # Skip header
        next(reader)

        spins_data.append([])

        for i in reader:
            spins_data[index].append(i)

# Generates the chips ev that we earn in n spins with a normal distribution

# nspins = 1000; buyin = 10; sala = 1; evchips = 70; rakeback = 15
# modify ev chips with variance
# write mean without variance in the graph based on chips ev
# sim_spins(1000, '10', 5, 70, 15)

# Poker sites codes:
# PS.es	       1
# PS.com	   2
# Party.es	   3
# Party.com	   4
# Sportium.es  5
# Winamax.es   6
# Winamax.fr   7

def sim_spins(nspins, buyin, sala, evchips, rakeback):

    rakeback = rakeback / 100

    # Keep the data from this site
    spins_data_n = spins_data[sala - 1]

    # Keep data from this stake
    # print(spins_data_n[1] == buyin)

    stake = [g for g, h in enumerate(spins_data_n) if h[1] == buyin]
    stake = stake[0]

    spins_data_n = spins_data_n[stake]

    # Add variance to the ev chips with standard deviation 750
    s = np.random.normal(evchips, 750, nspins)
    evchips2 = np.average(s)

    # Generate nspins spins

    # x3 is a random number to help  calculate the multiplier. It goes from 1 to maximum number of cases (tipically 1000.000)
    spins_data_n[4] = int(spins_data_n[4])
    x3 = np.random.choice(spins_data_n[4], nspins, replace = True)

    # x4 will be the multiplier of every spin
    x4 = [-1] * nspins

    # Change every value in x3 by its multiplier. x2 -> 8 or 9 and 1 is the highest multiplier

    # # A los 3 más altos les restamos 10% del premio porque luego se los añadiremos a los 3 jugadores

    spins_data_n[3] = int(spins_data_n[3])

    if int(spins_data_n[3]) == 8:

        for y in range(13, 21):

            spins_data_n[y] = int(spins_data_n[y])

        pr = spins_data_n[13:21]
        pr.reverse()
        pr = np.cumsum(pr)


        total_cases = spins_data_n[4]

        # Maximum multiplier
        x4 = [0 if b <= pr[7] else x4[a] for a, b in enumerate(x3)]
        x4 = [1 if b <= pr[6] else x4[a] for a, b in enumerate(x3)]
        x4 = [2 if b <= pr[5] else x4[a] for a, b in enumerate(x3)]
        x4 = [3 if b <= pr[4] else x4[a] for a, b in enumerate(x3)]
        x4 = [4 if b <= pr[3] else x4[a] for a, b in enumerate(x3)]
        x4 = [5 if b <= pr[2] else x4[a] for a, b in enumerate(x3)]
        x4 = [6 if b <= pr[1] else x4[a] for a, b in enumerate(x3)]
        # Minimum multiplier
        x4 = [7 if b <= pr[0] else x4[a] for a, b in enumerate(x3)]

        Mat_premios = []

        for y in range(45, 69):

            spins_data_n[y] = float(spins_data_n[y])

        Mat_premios.append(spins_data_n[45:48])
        Mat_premios.append(spins_data_n[48:51])
        Mat_premios.append(spins_data_n[51:54])
        Mat_premios.append(spins_data_n[54:57])
        Mat_premios.append(spins_data_n[57:60])
        Mat_premios.append(spins_data_n[60:63])
        Mat_premios.append(spins_data_n[63:66])
        Mat_premios.append(spins_data_n[66:69])

        spins_data_n[70] = float(spins_data_n[70])
        Rake = spins_data_n[70]

    if int(spins_data_n[3]) == 9:

        for y in range(14, 23):

            spins_data_n[y] = int(spins_data_n[y])

        pr = spins_data_n[14:23]
        pr.reverse()
        pr = np.cumsum(pr)

        total_cases = spins_data_n[4]

        # Maximum multiplier
        x4 = [0 if b <= pr[8] else x4[a] for a, b in enumerate(x3)]
        x4 = [1 if b <= pr[7] else x4[a] for a, b in enumerate(x3)]
        x4 = [2 if b <= pr[6] else x4[a] for a, b in enumerate(x3)]
        x4 = [3 if b <= pr[5] else x4[a] for a, b in enumerate(x3)]
        x4 = [4 if b <= pr[4] else x4[a] for a, b in enumerate(x3)]
        x4 = [5 if b <= pr[3] else x4[a] for a, b in enumerate(x3)]
        x4 = [6 if b <= pr[2] else x4[a] for a, b in enumerate(x3)]
        x4 = [7 if b <= pr[1] else x4[a] for a, b in enumerate(x3)]
        # Minimum multiplier
        x4 = [8 if b <= pr[0] else x4[a] for a, b in enumerate(x3)]

        Mat_premios = []

        for y in range(50, 77):

            spins_data_n[y] = float(spins_data_n[y])

        Mat_premios.append(spins_data_n[50:53])
        Mat_premios.append(spins_data_n[53:56])
        Mat_premios.append(spins_data_n[56:59])
        Mat_premios.append(spins_data_n[59:62])
        Mat_premios.append(spins_data_n[62:65])
        Mat_premios.append(spins_data_n[65:68])
        Mat_premios.append(spins_data_n[68:71])
        Mat_premios.append(spins_data_n[71:74])
        Mat_premios.append(spins_data_n[74:77])

        spins_data_n[78] = float(spins_data_n[78])
        Rake = spins_data_n[78]

    Rake = (1 - rakeback) * Rake

    # Los spins que ganas los ganas cuando consigues 1000 fichas, con las chipsev calculamos cuantos spins acabamos
    # con 1000 fichas y los demás asumimos que quedamos a pre (ganar 1 y perder 2)

    uiui2 = int((evchips2 * nspins) / 1000)

    # De los restantes ganamos un tercio (quedar a pre en fichas)
    rrr = int(((nspins - uiui2) / 3))

    # Total spins que ganamos
    uiui2 = uiui2 + rrr


    # Total spins que quedamos 2º, el resto quedamos 3º
    piropiro = int(nspins / 3)

    # Ponemos como ganadores los primeros uiui2 spins (marcados con 1) después los 2 y después los 3
    x5 = [3] * nspins

    for i in range(uiui2):
        x5[i] = 1

    for i in range(uiui2, (uiui2 + piropiro)):
        x5[i] = 2

    # Los barajamos
    np.random.shuffle(x5)

    # x4 is multiplier
    # x6 will be the prize
    x6 = x4

    for i in range(nspins):

        x6[i] = Mat_premios[x4[i]][x5[i]-1]

    buyin_num = float(spins_data_n[2])

    x6 = [a - (buyin_num - buyin_num * Rake * rakeback) for a in x6]
    # Segunda parte beneficio neto esperado en $ o € desués después de todos esos spins
    x6 = np.cumsum(x6)

    return (x6)

# Funcion que calcula el EV solo
# EV(1000, 10, 7, 70, 15)

def EV(nspins, buyin, rake, evchips, rakeback):

   rakeback = rakeback / 100
   rake = rake / 100
   rake = (1 - rakeback) * rake
   EvROI = ((((evchips + 500) * (1 - rake)) / 500) - 1) * 100
   return((buyin * (EvROI / 100) * nspins))

def graf_spins(nspins, name, buyin, sala, evchips, rakeback, ngraph):

    data = []
    ev = []

    for i in range(ngraph):
        data.append(sim_spins(nspins, name, sala, evchips, rakeback))

    ev = EV(nspins, buyin, sala, evchips, rakeback)

    xpoints = np.arange(nspins)

    for i in range(ngraph):
        plt.plot(xpoints, data[i])

    plt.plot((0, nspins), (0, ev))

    plt.grid(color='lightblue', linestyle='-.', linewidth=0.7)

    tit = sites[sala-1][0] + ', ' + name + ' ' + sites[sala-1][2] + ', EV ' + str(round(ev, 2)) + ' ' + sites[sala-1][2]

    plt.title(tit)
    plt.show()

graf_spins(10000, '10', 10, 3, 75, 15, 10)
