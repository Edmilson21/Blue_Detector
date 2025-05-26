import cv2
import numpy as np

# Iniciar la cámara
cap = cv2.VideoCapture(0)

"""Crear la ventana una sola vez (no se reabre en cada frame, se utiliza eso porque cuando tenemos un entorno mal configurado o 
quizás algunos tipos de IDE <Entorno de Desarrollo> como por ej: Spyder, Pycharm, Jupitrer, etc) se abren muchas ventanas
 en el bucle, por eso que se usa cv2.namedWindow, así los estaremos diciendo a opencv para crear una sola ventana.
 """
cv2.namedWindow('Detección de Azul')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertimos a HSV para detectar color azul
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    azul_bajo = np.array([100, 150, 50])
    azul_alto = np.array([130, 255, 255])
    mascara = cv2.inRange(hsv, azul_bajo, azul_alto)

    # Buscar contornos en la máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500:  # Filtrar objetos pequeños
            x, y, w, h = cv2.boundingRect(contorno)
            cx = x + w // 2
            cy = y + h // 2

            # Dibujar rectángulo verde alrededor del objeto
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Dibujar un círculo rojo en el centro
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            # Mostrar coordenadas en pantalla
            cv2.putText(frame, f'Centro: ({cx}, {cy})', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Mostrar solo UNA ventana con la imagen procesada
    cv2.imshow('Detección de Azul', frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()