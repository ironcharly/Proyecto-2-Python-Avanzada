# Proyecto-2-Python-Avanzada
Proyecto de la Upso - Bahurlet Micaela - Domé Florencia - Spinetta Carlos

## Diagrama de flujo del menú

![Diagrama de Flujo del Menú](https://github.com/ironcharly/Proyecto-2-Python-Avanzada/blob/d2270c4cf878d4612c1f3500b9c91eac3f3ed5c6/Dieagrama%20de%20flujo%20Menu.jpg)
# CONCLUSIONES

## ¿Cuál fue el desempeño del modelo?
El desempeño del modelo con los datos de prueba (Test) nos dio un R-cuadrado de aprox. 0.68 . Esto significa que nuestro modelo puede explicar más o menos el 68% de la variación del precio de una casa usando solo las 3 variables que determinamos. No es un modelo perfecto, pero genera más seguridad que el azar.

Esto significa que nuestro modelo es capaz de explicar el 68% de la variabilidad en el precio de las casas utilizando únicamente las 3 variables seleccionadas (RM, LSTAT, PTRATIO).

## ¿Qué variable fue la más influyente según los coeficientes del modelo?
A través del análisis de .coef_, podemos deducir que:

La variable RM (número de habitaciones) tuvo el coeficiente positivo más alto (aprox [4.5]). Esto indica que, por cada habitación extra, el precio de la casa aumenta significativamente.

La variable LSTAT (% de población de bajos ingresos) tuvo un coeficiente negativo considerable (aprox [-0.6]). Esto confirma que a mayor índice de pobreza en la zona, el valor de la propiedad tiende a disminuir.

Podríamos decir entonces que, la variable más influyente positivamente es el número de habitaciones (RM), mientras que el factor que más impacta negativamente es el nivel socioeconómico de la zona (LSTAT).

## ¿Las features extraídas del dataset fueron buenas predictoras? o sugieren otras?
Sí, las variables que seleccionamos (RM, LSTAT, PTRATIO) fueron buenas predictoras.

Mostraron una fuerte correlación en el mapa de calor previo y permitieron al modelo alcanzar un rendimiento superior al 60%.

Sin embargo, creemos que para intentar subir ese porcentaje, se podría incorporar otras variables del dataset que descartamos inicialmente pero que también tenían correlación, como:

INDUS (Proporción de hectáreas comerciales no minoristas por ciudad).

TAX (Tasa de impuestos a la propiedad). Agregar estas variables podría ayudar al modelo a captar matices que ahora se le están escapando.

Comparativa de resultados de evaluación del modelo con los datos de Entrenamiento y de Test
El puntaje de Entrenamiento (68%) y el de Test (63%) fueron relativamente similares. Eso es muy bueno, ya que significa que el modelo es "honesto" y confiable: no se aprendió de memoria los datos de práctica, sino que aprendió la relación real.
