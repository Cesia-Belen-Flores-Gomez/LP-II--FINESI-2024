frase = input("Introduce una frase: ")

vocal = input("Introduce una vocal: ")

contador = frase.lower().count(vocal.lower())

print(f"La vocal '{vocal}' aparece {contador} veces en la frase.")
