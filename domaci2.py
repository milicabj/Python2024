import math
import string

#1.
def paran_broj(n):
    if(n % 2 == 0):
        print("Portal se otvara!")
    else:
        print("Portal ostaje zatvoren!")

#2.
def berba_jabuka(p, m):
    if(p > m):
        print("Petar je ubrao vise jabuka od Milosa.")
    else:
        print("Milos je ubrao vise jabuka od Petra.")

#3. 
def pristup_ispitu(prisustvo, seminarski_radovi):
    if(prisustvo > 75 and seminarski_radovi == 1):
        return True
    else:
        return False

#4.
def kucni_red(sat):
    if(sat < 6 or (sat > 13 and sat < 17) or sat > 22):
        return False
    else:
        return True
    
#5.
def trougao(a, b, c):
    if(a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False

#6.
def kretanje_po_zici(x, y):
    if (y == 2 * x + 5):
        return True
    else:
        return False
    
#7.
def takmicenje(mat1, prog1, mat2, prog2):
    ukupno1 = mat1 + prog1 
    ukupno2 = mat2 + prog2

    if(ukupno1 > ukupno2):
        print(f"Pobjednik je takmicar sa {ukupno1} poena.")
    elif(ukupno1 < ukupno2):
        print(f"Pobjednik je takmicar sa {ukupno2} poena.")
    else:
        if(prog1 > prog2):
            print(f"Pobjednik je takmicar sa {prog1} poena iz programiranja.")
        else:
            print(f"Pobjednik je takmicar sa {prog2} poena iz programiranja.")

#8.
def uspjeh_ucenika(prosjek):
    if(prosjek >= 4.5):
        print("Odlican .")
    elif(prosjek >= 3.5 and prosjek < 4.5):
        print("Vrlodobar.")
    elif(prosjek >= 2.5 and prosjek < 3.5):
        print("Dobar.")
    elif(prosjek >= 2 and prosjek < 2.5):
        print("Dovoljan.")
    else:
        print("Nedovoljan.")

#9.
def zavjesa_prozor(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = abs(x2 - x1)
    b1 = abs(y2 - y1)

    povrsina_zavjese = a1 * b1

    a2 = abs(x4 - x3)
    b2 = abs(y4 - y3)

    povrsina_prozora = a2 * b2

    if(povrsina_zavjese >= povrsina_prozora):
        print(f"Zavjesa ce prekriti prozor.")
    else:
        print(f"Zavjesa nece prekriti prozor.")

#10.
def pikado_strelica(x1, y1, r, x2, y2):
    # (x1, y1) su koordinate centra kruga
    # (x2, y2 )su kordinate tacke

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if(d <= r):
        print("Strelica je pogodila pikado tablu!")
    else:
        print("Strelica nije pogodila pikado tablu!")

#11.
def mrav(x_desno, y_desno, x_lijevo, y_lijevo, x_mrav, y_mrav):
    if(x_mrav <= x_desno and x_mrav >= x_lijevo and y_mrav <= y_lijevo and y_mrav >= y_lijevo):
        return True
    else:
        return False
    
#12.
def dvocifreni_broj(broj):
    druga_cifra = broj % 10
    prva_cifra = broj // 10

    if(prva_cifra > druga_cifra):
        return prva_cifra - druga_cifra
    elif(prva_cifra < druga_cifra):
        return prva_cifra + druga_cifra
    else:
        return prva_cifra * druga_cifra

#13. 
def veca_povrsina(r1, r2):
    p1 = r1**2 * math.pi
    p2 = r2**2 * math.pi

    o1 = 2 * math.pi * r1
    o2 = 2 * math.pi * r2

    if(p1 > p2):
        print(o1)
    else:
        print(o2)

#14.
def cijene_proizvoda(x1, x2, x3):
    if(x1 + x2 < x1 + x3):
        najmanji_par = x1 + x2
    else:
        najmanji_par = x1 + x3

    if(x2 + x3 < najmanji_par):
        najmanji_par = x2 + x3

    return najmanji_par
    
#15.
def prestupna(godina):
    if((godina % 4 == 0 and godina % 100 !=0) or godina % 400 == 0):
        return True
    else:
        return False
    
#16.
def tacka_pravougaonik(x, y, x1, y1, x2, y2):
    if((x >= x1 and x <= x2) and (y <= y1 and y >= y2)):
        return True
    else:
        return False
#17.
       
#18.
def agregatno_stanje(temperatura):
    if(temperatura > 0 and temperatura < 100):
        print("Tecno.")
    elif(temperatura <= 0):
        print("Cvrsto.")
    else:
        print("Gasovito.")

#19.
        
#20.
def zbir_cifara():
    n = int(input("Unesite cetvorocifren broj: "))
    suma = 0

    if(n % 2 == 0):
        while(n != 0):
            c = n % 10
            n //= 10
            if(c % 2 == 0):
                suma += c
        return suma
    else:
        while(n != 0):
            c = n % 10
            n //= 10
            if(c % 2 != 0):
                suma += c
        return suma

#21.
def izracunaj_y(x):
    y = 0

    if(x <= -7):
        y = -2*x + 7/2
    elif(x > -7 and x < 1):
        y = (x**2 -3*x + 5) / (x**2 + 2)
    elif(x >= 1 and x <= 8):
        y = math.sqrt(x**2 + 2*x + 2) + math.sqrt(abs(3/2*x - 4/7))
    else:
        y = abs(3/x**2 - 11*x)

    return y

#24.
def skrati_tekst(tekst):
    if(len(tekst) > 30):
        novi = tekst[:30] + "..."
        return novi
    else:
        return tekst
    
#25.
def ukloni_karaktere(s):
    novi = s[1:len(s)-1]
    print(novi)

#26.
def provjeri_brojni_sistem():

    broj = input("Unesite broj: ")
    prefiks = broj[0:2]

    if(prefiks == "0b"):
        print("Korisnik je unio binarni broj.")
    elif(prefiks == "0o"):
        print("Korisnik je unio oktalni broj.")
    elif(prefiks == "0x"):
        print("Korisnik je unio heksadecimalni broj.")
    else:
        print("Korisnik je unio dekadni broj.")

provjeri_brojni_sistem()

#27.
def samoglasnik_u_stringu(s):
    for i in range(0, len(s)):
        if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            print("String sadrzi barem jedan samoglasnik.")
            return
        

samoglasnik_u_stringu("Milica")

#28.
def target_string(string, target):
    if(string[len(string)-len(target):] == target):
        print("Da")
    else:
        print("Ne") 

target_string("www.google.com","me")

#29.
def binarni_broj(s):
    for i in range(0, len(s)):
        if(s[i] != '0' and s[i] != '1'):
            return False
        
    return True

#30.
def generisi():
    n = int(input("Unesite broj: "))

    zbir, proizvod, parni, neparni = 0, 1, 0, 0

    for i in range(1, n+1):
        if(i % 2 == 0):
            parni+=1
            zbir += i
        else:
            neparni += 1
            proizvod *= i

    print(f"Proizvod: {proizvod}, zbir: {zbir}, parnih: {parni}, neparnih: {neparni}")

generisi()

#31.
def generisi_segment():
    start = int(input("Unesite pocetni indeks: "))
    end = int(input("Unesite krajnji indeks: "))

    suma = 0
    for i in range(start, end+1):
        if(i % 2 == 0 and i % 4 != 0):
            suma += i**2

    return suma

print(generisi_segment())

#32.
def djelilac_segment(a, b, djelilac):
    suma = 0
    br_elem = 0

    for i in range(a+1, b):
        if(i % djelilac == 0):
            suma += i
            br_elem += 1

    print(f"Suma: {suma}, broj elemenata djeljivih sa {djelilac} : {br_elem}")

djelilac_segment(1, 6, 2)

#33.
def saberi_cifre(broj):
    suma = 0

    while(broj != 0):
        suma += broj % 10
        broj //= 10

    return suma

print(saberi_cifre(50987))

#34.
def izvuci_cifre(tekst):
    proizvod = 1

    for i in range(0, len(tekst)):
        if(tekst[i].isdigit()):
            proizvod *= int(tekst[i])

    return proizvod

print(izvuci_cifre("M2li3c51"))

#35.
def broj_cifara_string(s):
    broj = ""

    for i in s:
        if(i.isdigit()):
            broj += i

    return int(broj)

print(broj_cifara_string("Hi Mr.Rober53. How are you today? Today is 08.10.2019"))

#36.
def encript(string):
    
    novi = ""
    for i in string:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            novi += "1"
        else:
            novi += "0"
    
    return novi

print(encript("abaae"))

#37.
def random_list(tekst):
    broj = 0

    for i in tekst:
        if(i == '1'):
            broj += + 1
        elif(i == '0'):
            broj += 0
        else:
            broj -= 1

    if(broj > 0):
        print(f"Igrac je u plusu. Broj iznosi {broj}.")
    else:
        print(f"Igrac je u minusu. Broj iznosi {broj}.")

random_list("11100**")

#38.
def encript_vol2(string):

    novi = ""

    for i in string:
        if(i.isdigit()):
            if(int(i) % 2 == 0):
                novi += "0"
            else:
                novi += "1"
        else:
            pass

    print(novi)

encript_vol2("15023")

#39.
def br_cifara(n):
    br = 0
    while(n != 0):
        br += 1
        n //= 10
    
    return br

def narcissistic_number(broj):
    res = 0
    org = broj
    stepen = br_cifara(broj)

    while(broj != 0):
        res += (broj % 10)**stepen
        broj //= 10

    if(res == org):
        print("Da")
    else:
        print("Ne")

#40.
def apsolutna_suma(niz):
    suma = 0

    for i in niz:
        if(i < 0 and i % 2 == 0):
            suma += abs(i)

    return suma

print(apsolutna_suma([-2, 7, -5, 3, 1, -4]))

#41.
def manji_od_max(lista, max):
    br = 0

    for i in lista:
        if i < max:
            br +=1
    
    return br

#42.
def market(niz_cijena, n):
    br = 0

    for i in niz_cijena:
        br+=1

    return n * br

#43.
def prebroj_ocjene(niz_ocjena):
    br3 = 0
    br4 = 0
    br5 = 0

    for i in niz_ocjena:
        if(i == 3):
            br3 += 1
        elif(i == 4):
            br4 += 1
        else:
            br5 += 1

    print(f"Broj ucenika sa ocjenom 3: {br3}, ocjenom 4: {br4}, ocjenom 5: {br5}")

#44.
def maksimalan_broj(niz_posjeta):
    max = 0

    for i in niz_posjeta:
        if i > max:
            max = i

    return max

#45.
def average(niz):
    n = len(niz)
    suma = 0

    for i in niz:
        suma += i

    return suma / n

def veca_od_prosjecne(niz_plata):
    prosjecna_plata = average(niz_plata)
    br_zaposlenih = 0

    for i in niz_plata:
        if i > prosjecna_plata:
            br_zaposlenih += 1
    
    return br_zaposlenih

    
print(veca_od_prosjecne([500, 600, 700]))

#46.
def drugi_najveci(lista_primanja):
    nova = sorted(lista_primanja)

    return nova[-2]

print(drugi_najveci([900, 540, 690]))

#47.
def maks_i_min(a, b, c):

    maks, minn = 0, 0

    if(a > b and a > c):
        maks = a
    elif(b > a and b > c):
        maks = b
    else:
        maks = c
    
    if(a < b and a < c):
        minn = a
    elif(b < a and b < c):
        minn = b
    else:
        minn = c

    print(f"Maksimalan broj: {maks}, minimalan broj: {minn}")

#48.
def stepenuj(x, n):
    br = 1
    for i in range(0, n):
        br *= x

    return br

print(stepenuj(2, 3))

#49.
def skrati_string(s, duzina):
    novi = ""

    if(len(s) >= duzina):
        novi = s[:duzina] + "..."
    else:
        novi = s + "..."

    print(novi)

skrati_string("milica", 10)

#50.
def vrati_samoglasnike(string):

    novi = ""

    for char in string:
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            novi += char
    
    return novi

print(vrati_samoglasnike("bagatwiuioasbax"))

#51.
def validate_password(lozinka):

    duzina, mala_slova, velika_slova, cifre = False, False, False, False

    if(len(lozinka) < 8 or len(lozinka) > 100):
        duzina = False
    else:
        duzina = True
    
    skup_cifara = set("0123456789")
    mala_slova_skup = set(string.ascii_lowercase)
    velika_slova_skup = set(string.ascii_uppercase)
    lozinka_skup = set(lozinka)

    if len(lozinka_skup & skup_cifara) == 0:
        cifre = False
    else:
        cifre = True


    if len(lozinka_skup & mala_slova_skup) == 0:
        mala_slova = False
    else:
        mala_slova = True
    

    if len(lozinka_skup & velika_slova_skup) == 0:
        velika_slova = False
    else:
        velika_slova = True

    if(duzina == True and cifre == True and mala_slova == True and velika_slova == True):
        print("YES")
    else:
        print("NO")
    
            
validate_password("12AbbbEEE")
   
               
#52.
def prosiri_string(a, pre, suf, num):
    novi = ""
    prefiks = ""
    sufiks = ""

    for i in range(0, num):
       prefiks += pre
       sufiks += suf

    novi = prefiks + a + sufiks
    print(novi)

prosiri_string("test", "pr", "su", 2)

#54.
def slobodno_polje(string, poz):

    if(poz == 0):
        if(string[poz+1] == "0"):
            return True
        else:
            return False
    elif(poz == len(string)-1):
        if(string[poz-1] == "0"):
            return True
        else:
            return False
    else:
        if(string[poz-1] == "0" and string[poz+1] == "0"):
            return True
        else:
            return False
        
print(slobodno_polje("01010", 2))

#55.
def molekuli_vode(h, o):
    vodonik = h//2
    br_molekula = 0

    if(o - vodonik >= 0):
        br_molekula = vodonik
    else:
        br_molekula = o

    print(br_molekula)

molekuli_vode(1, 2)

#56.
def jednocifreni_negativni(s):

    br = 0
    for i in range(0, len(s)):
        if(s[i] == '-' and i+2 < len(s)):
            if(s[i+1].isdigit() and s[i+2].isdigit() == False):
                br += 1
        elif(s[i] == '-' and i+1 == len(s)-1):
            br += 1
        else:
            pass
    return br


print(jednocifreni_negativni("2+3-2-32+4-22-44"))

#60.
def gen_segment():
    start = int(input("Unesite start: "))
    kraj = int(input("Unesite kraj: "))

    suma = 0
    for i in range(start, kraj):
        if i % 3 == 0 and i % 6 != 0:
            suma += i**2

    return suma

#61.
def get_upper(string):
    novi = ""

    for i in string:
        if i.isupper():
            novi += i

    print(novi)

get_upper("Prva recenica. Ovo je druga recenica. Na kraju treca.")

#62.
def get_hexa(string):

    tokens = string.split(" ")
    br = 0

    for i in tokens:
        if i[0:2] == "0x":
            br += 1

    return br

print(get_hexa("12 0x1A 0001 121 0x2"))

#63. 
def najuza_rijec(string):

    tokens = string.split(" ")
    maks = tokens[0]

    for i in tokens:
        if(len(i) > len(maks)):
            maks = i

    return maks

print(najuza_rijec("Milicaaaa milica hyyyyyyyyyyyy"))

#64. 
def suma_max_min(broj):
    najmanji = 9
    najveci = 0
    broj1 = broj

    while(broj != 0):
        c = broj % 10
        broj //= 10
        if c > najveci:
            najveci = c

    while(broj1 != 0):
        c = broj1 % 10
        broj1 //= 10
        if c < najmanji:
            najmanji = c
            
    return najmanji + najveci

print(suma_max_min(123456789))

#67.
def ponavljanje(lista, broj):

    suma = 0
    for i in lista:
        if i == broj:
            suma += 1

    return suma

print(ponavljanje([3, 3, 3, 67, 889, 333], 3))

#68.
def uvecaj_zarade(lista, x):
    prosjek = 0
    n = len(lista)
    suma = 0

    for i in lista:
        suma += i

    prosjek = suma / n

    for i in range(0, n):
        if(lista[i] > prosjek):
            lista[i] += x

    return lista

print(uvecaj_zarade([500, 600, 750, 900], 100))