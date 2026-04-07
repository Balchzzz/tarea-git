palabra_secreta = "python"
letras_adivinadas = []
intentos = 6

print("--- JUEGO DEL AHORCADO ---")

while intentos > 0:
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra
        else:
            estado += "_"
    
    print(f"\nPalabra: {estado}")
    print(f"Intentos restantes: {intentos}")
    
    if "_" not in estado:
        print("¡Ganaste!")
        break
        
    letra = input("Ingresa una letra: ").lower()
    letras_adivinadas.append(letra)
    
    if letra not in palabra_secreta:
        intentos -= 1

if intentos == 0:
    print(f"Perdiste. La palabra era: {palabra_secreta}")