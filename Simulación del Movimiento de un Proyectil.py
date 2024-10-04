import numpy as np
import matplotlib.pyplot as plt

# Función para simular la trayectoria del proyectil
def simular_proyectil(v0, angulo, g=9.81):
    """
    Simula el movimiento de un proyectil en 2D.
    
    :param v0: Velocidad inicial en m/s
    :param angulo: Ángulo de lanzamiento en grados
    :param g: Aceleración debida a la gravedad en m/s^2 (por defecto es 9.81 m/s^2)
    :return: Dos arrays (x, y) con las posiciones del proyectil a lo largo del tiempo
    """
    # Convertir el ángulo a radianes
    angulo_rad = np.radians(angulo)
    
    # Descomponer la velocidad inicial en componentes x e y
    v0x = v0 * np.cos(angulo_rad)
    v0y = v0 * np.sin(angulo_rad)
    
    # Tiempo total de vuelo
    t_vuelo = (2 * v0y) / g
    
    # Crear un array de tiempo desde 0 hasta el tiempo de vuelo
    t = np.linspace(0, t_vuelo, num=500)
    
    # Calcular las posiciones en x y y
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    
    return x, y

# Función para graficar la trayectoria
def graficar_proyectil(x, y):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title("Simulación del Movimiento de un Proyectil")
    plt.xlabel("Distancia horizontal (m)")
    plt.ylabel("Altura (m)")
    plt.grid(True)
    plt.show()

# Parámetros iniciales
v0 = float(input("Ingresa la velocidad inicial (m/s): "))
angulo = float(input("Ingresa el ángulo de lanzamiento (grados): "))

# Simular el movimiento del proyectil
x, y = simular_proyectil(v0, angulo)

# Graficar la trayectoria
graficar_proyectil(x, y)
