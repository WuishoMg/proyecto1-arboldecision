# Clasificación del Wine Dataset con Árboles de Decisión

## Descripción general

Este proyecto es una práctica universitaria de Inteligencia Artificial para la carrera de Ingeniería en Sistemas Computacionales. Su propósito es clasificar muestras de vino mediante un Árbol de Decisión y estudiar las reglas que el modelo aprende automáticamente a partir de los datos.

El ejercicio utiliza aprendizaje automático supervisado: cada muestra posee una clase conocida durante el entrenamiento y el modelo aprende a predecir la clase de muestras nuevas. Aunque el árbol expresa su decisión mediante reglas condicionales interpretables, estas reglas no fueron programadas manualmente, por lo que el ejercicio no debe describirse como IA simbólica pura.

## Objetivo

- Entrenar y evaluar un clasificador de Árbol de Decisión.
- Comprender cómo se generan reglas del tipo “si condición, entonces decisión”.
- Comparar modelos con diferentes valores de `max_depth`.
- Relacionar la complejidad del árbol con su precisión e interpretabilidad.
- Identificar las características que más participaron en las decisiones de los modelos entrenados.

## Wine Dataset

Los datos se cargan directamente con `sklearn.datasets.load_wine`; no se descarga ningún archivo externo.

| Propiedad | Valor |
|---|---:|
| Muestras | 178 |
| Características de entrada | 13 |
| Clases | 3 |
| Valores de la clase | 0, 1 y 2 |
| Valores faltantes | Ninguno |

Las variables de entrada se almacenan en `X = wine.data`. Son 13 mediciones químicas numéricas cuyos nombres originales son:

- `alcohol`
- `malic_acid`
- `ash`
- `alcalinity_of_ash`
- `magnesium`
- `total_phenols`
- `flavanoids`
- `nonflavanoid_phenols`
- `proanthocyanins`
- `color_intensity`
- `hue`
- `od280/od315_of_diluted_wines`
- `proline`

La variable objetivo se almacena en `y = wine.target` y representa las clases `0`, `1` y `2`, denominadas `class_0`, `class_1` y `class_2` por scikit-learn. Las muestras proceden de análisis químicos de vinos de una misma región de Italia producidos por tres cultivadores diferentes.

## ¿Qué es un Árbol de Decisión?

Un Árbol de Decisión es un modelo que divide los datos mediante preguntas sucesivas sobre sus características. Cada nodo interno contiene una condición, cada rama representa el resultado de esa condición y cada hoja asigna una clase final.

Durante el entrenamiento, `DecisionTreeClassifier` selecciona automáticamente las características y los umbrales que permiten separar las clases. Después, una muestra nueva recorre las condiciones desde la raíz hasta llegar a una hoja con la predicción.

El parámetro `max_depth` limita cuántos niveles puede desarrollar el árbol. Una profundidad pequeña produce reglas más breves, pero puede ser insuficiente para representar los patrones de los datos. Una profundidad mayor permite reglas más específicas, aunque incrementa la complejidad y puede ajustar en exceso los datos de entrenamiento.

## Metodología experimental

Se utilizó una sola división con 80 % de los datos para entrenamiento y 20 % para prueba. El resultado fue de 142 muestras de entrenamiento y 36 de prueba.

La división se creó con `random_state=42` para hacerla reproducible y `stratify=y` para conservar aproximadamente la distribución de las clases. Se generó una sola vez y se reutilizó en todos los modelos. De este modo, la variable principal que cambió entre experimentos fue `max_depth`.

Se entrenaron árboles con profundidades máximas solicitadas de `1`, `2`, `3`, `4`, `5` y `None`. Cada modelo se entrenó exclusivamente con los datos de entrenamiento y se evaluó con los mismos datos de prueba. Además de la precisión, se registraron la profundidad real, el número de hojas y las reglas obtenidas mediante `export_text`.

## Resultados

Los siguientes valores proceden de la ejecución real de `python main.py`:

| `max_depth` | Profundidad real | Hojas | Precisión de entrenamiento | Precisión de prueba |
|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 0.6620 | 0.5833 |
| 2 | 2 | 4 | 0.9366 | 0.8611 |
| 3 | 3 | 7 | 0.9930 | 0.9444 |
| 4 | 4 | 8 | 1.0000 | 0.9444 |
| 5 | 4 | 8 | 1.0000 | 0.9444 |
| `None` | 4 | 8 | 1.0000 | 0.9444 |

### Modelo inicial: `max_depth=2`

El modelo inicial alcanzó una precisión de prueba de **0.8611 (86.11 %)**, profundidad real de 2 y 4 hojas. Sus reglas emplearon `color_intensity` en la raíz y después `ash` o `flavanoids`. Es un árbol compacto y fácil de explicar, pero su precisión fue menor que la de los modelos a partir de profundidad 3.

### Comparación de profundidades y reglas

Con `max_depth=1`, el árbol solo utilizó `color_intensity`, produjo dos hojas y obtuvo la precisión más baja. Con profundidad 2 incorporó `ash` y `flavanoids`, y la precisión aumentó de 0.5833 a 0.8611.

Con profundidad 3 aparecieron también `od280/od315_of_diluted_wines`, `alcalinity_of_ash` y `proline`. El modelo alcanzó 7 hojas y una precisión de prueba de 0.9444. Con profundidad 4 se agregó una condición sobre `malic_acid` y el árbol llegó a 8 hojas, pero la precisión de prueba permaneció en 0.9444.

