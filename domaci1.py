import math
#1.
def pravougaonik(a, b):

    povrsina = a * b
    obim = 2*(a + b)

    print(f"Povrsina: {povrsina}, Obim: {obim}")

pravougaonik(5, 3)

#2.
def kvadratna_jednacina(a, b, c):
  
  d = b**2 - 4*a*c
  x1 = (-b + math.sqrt(d)) / 2*a
  x2 = (-b - math.sqrt(d)) / 2*a

  print(f"x1 = {x1}, x2 = {x2}")

#3.
def razlika_kvadrata(a, b):
  
  razlika = (a+b)*(a-b)
  return razlika

#4.
def sportista(a, b):
  
  obim = 2*(a+b)
  return 4*obim

#5.
def list_papira(sirina, visina):
   
   p = (sirina/10) * (visina/10)
   return p

#6.
def kvadrat_trinoma(a, b, c):
   
   razlika = a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c
   return razlika

#7.
def biciklizam(sati):
   
   litri = math.floor(sati*0.5)
   print(litri)

biciklizam(11.8)

#8.
def duzina_kruznog_luka(P):
   
   r = math.sqrt(P/math.pi)
   l = 2*(math.pi)*r
   return l

print(duzina_kruznog_luka(78.54))

#9.
def fudbalski_teren(d, s, r):
   ograda = 2*(d+r) + 2*(s+r)
   return ograda

print(fudbalski_teren(3, 5, 2))


#10.
def pravougaonik_koordinate(x1, y1, x2, y2):
   
   a = x2 - x1
   b = y2 - y1

   p = a*b
   o = 2*(a+b)
   print(f"Povrsina: {p}, obim: {o}")

pravougaonik_koordinate(3, 4, 6, 7)

#11.
def euclide_distance(x1, y1, x2, y2):
   
   d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
   return d

#12.
def godina_rodjenja(n):
   
   god = 2024 - n
   return god

#14.
def procjena_cijene_stana(velicina, lokacija, parking):

    if(parking == 'ima'):
        parking = 1
    else:
      parking = 0

    if(lokacija == 'zona 1'):
       lokacija = 3
    elif(lokacija == 'zona 2'):
       lokacija = 2
    else:
       lokacija = 1
       
    lokacija *= velicina * 5
    parking *= lokacija * 10

    cijena = velicina * 1200 + lokacija + parking - 1000
    return cijena

print(procjena_cijene_stana(45, 'zona 1', 'ima'))

#15.
def povrsina_trougla(x1, y1, x2, y2, x3, y3):
   #a je rast (x1, y1) (x2, y2)
   #b (x2, y2)(x3, y3)
   #c (x3, y3)(x1, y1)

   a = euclide_distance(x1, y1, x2, y2)
   b = euclide_distance(x2, y2, x3, y3)
   c = euclide_distance(x3, y3, x1, y1)

   s = (a+b+c) / 2
   p = math.sqrt(s*(s-a)*(s-b)*(s-c))
   return p

print(povrsina_trougla(1, 1, 3, 3, 4, 5))

#16.
def taksi_cijena(km):
   
   cijena = 1 + km * 0.5
   return cijena

#17.
def knjizara(cijena, popust):
   
   konacna_cijena = cijena - (popust/100)*cijena

   return konacna_cijena


#18.
def playStation_cijena(cijena):
   
   cijena_porast = cijena + (10/100)*cijena
   cijena_pad = cijena_porast - (10/100)*cijena_porast

   print(f"Cijena konzole nakon promjena iznosi {cijena_pad}")

#19.
def zbir_cifara3(br):
   
   j = br % 10
   d = br // 10 % 10
   s = br // 100

   return j+d+s

#20.
def prizvod_cifara3(br):
   
   j = br % 10
   d = br // 10 % 10
   s = br // 100

   return j*d*s

def desifruj(broj):
   
   proizvod = prizvod_cifara3(broj)
   zbir = zbir_cifara3(broj)

   sifra = proizvod - zbir
   return sifra

#21.
def sifra_sef(br):
   j = br % 10
   d = br % 100 % 10
   s = br // 100 % 10
   h = br // 1000

   s1 = razlika_kvadrata(s, d)

   sifra = (h+j)**2 - s1
   return sifra

#22.
def takmicenje_matematika():
   n = int(input("Unesite ukupan broj ucenika: "))
   k = int(input("Unesite broj ucenika na drugoj strani: "))
   p1 = float(input("Unesite prosjecan br. poena ucenika na 1. strani: "))
   p2 = float(input("Unesite prosjecan br. poena ucenika na 2. strani: "))

   s = n - k  # broj ucenika na 1. strani
   br1 = p1 * s
   br2 = p2 * k
   pom = (br1 + br2) / n
   ukupno = round(pom, 2)
   return ukupno


print(takmicenje_matematika())

#23.
def srednja_vrijednost(a, b):
   return (a+b)/2

#24.
def zamijeni(x, y):
   
   temp = x
   x = y
   y = temp

   print(f"X={x} , Y={y}")

zamijeni(7, 10)

#25.
def rastojanje_metri(broj):
   return broj // 100

#26.
def sprat(n):
   sprat = n % 100 % 10
   return sprat

#27.
def suma_cifara(n):
   suma = 0
   while(n != 0):
      suma += n % 10
      n //= 10  
   return suma

def kvadrat_zbira_cifara4(br):
   n = suma_cifara(br)
   return n**2

#28.
def zamijeni_cifre(br):
   j = br % 10
   d = br // 10 % 10
   s = br // 100

   novi = j*100 + d*10 + s
   print(f"Novi broj je: {novi}")

zamijeni_cifre(456)

#29.
def srednja_tacka(x1, y1, x2, y2):
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2
    return x3, y3

def glavna(x1, y1, x2, y2):
   x3, y3 = srednja_tacka(x1, y1, x2, y2)
   distanca = euclide_distance(x1, y1, x3, y3)
   return distanca

#30.
def kvadrat_pravougaonik():
   pp = 545 * 130
   pk = 65**2

   return pp // pk

#31.
def povrsina_ekrana(d, odnos_stranica):
   
    sirina, visina = odnos_stranica.split(":")
    sirina = int(sirina)
    visina = int(visina)

    
    a = math.sqrt((d ** 2 / (1 + (visina / sirina) ** 2)) )
    b = a * visina / sirina

   
    povrsina = a * b
    return povrsina
 

#32.
def sestocifreni_broj(n):
   f = n % 10
   e = n % 100 % 10
   d = n % 1000 // 100
   c = n // 1000 % 10
   b = n // 10000 % 10
   a = n // 100000

   if(a * c + 2 + f == b + d * e):
      return True
   else:
      return False

#33.
def poligoni(n, a, b):
   povrsina_kvadrata = n**2
   povrsina_poljane = a*b

   return povrsina_poljane // povrsina_kvadrata

#34.
def laboratorijski_sektor(n):
   
   suma = suma_cifara(n)**2
   treca = n // 1000 % 10
   cetvrta = n % 1000 // 100

   broj = suma - treca * cetvrta
   return broj
   
#35.
def stambena_jedinica(br):
   poslednja = br % 10
   srednja = br // 100 % 10

   return poslednja + srednja

