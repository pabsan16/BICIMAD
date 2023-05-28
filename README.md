# BICIMAD

En este repositorio se pueden encontrar los ficheros necesarios para la práctica de BICIMAD. En la memoria subida al repositorio, se pueden ver más en detalle los diferentes pasos que hemos seguido para la implementación del código con el que resolvemos el problema elegido, así como los resultados y conclusiones que obtenemos de nuestro análisis.

**Problema a estudiar:**

Hemos decidido estudiar los años 2019 y 2020, y además lo haremos agrupando los meses en las cuatro estaciones. Esto se debe a que queremos ver las diferencias entre el año de la pandemia (2020) con el inmediatamente anterior (2019), para ver si, como sospechamos, la tasa de uso del servicio de BICIMAD se vio afectada por la situación sanitaria que atravesaba nuestro país (y el resto del mundo).

Además, en cada estación organizaremos las estaciones en orden creciente en cuanto al número de bicis que acaban teniendo, es decir, en primer lugar, las de balance negativo (las que acaban con menos bicis que con las que empezaron) y finalmente las de balance positivo (las que acaban con un mayor número de bicis que el inicial).

**Procedimiento:**

Los pasos que hemos seguido para implementar el código que nos permita analizar los datos que queremos son los siguientes:

1.	Unimos los datos de los ficheros que pertenecen a la misma estación mediante la función **union**.

2.	A través de la función **datos**, nos quedamos únicamente con los datos que nos interesan de los que aparecen en los ficheros (por ejemplo, la estación en la que se inicia el viaje y en la que se termina).

3.	Después, ordenamos las estaciones en orden creciente en cuanto al número de bicis que acaban teniendo con la función **sort** que hemos definido.

4.	Finalmente, mostramos por pantalla las listas de las estaciones (organizadas en estaciones) ya ordenadas.

Para ejecutar los años 2019 y 2020, es necesario tener descargados los archivos correspondientes a cada mes del año en unas carpetas que hemos llamado Datos_2019 y Datos_2020, las cuales se deben encontrar en la misma carpeta que el archivo Python. Los ficheros, que adjuntamos en el repositorio dentro de las carpetas previamente mencionadas, se obtienen de la página oficial de BICIMAD, y los hemos renombrado para simplificar el proceso como “mes.json”.


