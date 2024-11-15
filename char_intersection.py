texto = input()
texto2 = input()
texto_set=set()
texto2_set=set()

for i in texto.split(" "):
    texto_set.add(i)
for i in texto2.split(" "):
    texto2_set.add(i)
a = texto_set.intersection(texto2_set)

list=[]
for i in a:
    list.append(i)

print(" ".join(list))
