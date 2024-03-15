#1.
def ends_with(string, s):
    result = []
    tokens = string.split(".")
    br = 0
    pom = []

    for i in range(len(tokens)-1):
        recenica = tokens[i]
        rijeci = recenica.split(" ")
        for i in range(len(rijeci)):
            if rijeci[i].endswith(s):
                br+=1     
                pom.append(rijeci[i])  
        pom.append(br)
        result.append(tuple(pom))
        br = 0
        pom.clear()
        

    print(result)

ends_with("Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.", "s")

#4.
def preklapanje(string):
    br = 0
    if len(string) == 1 or len(string) == 0:
        br = 0
    else:
        for i in range(len(string)-1):
            if string[i]  == string[i+1]:
                br += 1

    return br

print(preklapanje("aabaaaaccv"))

#5.
def najgori_odnos_poz_neg(podcast):

    tren_odnos = 0
    najgori_odnos = 10000
    tren_ime = ""
    res_ime = ""

    for p in podcast:
        tren_odnos = int(p['br_pozitivni'] / p['br_negativni'])
        tren_ime = p['naziv']
        if tren_odnos < najgori_odnos:
            najgori_odnos = tren_odnos
            res_ime = tren_ime
    
    return res_ime

podcasti = [{'naziv':'Español para principiantes', 'br_pozitivni':1000,'br_negativni':10},
{'naziv':'Philophize This!', 'br_pozitivni':500,'br_negativni': 30}, {'naziv':'Science VS.',
'br_pozitivni':600,'br_negativni': 45}]

print(najgori_odnos_poz_neg(podcasti))

#6.
class Televizor:
    def __init__(self):
        self._br_tekuceg_kanala = 0
        self._naziv_tekuceg_kanala = ""
        self._kanali = []
        self._jacina_tona = 0

    def set_naziv_tekuceg_kanala(self, naziv_kanala):
        self._naziv_tekuceg_kanala = naziv_kanala

    def set_kanali(self, kanali):
        self._kanali = kanali
    
    def set_jacina_tona(self, ton):
        if ton <= 10 and ton >= 0:
            self._jacina_tona = ton
        else:
            print("Neispravan unos tona.")
            return

    def set_br_tekuceg_kanala(self, br_kanala):
        if br_kanala >= 0 and br_kanala <= len(self._kanali):
            self._br_tekuceg_kanala = br_kanala
        else:
            print("Neispravan unos za broj tekuceg kanala.")
            return
    
    def get_br_tekuceg_kanala(self):
        return self._br_tekuceg_kanala
    
    def get_naziv_tekuceg_kanala(self):
        return self._naziv_tekuceg_kanala

    def get_kanali(self):
        return self._kanali
    
    def get_jacina_tona(self):
        return self._jacina_tona
    
    def dodaj_kanal(self, naziv_kanala):
        self._kanali.append(naziv_kanala)
    
    def obrisi_kanal(self, naziv_kanala):
            if naziv_kanala in self._kanali:
                self._kanali.remove(naziv_kanala)
            else:
                print("Kanal ne postoji.")
                return
    
    def pojacaj_ton(self):
        self.set_jacina_tona(self._jacina_tona+1)

    def ime_kanala(self, broj):
        if broj >= 1 and broj <= len(self._kanali):
             return self._kanali[broj-1]
        else:
            print("Nepostojeci broj kanala.")
            return


'''tv1 = Televizor()
tv1.dodaj_kanal("Vijesti")
tv1.dodaj_kanal("RTCG1")
tv1.dodaj_kanal("RTCG2")
tv1.obrisi_kanal('Pink')
print(tv1.ime_kanala(3))
tv1.pojacaj_ton()
print(tv1.get_jacina_tona())
print(tv1.get_kanali())
'''

class Book:
    def __init__(self, naslov, autor, god_izdanja, br_kopija):
        self._naslov = naslov
        self._autor = autor
        self._god_izdanja = god_izdanja
        self._broj_kopija = br_kopija

    def set_naslov(self, naslov):
        self._naslov = naslov
    
    def get_naslov(self):
        return self._naslov
    
    def set_autor(self, autor):
        self._autor = autor
    
    def get_autor(self):
        return self._autor
    
    def set_god_izdanja(self, god_izdanja):
        if god_izdanja > 0:
            self._god_izdanja = god_izdanja
        else:
            print("Neispravan unos godine izdanja.")
            return
    
    def get_god_izdanja(self):
        return self._god_izdanja
    
    def set_broj_kopija(self, br_kopija):
        if br_kopija >= 0 :
            self._broj_kopija = br_kopija
        else:
            print("Neispravan unos broja kopija u invertaru.")
            return
    
    def stampaj(self):
        return f"Naslov: {self._naslov}, autor: {self._autor}, god. izd: {self._god_izdanja}, br. kopija: {self._broj_kopija}"

