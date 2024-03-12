<<<<<<< HEAD
'''2. Napisati program koji nalazi ponavljajuću sekvencu (podniz) koja u proizvodu daje najveću
vrijednost. Štampati tu sekvencu i proizvod te sekvence. Primjer: za listu [1, 2, 2, 2, 4, 4] treba da
se štampa sekvenca [4, 4] i proizvod 16.
def ponavljajuca_sekvenca_proizvod(lista):
    tren_proizvod = 1
    max_proizvod = 1
    tren_sekv = []
    max_sekv = []
   
    i=0
    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            tren_sekv.append(lista[i])
            tren_sekv.append(lista[i+1])
            tren_proizvod *= lista[i] * lista[i+1]
            i += 2
            if tren_proizvod >= max_proizvod:
                max_proizvod = tren_proizvod
                max_sekv = tren_sekv
        else:
            tren_proizvod = 1
            tren_sekv.clear()
            i += 1

    print(f"Sekvenca: {max_sekv}, proizvod: {max_proizvod}")

    ponavljajuca_sekvenca_proizvod([4, 4, 5, 5, 5])
'''

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

'''1. Napisati funkciju koja za zadati string i slovo vraća listu torki. Svaka torka se odnosi na rečenicu,
a sastoji se od svih riječi koje se završavaju sa zadatim slovom u toj rečenici, kao i broj riječi koje
se završavaju sa zadatim slovom u toj rečenici. Primjer: get_words_ends_with_letter (“Print only
the words that end with the chosen letter in those sentences. Example can contains one or more
sentences.”, “s”) vraća listu sljedećeg oblika: [(“words”, “sentences”, 2), (“contains”, “sentences”,
2)]
'''
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
=======

>>>>>>> 119eb215b0261bceddd5cf225cb85aaf339f4814