Los modelos con `max_depth=4`, `max_depth=5` y `max_depth=None` generaron la misma estructura y las mismas reglas. Esto ocurrió porque, con estos datos de entrenamiento y esta configuración, el árbol dejó de crecer naturalmente al alcanzar profundidad 4. Por tanto, el árbol sin límite no alcanzó una profundidad teórica o supuesta: su profundidad real medida fue **4**.

Frente al modelo inicial, el árbol sin límite duplicó el número de hojas, pasó de profundidad 2 a 4, utilizó siete características en lugar de tres y mejoró la precisión de prueba de 0.8611 a 0.9444. A cambio, sus reglas son más extensas y requieren seguir más condiciones, por lo que resulta menos sencillo de interpretar.

### Posibles indicios de sobreajuste

Los modelos de profundidad real 4 alcanzaron precisión perfecta en entrenamiento y 0.9444 en prueba. El ajuste perfecto del entrenamiento y la condición adicional que no mejoró la precisión de prueba son señales que conviene vigilar. Sin embargo, la precisión de prueba no disminuyó respecto al árbol de profundidad 3, por lo que estos resultados no permiten afirmar que exista un sobreajuste perjudicial.

Con la división utilizada, `max_depth=3` ofrece el mejor equilibrio observado: empata en la mayor precisión de prueba con los árboles más complejos, pero utiliza una profundidad y una hoja menos. Esta conclusión pertenece a este experimento concreto; una sola división train/test no demuestra que sea universalmente la mejor configuración.

## Importancia de las características

Las importancias se obtuvieron mediante `feature_importances_`. Un valor mayor indica que la característica tuvo más participación en las reducciones de impureza realizadas por ese árbol.

### Modelo inicial (`max_depth=2`)

| Característica | Importancia |
|---|---:|
| `flavanoids` | 0.4926 |
| `color_intensity` | 0.4831 |
| `ash` | 0.0243 |

### Árbol sin límite (`max_depth=None`)

| Característica | Importancia |
|---|---:|
| `flavanoids` | 0.4081 |
| `color_intensity` | 0.4002 |
| `proline` | 0.1110 |
| `od280/od315_of_diluted_wines` | 0.0210 |
| `alcalinity_of_ash` | 0.0209 |
| `ash` | 0.0202 |
| `malic_acid` | 0.0187 |

`flavanoids` y `color_intensity` parecen fundamentales para estos modelos porque concentran las importancias más altas y aparecen cerca de la parte superior de las reglas. `proline` también tuvo una participación relevante en el árbol más profundo. Estas importancias describen únicamente los modelos obtenidos con esta división y configuración; no representan una verdad universal sobre todos los vinos ni demuestran relaciones causales.

## Adecuación del dataset

Sí, el Wine Dataset cumple los requisitos necesarios para esta práctica de clasificación con Árboles de Decisión. Tiene una variable objetivo categórica conocida, características numéricas utilizables por el clasificador, ejemplos de las tres clases y ningún valor faltante. Además, su tamaño permite entrenar y evaluar rápidamente varios árboles y examinar sus reglas.

Esta adecuación debe entenderse dentro del propósito académico. Las 178 muestras constituyen un conjunto pequeño, procedente de una región y un contexto concretos, por lo que no bastan para asegurar que el modelo generalice a cualquier vino del mundo.

Para ampliar un estudio posterior podrían incorporarse mediciones como pH, acidez volátil, azúcar residual, densidad y sulfatos, porque complementarían la composición química disponible. También podrían añadirse añada, condiciones climáticas, suelo y proceso de fermentación o envejecimiento para estudiar factores ambientales y de producción. Estas variables deberían recopilarse de forma consistente y sin introducir información que revele directamente la clase objetivo.

## Conclusiones

El experimento muestra que aumentar la profundidad de 1 a 3 permitió representar mejor las separaciones entre las tres clases y elevó la precisión de prueba de 0.5833 a 0.9444. Continuar hasta profundidad 4 aumentó ligeramente la complejidad, pero no produjo una mejora adicional en prueba.

El modelo con `max_depth=2` es especialmente sencillo de interpretar, mientras que el modelo con profundidad 3 consiguió el mejor equilibrio observado entre precisión y complejidad. El árbol sin límite alcanzó por sí mismo profundidad 4 y no aportó mayor precisión que el de profundidad 3. En todos los casos, las reglas y las importancias se aprendieron de los datos; no fueron definidas manualmente.

## Estructura del proyecto

- `main.py`: ejecuta los experimentos y muestra las métricas e importancias.
- `resultados/`: contiene las reglas reales exportadas para cada profundidad.
- `CHECKLIST.md`: registra las tareas y validaciones completadas por fase.
- `requirements.txt`: declara la dependencia necesaria.

## Instalación y ejecución

Se recomienda crear un entorno virtual:

```bash
python -m venv .venv
```

En Windows, puede activarse con:

```powershell
.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instalar la dependencia:

```bash
python -m pip install -r requirements.txt
```

Ejecutar el proyecto:

```bash
python main.py
```

La ejecución muestra la tabla de experimentos y las importancias analizadas, y vuelve a generar los archivos de reglas dentro de `resultados/` a partir de los modelos entrenados realmente.
