# Análisis de Hashtags de Usuarios de X (Twitter)

Este script de Python utiliza la API v2 de X (Twitter) para obtener los últimos 20 tuits de un usuario específico y luego analiza los hashtags utilizados en esos tuits. Finalmente, genera un gráfico de barras horizontal que muestra los 10 hashtags más frecuentes encontrados.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente:

* **Python 3.6 o superior**
* La librería **tweepy** (para interactuar con la API de X):
    ```bash
    pip install tweepy
    ```
* La librería **re** (para expresiones regulares, usualmente incluida con Python).
* La librería **matplotlib** (para generar gráficos):
    ```bash
    pip install matplotlib
    ```
* La librería **collections** (para el contador de hashtags, usualmente incluida con Python).

## Configuración

1.  **Obtener un Bearer Token de la API v2 de X (Twitter):**
    * Dirígete al [Portal de Desarrolladores de Twitter](https://developer.twitter.com/en/portal/dashboard).
    * Crea una cuenta de desarrollador si aún no tienes una.
    * Crea un nuevo proyecto y luego una nueva aplicación.
    * En la sección de claves y tokens de tu aplicación, genera un **Bearer Token**.
    * **Reemplaza** la siguiente línea en el código con tu Bearer Token:
        ```python
        BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAG1I0gEAAAAAH8e6Pol6LhVxszzta%2FYOu%2F8muiE%3DVKIDLue3dAfwwognmYAUBUznGqKoD6tSPJ7abJ2QASrp0Fpdg4"
        ```
        **¡Importante!** Mantén tu Bearer Token seguro y no lo compartas públicamente.

## Uso

1.  **Guarda el código Python** en un archivo con extensión `.py` (por ejemplo, `analizar_hashtags.py`).
2.  **Abre una terminal o símbolo del sistema** y navega hasta el directorio donde guardaste el archivo.
3.  **Ejecuta el script** utilizando el siguiente comando:
    ```bash
    python analizar_hashtags.py
    ```
4.  El script te pedirá que **ingreses el nombre de usuario de X (sin el símbolo @)** que deseas analizar.
5.  El script intentará obtener los últimos 20 tuits de ese usuario, extraer los hashtags y mostrar los 10 hashtags más utilizados, junto con un gráfico de barras.

## Usuarios Recomendados para Probar el Código

Para asegurar que el código funcione correctamente y que se encuentren hashtags para generar el gráfico, te recomendamos utilizar los siguientes usuarios de X durante las pruebas:

* **yEoupS7LYFcs0m2**: Este usuario suele publicar contenido con hashtags variados.
* **LatinGRAMMYs**: La cuenta oficial de los Latin GRAMMYs es muy activa y utiliza hashtags relevantes a la música latina.
* **premiolonuestro**: Similar a los Latin GRAMMYs, Premios Lo Nuestro también utiliza hashtags relacionados con la música y sus premios.

Estos usuarios son buenos ejemplos porque tienden a incluir hashtags en sus publicaciones, lo que permitirá verificar que la extracción y el conteo de hashtags, así como la generación del gráfico, funcionen como se espera.

## Salida del Script

El script mostrará en la consola:

* Un mensaje indicando si la conexión con la API de X fue exitosa.
* Los últimos 20 tuits del usuario ingresado.
* Una lista de los hashtags más usados y la cantidad de veces que aparecen.
* Si se encontraron hashtags, se mostrará una ventana con un gráfico de barras horizontal representando los 10 hashtags más frecuentes.
* Si no se encontraron tuits o hashtags, se mostrará un mensaje indicándolo.

## Manejo de Errores

El script incluye manejo básico de errores para los siguientes casos:

* Fallo en la conexión con la API de X.
* No se puede obtener el ID del usuario ingresado.
* No se encuentran tuits para el usuario especificado.
* Errores al acceder a los tuits del usuario (por ejemplo, cuenta privada).
* No se encuentran hashtags en los tuits.