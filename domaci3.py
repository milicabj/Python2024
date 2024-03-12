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

