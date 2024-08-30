# Enunciado 2: Función de Web Scrapping

## 1. Explicación de la lógica en `test2.py`

1. **Librerías**: Se importa`requests` para hacer una petición HTTP con los url y `BeautifulSoup` para analizar el contenido HTML de estas páginas web. La librería `multiprocessing` es útil para realizar web scrapping concurrente, mas no se utiliza en el código entregado.
   
2. **Petición a la página web**: La función `scrape_url` parte probando una solicitud HTTP usando `requests.get(url)`.

3. **Procesamiento del HTML**: Si la página devuelve el código 200 (OK), se usa `BeautifulSoup` para obtener el código HTML de la página y luego buscar un `div` de la clase `example-class`.

4. **Extracción de datos**: Se retorna el texto de esa `div`.

5. **Manejo de errores**: Si la petición HTTP falla o el código no es 200, se imprime la execpción o el código respectivo y se retorna `None`.

6. **Iteración secuencial**: Tras definir la función, se utiliza esta para procesar las URLs en `url_list` de forma secuencial y se imprime su resultado, en caso de no levantar un error.

## 2. Comparación web scraping secuencial y concurrente

### Web scraping secuencial:
Útil cuando:
- Cantidad de datos a extraer es razonablemente pequeña.
- Se desea evitar una sobreexigencia en el servidor por peticiones simultáneas
- Se busca una implementación más sencilla y un manejo de errores más simple.

### Web scraping concurrente:
Útil cuando:
- Hay muchas URL de las cuales extraer datos y un rendimiento eficiente es requerido.
- Se necesitan tiempos de espera menores, por lo que se realizan peticiones simultánesas.
- Los sitios web visitados tienen mucho contenido o son de lento acceso.