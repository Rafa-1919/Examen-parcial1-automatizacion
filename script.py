def mostrar_datos():
    nombre = "Rafael Sánchez Mora"
    comandos_favoritos = [
        "git status - Permite saber exactamente qué está pasando en el entorno de trabajo.",
        "git commit - Consolida el progreso y guarda los cambios de forma permanente.",
        "git checkout - Facilita la navegación rápida entre distintas ramas de desarrollo."
    ]
    
    print(f"Nombre: {nombre}")
    print("\nMis 3 comandos de Git favoritos:")
    for comando in comandos_favoritos:
        print(f"- {comando}")

if __name__ == "__main__":
    mostrar_datos()