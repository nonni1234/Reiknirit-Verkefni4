import re

def Heilda(f,x): # skilar heildi á fallinu: 'f' með x gildinu: 'x'
    merki = re.findall("[+-]",f)
    lidir = re.split('[+-]',f)
    if f[0] == '-':
        lidir.remove('')
    else:
        merki.insert(0,'+')

    tel = 0
    summa = 0
    for i in lidir:
        lidur = i.split('x')

        if len(lidur) == 1: # ef lidur er bara tala
            if merki[tel] == "+":
                summa += (int(lidur[0]) * x)
            else:
                summa -= (int(lidur[0]) * x)

        elif lidur[0] == '' and lidur[1] == '': # ef lidur er bara x
            if merki[tel] == '+':
                summa += (x ** 2 / 2)
            else:
                summa -= (x ** 2 / 2)

        elif lidur[0] == '' and lidur[1] != '': # ef lidur er x með veldi
            if merki[tel] == '+':
                summa += (x ** (int(lidur[1]) + 1) / (int(lidur[1]) + 1) )
            else:
                summa -= (x ** (int(lidur[1]) + 1) / (int(lidur[1]) + 1) )

        elif lidur[0] != '' and lidur[1] == '': # ef lidur er tala með x t.d.: '2x'
            if merki[tel] == '+':
                summa += (int(lidur[0]) * x ** 2 / 2)
            else:
                summa -= (int(lidur[0]) * x ** 2 / 2)

        else: # ef lidur er tala með x og veldi t.d: '2x2'
            if merki[tel] == '+':
                summa += (int(lidur[0]) * x ** (int(lidur[1]) + 1) / (int(lidur[1]) + 1))
        tel += 1
    return summa

fall = input("Sláðu inn f(x): ")

em = int(input('Sláðu inn x fyrir efri mörk: '))
nm = int(input('Sláðu inn x fyrir neðri mörk: '))

flatarmal = Heilda(fall,em) - Heilda(fall,nm)

print(f'Flatarmálið fyrir {fall} á milli {nm} og {em} er {flatarmal}')