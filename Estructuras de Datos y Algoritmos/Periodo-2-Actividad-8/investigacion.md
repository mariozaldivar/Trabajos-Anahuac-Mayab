# Los algoritmos en la solución de problemas del pasado y del presente

## Problema 1 (antiguo): Censos en EE. UU. de 1880–1890

El gobierno estadounidense necesitaba contar y clasificar los datos de toda la población para repartir escaños en el congreso. Este problema llevaba existiendo desde 1790, cuando tuvo lugar el primer censo, pero se volvió aún más crítico en 1880, cuando procesar 50 millones de pesronas tomó entre 7 y 8 años. La principal dificultad era que el volumen de datos era enorme, y cada clasificación nueva obligaba a revisar todo otra vez.
A esto se sumaban los errores humanos y los costos altos, y se estimaba que el censo de 1890 tardaría más de 10 años. La solución llegó en 1890 con Herman Hollerith, que registró los datos en tarjetas perforadas y los procesó con máquinas tabuladoras y clasificadoras. Así, el conteo preliminar estuvo listo en seis semanas y se ahorraron unos 5 millones de dólares.

Relación con los algoritmos

Básico: Inserción. Es lo que hace una persona con un mazo de tarjetas. Sirve para lotes pequeños, pero es O(n²).
Avanzado: Radix Sort LSD. Es exactamente lo que hacían las clasificadoras de Hollerith e IBM: una pasada por dígito y 10 casillas. Con llaves cortas (edad, código de estado) es casi lineal.
Tabla hash: llave = (estado, sexo, edad) y valor = contador. Basta leer cada tarjeta una sola vez para obtener los conteos por categoría. También sirve para encontrar a una persona por su folio en O(1).
Ventajas y desventajas: Inserción es simple pero lenta con millones de registros. Radix es muy rápido, pero solo funciona con llaves numéricas cortas. La tabla hash localiza y cuenta rápido, pero no ordena.
Mejor opción: Radix Sort + tabla hash de contadores. Los datos son códigos cortos y el objetivo eran conteos por categoría. Históricamente, fue la solución que funcionó.

---

## Problema 2 (moderno): Consultas en bases de datos (PostgreSQL)

Las empresas y organizaciones actuales necesitan buscar, ordenar y cruzar millones de registros (pedidos, clientes, transacciones) en cuestión de milisegundos. Este problema existe desde las primeras bases de datos de los años 60 y la aparición del modelo relacional de Edgar F. Codd en 1970, pero se volvió mucho más grande con la llegada de internet y el _big data_. Hoy lo enfrentan tiendas en línea, bancos, gobiernos, redes sociales y los administradores de bases de datos. La principal dificultad es que los datos ya no caben en la memoria RAM y el disco es mucho más lento. Además, miles de usuarios hacen consultas al mismo tiempo, y cada consulta puede ser distinta. Originalmente, la información se guardaba en archivos secuenciales en cinta magnética: para encontrar un registro había que leer todo desde el inicio, y para actualizar se fusionaban archivos ya ordenados. Con el tiempo surgieron los índices, que permitieron localizar datos sin recorrer todo el archivo.

**Relación con los algoritmos (evidencia real)**

- **Básico:** _Inserción_. No sirve como algoritmo principal, pero **TimSort** (el ordenamiento por defecto de Python y Java) la usa para ordenar tramos pequeños antes de fusionarlos.
- **Avanzado:** PostgreSQL usa **Quicksort** cuando los datos caben en memoria y **Merge Sort externo** cuando no. Esto se ve en `EXPLAIN ANALYZE` como `Sort Method: quicksort` o `external merge`.
- **Tabla hash:** PostgreSQL tiene **índices hash** (`CREATE INDEX ... USING HASH`) para búsquedas con `=` en O(1). También usa **Hash Join**: construye una tabla hash con la tabla pequeña y la consulta con cada fila de la grande.
- **Ventajas y desventajas:** Quicksort es el más rápido en RAM, pero no sirve si los datos no caben. Merge Sort funciona con datos en disco, pero usa memoria extra. La tabla hash es la más rápida para buscar, pero solo funciona con igualdad (`=`): no sirve para rangos ni para ordenar.
- **Mejor opción:** una **combinación**: tabla hash para localizar por llave exacta, y Quicksort o Merge Sort externo para ordenar, según la memoria disponible. Es lo que hace PostgreSQL automáticamente.

---

## Fuentes

- IBM – _The punched card tabulator_: https://ibm.com/history/punched-card-tabulator
- Smithsonian – _Herman Hollerith's Tabulating Machine_: https://www.smithsonianmag.com/smithsonian-institution/herman-holleriths-tabulating-machine-2504989
- Knuth, _The Art of Computer Programming, Vol. 3_ (extracto): https://ed-thelen.org/comp-hist/Knuth-Sort.html
- Ken Shirriff – _Inside card sorters_: https://righto.com/2016/05
- PostgreSQL – _Hash Indexes_: https://www.postgresql.org/docs/current/hash-index.html
- CYBERTEC – _Join strategies in PostgreSQL_: https://www.cybertec-postgresql.com/en/?p=18872
- depesz – _Understanding work_mem_: https://www.depesz.com/?p=2218
- GeeksforGeeks – _TimSort_: https://www.geeksforgeeks.org/dsa/timsort/
