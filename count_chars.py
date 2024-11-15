texto = input()
texto=texto.lower()
texto = texto.replace(" ", "")
texto=texto.replace("?","")
letters={}
for letter in texto:
    if letter not in letters:
        letters[letter] = texto.count(letter)
print(letters)