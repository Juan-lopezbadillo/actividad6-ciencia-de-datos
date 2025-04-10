# actividad6-ciencia-de-datos
Solucion a los ejercicios de la actividad 6 - Ciencia de Datos con Python


## Ejercicio 5: Analisis de tuits con la API de ttwitter

Este script permite conectarse a Twittter mediante la libreria 'tweepy' y obtener los ultimos 20 tuits
de un usuario para analizar patrones de texto.

###  🛠️ Requisitos previos

1. Tener una cuenta en [Twitter] ((https://twitter.com))
2. Registrarse como desarrollador en [developer.twitter.com](https://developer.twitter.com)
3. Crear un proyecto y obtener las siguientes claves: 
    - API Key
    - API Key Secret
    - Access Token
    - Access Token Secret
4. Instalar la libreria 'tweepy':
    --- git bash ---
    pip install tweepy

### 📜 Descripción del script (`ejercicio5/ejercicio5.py`)

- Se conecta a la API de Twitter usando las claves del usuario.
- Solicita un nombre de usuario (sin `@`).
- Obtiene los últimos 20 tuits de ese usuario.
- Muestra los tuits uno por uno.
- El código está preparado para incluir análisis como:
  - Palabras más usadas
  - Hashtags frecuentes
  - Menciones
  - Detección de enlaces

### 📌 Notas

- Si el usuario tiene la cuenta privada, no se podrán leer sus tuits.
- Se recomienda usar cuentas públicas.
- El script puede extenderse para hacer análisis con librerías como `collections`, `nltk`, o `pandas`.
