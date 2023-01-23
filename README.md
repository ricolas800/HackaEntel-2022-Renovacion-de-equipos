# Renovación de equipos

El presente proyecto consiste en el desarrollo de modelos de machine learning para predecir la probabilidad de que un usuario renueve su equipo móvil en un periodo de 2 meses. El objetivo de este proyecto es determinar cuales son los factores claves que influyen en la renovación de equipos y así poder diseñar estrategias de negocio para incrementar el número de líneas renovadas.

Los datos utilizados se encuentran repartidos en 8 bases de datos diferentes, las cuales se procesaron y combinaron para formar un dataset general que contuviera la información lista para ser utilizada en el desarrollo de los distintos modelos predictivos. Este proceso se realiza en el notebook *procesamiento_dataset*.

Dado que el objetivo es predecir si una línea será renovada o no, es un problema de clasificación, por lo que se utilizarán los siguientes modelos:
* Regresión Logística
* Árboles de decisión (Random Forest)
* XGBoost

Los modelos desarrollados se guardaran en formato *.pkl*.

Se evaluará el rendimiento de cada uno de los modelos con un conjunto de prueba y se realizarán las predicciones para el mes de abril. 

Se realizará una comparación de los resultados obtenidos por cada uno de los 3 modelos y por últimmo, podremos escoger el modelo que presenta mejor rendimiento.
