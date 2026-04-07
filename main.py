# ahorcado.py - Versión de la Cuenta B
palabra = "chile"
adivinadas = []
vidas = 5

print("¡Bienvenido al Ahorcado de Puente Alto! 🇨🇱")
print("Intenta adivinar la palabra secreta.")

while vidas > 0:
    progreso = [l if l in adivinadas else "_" for l in palabra]
    print(f"\nTu progreso: {' '.join(progreso)}")
    print(f"Letras que ya probaste: {', '.join(adivinadas)}")
    
    if "_" not in progreso:
        print("¡Excelente! ¡Ganaste el juego! 🎉")
        break
        
    letra = input("👉 ¿Qué letra quieres probar?: ").lower()
    
    if letra in adivinadas:
        print("⚠️ Ya usaste esa letra, ¡intenta con otra!")
        continue
        
    adivinadas.append(letra)
    
    if letra not in palabra:
        vidas -= 1
        print(f"❌ La letra '{letra}' no está. Te quedan {vidas} vidas.")

if vidas == 0:
    print(f"💀 ¡Oh no! Te quedaste sin vidas. La palabra era: {palabra}")
