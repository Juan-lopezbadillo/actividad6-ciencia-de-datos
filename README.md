# Análisis de Hashtags en X (Twitter): Un Estudio Exploratorio

## Presentado por:

**Juan Carlos Lopez Badillo**

## Para la Clase de:

**Fundamentos de la Ciencia de Datos**

## Programa:

**Ingeniería en Ciencia de Datos**

## Semestre:

**Primer Semestre**

## Institución:

**Corporación Universitaria Iberoamericana**

---

### **Introducción**

Este trabajo presenta un script de Python desarrollado para explorar y visualizar el uso de hashtags en la plataforma X (anteriormente Twitter). El objetivo principal es analizar los últimos 20 tuits de un usuario específico para identificar los hashtags más frecuentes y representarlos gráficamente. Esta actividad se enmarca dentro de los fundamentos de la ciencia de datos, aplicando técnicas de extracción, procesamiento y visualización de información textual obtenida de una fuente de datos en línea.

---

### **Objetivo Principal**

* Desarrollar una herramienta que permita extraer los hashtags utilizados en los últimos 20 tuits de un usuario de X.
* Identificar y contar la frecuencia de cada hashtag encontrado.
* Visualizar los 10 hashtags más comunes a través de un gráfico de barras horizontal.

---

### **Metodología**

El script desarrollado sigue los siguientes pasos:

1.  **Conexión a la API de X (v2):** Se establece una conexión segura con la API de X utilizando un Bearer Token.
2.  **Obtención de Datos:** Se solicita al usuario ingresar un nombre de usuario de X y se recuperan sus últimos 20 tuits, incluyendo el texto de cada tuit y sus entidades (donde se encuentran los hashtags).
3.  **Extracción de Hashtags:** Mediante el uso de expresiones regulares, se identifican y extraen todos los hashtags presentes en los tuits obtenidos.
4.  **Conteo de Frecuencia:** Se utiliza la librería `collections` para contar la ocurrencia de cada hashtag extraído.
5.  **Visualización:** Finalmente, se emplean las funcionalidades de la librería `matplotlib` para generar un gráfico de barras horizontal que muestra los 10 hashtags más frecuentes y su respectiva cantidad de uso.

---

### **Herramientas Utilizadas**

* **Python:** Lenguaje de programación principal para el desarrollo del script.
* **Tweepy:** Librería de Python para interactuar con la API de X.
* **re:** Módulo de Python para trabajar con expresiones regulares (para la extracción de hashtags).
* **Matplotlib:** Librería de Python para la creación de gráficos y visualizaciones de datos.
* **Collections:** Módulo de Python que implementa tipos de datos contenedores especializados, como `Counter` para el conteo de hashtags.

---

### **Resultados Esperados**

Al ejecutar el script e ingresar un nombre de usuario de X, se espera obtener:

* La lista de los últimos 20 tuits del usuario consultado.
* Un listado de todos los hashtags encontrados en esos tuits, junto con su frecuencia de aparición.
* Un gráfico de barras horizontal que ilustre los 10 hashtags más utilizados por el usuario en sus recientes publicaciones.

---

### **Usuarios de Prueba Recomendados**

Para garantizar la correcta funcionalidad del script y la obtención de datos relevantes para la visualización, se recomienda utilizar los siguientes usuarios de X durante las pruebas:

* **yEoupS7LYFcs0m2**
* **LatinGRAMMYs**
* **premiolonuestro**

Estos usuarios suelen emplear hashtags en sus publicaciones, lo que facilita la verificación del proceso de extracción y conteo.

---

### **Conclusiones Preliminares**

Este ejercicio práctico demuestra cómo las herramientas de programación en Python y las APIs de plataformas de redes sociales pueden utilizarse para realizar análisis exploratorios de datos textuales. La identificación y visualización de hashtags proporcionan una visión general de los temas y tendencias que un usuario determinado está discutiendo o promoviendo en sus publicaciones recientes. Este tipo de análisis puede ser fundamental en campos como el marketing digital, el análisis de tendencias y la comprensión del discurso público en línea.