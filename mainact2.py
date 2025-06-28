import numpy as np
import matplotlib.pyplot as plt

# --- Definición del tiempo ---
t = np.linspace(-1, 1, 1000)

# --- Señales en el dominio del tiempo ---
# Pulso rectangular
rect = np.where(np.abs(t) <= 0.2, 1, 0)

# Escalón unitario
step = np.where(t >= 0, 1, 0)

# Señal senoidal
f = 5  # Frecuencia en Hz
sine = np.sin(2 * np.pi * f * t)

# --- Visualización en el dominio del tiempo ---
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, rect)
plt.title("Pulso Rectangular")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, step)
plt.title("Escalón Unitario")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, sine)
plt.title("Señal Senoidal")
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Función para graficar la FFT ---
def plot_fft(signal, t, title):
    N = len(signal)
    T = t[1] - t[0]
    fft_signal = np.fft.fft(signal)
    freq = np.fft.fftfreq(N, T)
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(freq, np.abs(fft_signal))
    plt.title(f"Magnitud de {title}")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(freq, np.angle(fft_signal))
    plt.title(f"Fase de {title}")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# --- Transformada de Fourier de cada señal ---
plot_fft(rect, t, "Pulso Rectangular")
plot_fft(step, t, "Escalón Unitario")
plot_fft(sine, t, "Señal Senoidal")

# --- Verificación de Propiedades ---
# Linealidad: combinación lineal de señales
combinada = 0.5 * rect + 0.5 * sine
plot_fft(combinada, t, "Combinación Lineal")

# Desplazamiento en el tiempo
rect_shifted = np.where(np.abs(t - 0.3) <= 0.2, 1, 0)
plot_fft(rect_shifted, t, "Pulso Rectangular Desplazado")

# Escalamiento en frecuencia
sine_scaled = np.sin(2 * np.pi * 10 * t)  # frecuencia aumentada
plot_fft(sine_scaled, t, "Senoidal de Mayor Frecuencia")
