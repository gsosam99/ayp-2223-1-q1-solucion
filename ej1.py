palabras_censuradas=["racismo", "terrorista", "peligro", "miedo", "odio"]

tweet = input("Por favor, ingrese el tweet que desea censurar: ")
character = input("Por favor, ingrese el carácter por el que desea reemplazar las letras de las palabras censuradas: ")

words = tweet.split(" ") # Tomamos el tweet y metemos cada palabra en una lista
for word in words:
  # Procedemos a limpiar las palabras que tienen , . o saltos de lineas en una nueva variable
  clean = word.replace(",", "")
  clean = clean.replace(".", "")
  clean = clean.replace("\n", "")
  if palabras_censuradas.count(clean.lower()) > 0:
    change = ""
    for letter in clean: # Por cada letra de la palabra, agregamos un caracter de censura
      change += character
    changed = word.replace(clean, change) # Aca tomamos la palabra original y cambiamos la parte limpia por lo censurado. Por ejemplo: word = "peligro," => clean = "peligro" => change = "*******". Finalmente de "peligro," reemplazar "peligro" por "*******". Resultando "*******,"
    tweet = tweet.replace(word, changed) # Luego reemplazamos la palabra original por la palabra censurada
print(tweet)
