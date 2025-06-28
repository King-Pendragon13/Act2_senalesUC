El código realiza lo siguiente:

Generación de señales en el dominio del tiempo: Se definen matemáticamente las señales mediante arreglos de NumPy sobre un intervalo temporal común.

Visualización temporal: Se grafican las señales originales para observar su comportamiento en función del tiempo.

Cálculo de la Transformada de Fourier: Utilizando np.fft.fft() y np.fft.fftfreq(), se obtiene el espectro de frecuencia de cada señal, separando la magnitud y la fase.

Visualización espectral: Se grafican la magnitud y la fase del espectro de frecuencia para cada señal, mostrando cómo se representa su contenido frecuencial.

Verificación de propiedades:

Linealidad: Se analiza la FFT de una combinación lineal de señales.

Desplazamiento en el tiempo: Se analiza cómo cambia el espectro al trasladar una señal.

Escalamiento en frecuencia: Se observa el efecto de modificar la frecuencia de una señal senoidal.

Este programa es una herramienta didáctica útil para visualizar conceptos fundamentales del análisis de señales y la Transformada de Fourier, permitiendo observar la correlación entre el dominio temporal y el espectro frecuencial.

