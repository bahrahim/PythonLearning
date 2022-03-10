phrase = "Bonjour la famille comment allez vous ?"
print(phrase)  # affiche la valeur de la phrase Bonjour la famille...

print(phrase.count(""))  # donne le nombre de lettres et d'espaces entre les mots
print(phrase.count(" "))  # compte que le nombre d'espaces entre les mots

nombre = "1,2,3,4,5"
print(nombre.split(","))
print(",".join(nombre.split(",")))
print("-".join(nombre.split(",")))
print(" ".join(nombre.split(",")))

for i in range(5):
    print(str(i).zfill(2))  # zfill complete par des 0 aux chiffres selon le besoin
