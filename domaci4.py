from functools import reduce
from time import time

# 17.
def vrijeme_izvrsavanja_funkcije(funct):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Funkcija je zavrsila izvrsavanje za {t2-t1} vremena.")
        return result
    return wrapper


#1.
def longest_string_reduce(lista):
    return(reduce(lambda a, b: a if len(a) > len(b) else b, lista))

lista = ["flower","flow","flightyyy"]
#print(longest_string_reduce(lista))

#2.
def above_average(imena, ocjene):
    
    result = (filter(lambda x: x[1] > 8.5, zip(imena, ocjene)))
    return list(result)

imena = ["Ana", "Nikola", "Mia"]
ocjene = [9, 7, 8.7]

#print(above_average(imena, ocjene))

#3.
@vrijeme_izvrsavanja_funkcije
def filtriraj(lista):

    temp = list(filter(lambda x: x['godine'] > 21, lista))

    res = sorted(temp, key=lambda x: x['prosjek'])
    return res

studenti = [
    {'ime': 'Ana', 'godine': 22, 'prosjek': 9.1},
    {'ime': 'Marko', 'godine': 21, 'prosjek': 8.7},
    {'ime': 'Ivana', 'godine': 23, 'prosjek': 9.5},
    {'ime': 'Petar', 'godine': 20, 'prosjek': 9.2},
    {'ime': 'Jelena', 'godine': 22, 'prosjek': 8.9}
]

#print(filtriraj(studenti))

#4.
def total_count_words(lista):

    lista_rijeci = list(map(lambda x: len(x.split()), lista))
    return lista_rijeci

l = ["Hello, World!", "Python is cool", "Functional programming rocks"]

#print(total_count_words(l))

#5.
from functools import reduce

@vrijeme_izvrsavanja_funkcije
def average_grade_per_subject(ocjene):
    
    ocjene_po_predmetu = {}

    def dodaj_ocjenu(predmet, ocjena):
        if predmet in ocjene_po_predmetu:
            ocjene_po_predmetu[predmet].append(ocjena)
        else:
            ocjene_po_predmetu[predmet] = [ocjena]

    
    def prosjecna_ocjena(ocjene):
        return sum(ocjene) / len(ocjene)

    for ime, ocjena, predmet in ocjene:
        dodaj_ocjenu(predmet, ocjena)

    
    prosjecne_ocjene = map(lambda x: (x, prosjecna_ocjena(ocjene_po_predmetu[predmet])), ocjene_po_predmetu)

    return list(prosjecne_ocjene)


ocjene = [("Ana", 8.5, "Matematika"), ("Marko", 7.5, "Matematika"), ("Ana", 9.0, "Fizika"), ("Marko", 8.0, "Fizika")]
#print(average_grade_per_subject(ocjene))

#6.
def diferencija(lista):

    res = list(map(lambda x: lista[x-1] - lista[x], range(1, len(lista))))
    return res

#print(diferencija([15, 25, 33, 9]))

#7.
def frequency(lista):
    
    temp = list(map(lambda x: {x: lista.count(x)}, lista))
    
    
    return temp

print(frequency(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))


# 8.
@vrijeme_izvrsavanja_funkcije
def pravougaonik():
    with open("Desktop/rectangles.txt") as stranice:
        kvadrati = []
        maks = 0
        for i in stranice.readlines():
            i = (i.removesuffix('\n')).split(',')
            a = float(i[0])
            b = float(i[1])
            if a == b:
                kvadrati.append((a, b))
                if a*b > maks:
                    maks = a*b
    return kvadrati, maks


#print(pravougaonik())


# 9.
def naselja_maks_stanovnika():

    grad = input('Unesite naziv grada: ')
    maks_naselje = ''
    maks_stanovnici = 0
    with open('Desktop/cities.txt') as naziv:
        for i in naziv.readlines():
            g = (i.removesuffix('\n')).split(',')
            ime_grad = g[0]
            ime_naselje = g[1]
            br_stanovnika = int(g[2])
            if ime_grad.lower() == grad.lower() and br_stanovnika > stanovnika_max:
                stanovnika_max = br_stanovnika
                naselje_max = ime_naselje
    return f"{grad} : {maks_stanovnici}"


# print(naselja_maks_stanovnika()

# 10.
def najmanji_broj_stanovnika():
    drzava = input("Unesite naziv drzave: ")
    minn = 999999999999
    grad = ''
    with open("Desktop/population.txt") as my_file:
        for line in my_file.readlines():
            temp = (line.removesuffix('\n')).split(',')
            drzava1 = temp[0]
            grad1 = temp[1]
            broj_stanovnika = int(temp[2])
            if drzava1.lower() == drzava.lower() and broj_stanovnika < minn:
                minn = broj_stanovnika
                grad = grad1
        return grad


#print(najmanji_broj_stanovnika())


# 11.
def broj_stanovnika():
    unos = input('Unesite naziv drzave: ')
    ukupno_stanovnika = 0
    with open('Desktop/population.txt') as fajl:
        for linija in fajl.readlines():
            tmp = (linija.removesuffix('\n')).split(',')
            drzava = tmp[0]
            br_stanovnika = int(tmp[2])
            if drzava.lower() == unos.lower():
                ukupno_stanovnika += br_stanovnika
    return ukupno_stanovnika


# print(broj_stanovnika())

# 12.
def heksadecimalni():
    hexa, ukupno = 0, 0

    with open('Desktop/hexa.txt') as fajl:
        for broj in fajl.readlines():
            if broj.startswith('0x'):
                hexa = int((broj.removesuffix('\n')), 0)
                if hexa % 10 == 3:
                    ukupno += hexa

    return ukupno

#print(heksadecimalni())


# 14.
def append_to_file(lista):
    with open('Desktop/students.txt', mode='w') as fajl:
        fajl.write("Naziv, Opis, Godina, Kolicina, Cijena\n")
        for student in lista:
            fajl.write(f'{student['ime']},{student['prezime']},{student['godina']},{
                       student['prosjek']}\n')


'''append_to_file([{'ime': 'Ana', 'prezime': 'Markovic', 'godina': 1, 'prosjek': 9.2},
    {'ime': 'Petra', 'prezime': 'Popovic', 'godina': 2, 'prosjek': 8.3},
    {'ime': 'Ivan', 'prezime': 'Pincic', 'godina': 3, 'prosjek': 7.5}])
'''

def get_students_with_greater_grade(year, grade):
    ocjene = {'A': (9.5, 10), 'B': (8.5, 9.5),
             'C': (7.5, 8.5), 'D': (6.5, 7.5),
             'E': (6, 6.5)}
    if grade not in ocjene.keys():
        return "Nepravilan unos ocjene."
    if 1 < year > 8:
        return "Nepravilan unos godine.."

    studenti = []
    ocjena = ocjene[grade][0]
    with open('Desktop/students.txt') as file:
        next(file)
        for student in file:
            s = student.split(',')
            if (int(s[2]) == year) and (float(s[3]) >= ocjena):
                studenti.append({'ime': s[0], 'prezime': s[1],
                                'godina': int(s[2]), 'prosjek': float(s[3])})
    return studenti