class Library(Book):

    def __init__(self):
        self._lista_knjiga = []

    def dodaj_u_inventar(self, knjiga):
        self._lista_knjiga.append(knjiga)
    
    def obrisi_iz_inventara(self, knjiga):
        if knjiga in self._lista_knjiga:
            self._lista_knjiga.remove(knjiga)
        else:
            print("Knjiga se ne nalazi u inventaru.")
            return

    def pretrazi_naslov(self, naslov_knjige):
        lista_istih_naslova = [knjiga.stampaj() for knjiga in self._lista_knjiga if knjiga.get_naslov() == naslov_knjige]
        return lista_istih_naslova
    
    def pretrazi_autora(self, autor):
        lista_autori = [knjiga.stampaj() for knjiga in self._lista_knjiga if knjiga.get_autor() == autor]
        return lista_autori

    def trenutno_dostupne(self):
        lista = [knjiga.stampaj() for knjiga in self._lista_knjiga]
        return lista

    def izmijeni_knjigu(self, knjiga, atribut, nova_vrijednost):

        for book in self._lista_knjiga:
            if book.get_naslov() == knjiga.get_naslov():
                if atribut == "naslov":
                    book.set_naslov(nova_vrijednost)
                    return True
                elif atribut == "autor":
                    book.set_autor(nova_vrijednost)
                    return True
                elif atribut == "godina izdanja":
                    book.set_god_izdanja(nova_vrijednost)
                    return True
                else:
                    book.set_broj_kopija(nova_vrijednost)
                    return True


        print(f"Trazena knjiga se ne nalazi u inventaru biblioteke.")
        return False

'''
knjiga1 = Book("Lovac u žitu", "J.D. Salinger", 1951, 7)
knjiga2 = Book("Gospođica Julija", "August Strindberg", 1888, 5)
knjiga3 = Book("Na Drini ćuprija", "Ivo Andric", 1945, 10)
knjiga4 = Book("Seobe", "Milos Crnjanski", 1929, 8)
knjiga5 = Book("Zona Zamfirova", "Stevan Sremac", 1906, 6)
knjiga6 = Book("Prokleta Avlija", "Ivo Andric", 1967, 34)

biblioteka = Library()
biblioteka.dodaj_u_inventar(knjiga1)
biblioteka.dodaj_u_inventar(knjiga3)
biblioteka.dodaj_u_inventar(knjiga6)
biblioteka.dodaj_u_inventar(knjiga5)
biblioteka.dodaj_u_inventar(knjiga2)
biblioteka.dodaj_u_inventar(knjiga4)


biblioteka.izmijeni_knjigu(knjiga1, "broj kopija", 10)
print(biblioteka.pretrazi_autora("Ivo Andric"))
print(biblioteka.pretrazi_naslov("Dervis i smrt"))
biblioteka.trenutno_dostupne()
'''
#8.
class Player:
    def __init__(self, x, y, width, height, health):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._health = health

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x
    
    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y
    
    def set_width(self, width):
        self._width = width
    
    def get_width(self):
        return self._width
    
    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height
    
    def set_health(self, health):
        if health >= 0 and health <= 100:
            self._health = health
        else:
            print("Neispravan unos za atribut health.")
            return
        
    def get_health(self):
        return self._health
    

class Enemy:
    def __init__(self, x, y, width, height, damage):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._damage = damage
    
    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x
    
    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y
    
    def set_width(self, width):
        self._width = width
    
    def get_width(self):
        return self._width
    
    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height
    
    def set_damage(self, damage):
        if damage >= 0 and damage <= 100:
            self._damage = damage
        else:
            print("Neispravan unos za atribut damage.")
            return
        
    def get_damage(self):
        return self._damage
    
player1 = Player(3, 3, 5, 7, 50)
player2 = Player(4, 3, 8, 10, 78)
enemy = Enemy(2, 3, 7, 7, 38)

def check_collision(player, enemy):
    x_osa = (player.get_x() < enemy.get_x() + enemy.get_width()) and (player.get_x() + player.get_width() > enemy.get_x())
    y_osa = (player.get_y() < enemy.get_y() + enemy.get_height()) and (player.get_y() + player.get_height() > enemy.get_y())

    return x_osa and y_osa


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.set_health(player.get_health() - enemy.get_damage())
        print(f"Health nakon kolizije: {player.get_health()}")
    else:
        print("Nije doslo do promjene atributa health.")

decrease_health(player1, enemy)

#9.
class Turnir:
    def __init__(self, naziv_turnira, broj_igraca, broj_rundi):
        self.naziv_turnira = naziv_turnira
        self.broj_igraca = broj_igraca
        self.broj_rundi = broj_rundi
        self.lista_igraca = []

    def set_naziv_turnira(self, naziv_turnira):
        self.naziv_turnira = naziv_turnira

    def get_naziv_turnira(self):
        return self.naziv_turnira
    
    def set_broj_igraca(self, broj_igraca):
        self.broj_igraca = broj_igraca
    
    def get_broj_igraca(self):
        return self.broj_igraca
    
    def set_broj_rundi(self, broj_rundi):
        if broj_rundi > 0 and broj_rundi < 10:
            self.broj_rundi = broj_rundi
        else:
            return "Neispravan unos za rundu!"
        
    def get_broj_rundi(self):
        return self.broj_rundi
    
    def set_lista_igraca(self, lista_igraca):
        self.lista_igraca = lista_igraca
    
    def get_lista_igraca(self):
        return self.lista_igraca
    
    def dodaj_igraca(self, ime_igraca):
        self.lista_igraca.append(tuple(ime_igraca, 0))
        return self.lista_igraca
    
    def obrisi_igraca(self, ime_igraca):
        for igrac in self.lista_igraca:
            if igrac[0] == ime_igraca:
                self.lista_igraca.remove(igrac)

        return "Igrac se ne nalazi u listi igraca!"
        
    def prikazi_najboljeg(self):

        najbolji = max(self.lista_igraca, key=lambda x: x[1])
        return najbolji[0]
    

