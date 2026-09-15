# Checklist del proyecto

## FASE 1 — ESTRUCTURA Y MODELO BASE

- [x] Crear estructura inicial.
- [x] Crear CHECKLIST.md.
- [x] Crear main.py.
- [x] Crear requirements.txt.
- [x] Crear .gitignore.
- [x] Cargar Wine Dataset.
- [x] Separar X e y.
- [x] Realizar división 80/20.
- [x] Configurar random_state.
- [x] Configurar stratify.
- [x] Crear modelo max_depth=2.
- [x] Entrenar modelo.
- [x] Realizar predicciones.
- [x] Calcular precisión.
- [x] Obtener profundidad real.
- [x] Obtener número de hojas.
- [x] Generar reglas con export_text.
- [x] Ejecutar python main.py.
- [x] Comprobar que no existan errores.

### Resultado de la Fase 1

Se creó la estructura inicial con `CHECKLIST.md`, `main.py`,
`requirements.txt` y `.gitignore`.

Se implementó el modelo base con
`DecisionTreeClassifier(max_depth=2)`, utilizando una división
80/20 con `random_state=42` y `stratify=y`.

El modelo obtuvo:

- Precisión en prueba: 0.8611 (86.11 %)
- Profundidad real: 2
- Número de hojas: 4

Las reglas generadas utilizaron las características
`color_intensity`, `ash` y `flavanoids`.

El proyecto fue validado localmente mediante:

`python main.py`

Durante la primera ejecución local faltaba la dependencia
`scikit-learn`, por lo que se instalaron las dependencias
declaradas en `requirements.txt`. Después de la instalación,
el programa se ejecutó correctamente y reprodujo los resultados
esperados.

## FASE 2 — EXPERIMENTACIÓN

- [x] Ejecutar max_depth=1.
- [x] Ejecutar max_depth=2.
- [x] Ejecutar max_depth=3.
- [x] Ejecutar max_depth=4.
- [x] Ejecutar max_depth=5.
- [x] Ejecutar max_depth=None.
- [x] Registrar precisión.
- [x] Registrar profundidad real.
- [x] Registrar número de hojas.
- [x] Generar reglas de cada árbol.
- [x] Crear carpeta resultados/.
- [x] Guardar reglas de cada experimento.
- [x] Comprobar que todos los experimentos utilizan la misma división.
- [x] Comparar resultados.
- [x] Identificar profundidad real del árbol sin límite.
- [x] Verificar los archivos generados.

### Resultado de la Fase 2

Se ejecutaron los seis experimentos con `max_depth=1`, `2`, `3`, `4`, `5` y `None`. Todos reutilizaron la única división 80/20 creada antes del ciclo de entrenamiento, con `random_state=42` y `stratify=y`.

| max_depth | Profundidad real | Hojas | Precisión |
|---:|---:|---:|---:|
| 1 | 1 | 2 | 0.5833 |
| 2 | 2 | 4 | 0.8611 |
| 3 | 3 | 7 | 0.9444 |
| 4 | 4 | 8 | 0.9444 |
| 5 | 4 | 8 | 0.9444 |
| None | 4 | 8 | 0.9444 |

La profundidad real del árbol sin límite fue 4. La precisión aumentó hasta el experimento con profundidad solicitada 3 y permaneció en 0.9444 para los experimentos posteriores; los modelos con límites 4, 5 y sin límite alcanzaron 8 hojas y profundidad real 4.

Se creó `resultados/` y se generaron los seis archivos `reglas_depth_1.txt`, `reglas_depth_2.txt`, `reglas_depth_3.txt`, `reglas_depth_4.txt`, `reglas_depth_5.txt` y `reglas_depth_none.txt` mediante `export_text`. Se verificó que todos existen, contienen condiciones y clases finales. La ejecución de `python.exe main.py` terminó sin errores.

## FASE 3 — ANÁLISIS Y DOCUMENTACIÓN

- [x] Analizar resultados.
- [x] Comparar diferentes max_depth.
- [x] Analizar las reglas.
- [x] Analizar complejidad.
- [x] Analizar precisión.
- [x] Analizar posibles indicios de sobreajuste.
- [x] Analizar feature_importances_.
- [x] Identificar características importantes.
- [x] Analizar adecuación del dataset.
- [x] Proponer características adicionales.
- [x] Completar README.md.
- [x] Responder todas las preguntas solicitadas por la práctica.
- [x] Escribir conclusiones basadas en resultados reales.
- [x] Verificar consistencia entre README y ejecución.

### Resultado de la Fase 3

Se analizaron las métricas y reglas reales de los seis modelos. La precisión de prueba aumentó hasta 0.9444 con `max_depth=3` y no mejoró con árboles más complejos. Los modelos con `max_depth=4`, `5` y `None` alcanzaron la misma profundidad real de 4, 8 hojas y reglas idénticas. Según este experimento, la profundidad 3 ofreció el mejor equilibrio observado entre precisión y complejidad.

Se incorporó al programa la precisión de entrenamiento para apoyar el análisis de posibles indicios de sobreajuste. Los árboles de profundidad real 4 obtuvieron 1.0000 en entrenamiento y 0.9444 en prueba; se documentó como una señal que debe vigilarse, pero no como evidencia suficiente para afirmar sobreajuste perjudicial, porque la precisión de prueba no disminuyó.

Se calcularon las importancias mediante `feature_importances_`. En el modelo base destacaron `flavanoids` (0.4926) y `color_intensity` (0.4831). En el árbol sin límite también fueron las variables principales, con 0.4081 y 0.4002 respectivamente, seguidas por `proline` con 0.1110. Se dejó explícito que estas importancias corresponden únicamente a los modelos y condiciones de este experimento.

Se creó `README.md` con la descripción académica, dataset, metodología, explicación del clasificador, resultados, comparación de reglas, análisis de complejidad y precisión, adecuación del dataset, variables adicionales propuestas, conclusiones e instrucciones de instalación y ejecución.

La consistencia se verificó ejecutando nuevamente `main.py` y mediante comprobaciones automáticas sobre la división 142/36, las métricas, profundidades, hojas y contenido de los seis archivos de reglas. La ejecución terminó sin errores y la validación interna reportó `VALIDACION_INTERNA=OK`.

## FASE 4 — REVISIÓN FINAL

- [x] Ejecutar nuevamente python main.py.
- [x] Comprobar imports.
- [x] Comprobar requirements.txt.
- [x] Comprobar .gitignore.
- [x] Revisar estructura.
- [x] Revisar main.py.
- [x] Revisar CHECKLIST.md.
- [x] Revisar README.md.
- [x] Revisar carpeta resultados/.
- [x] Comprobar resultados documentados.
- [x] Comprobar que no existan resultados inventados.
- [x] Comprobar reproducibilidad.
- [x] Eliminar archivos temporales.
- [x] Verificar que el proyecto esté preparado para GitHub.

### Resultado de la Fase 4

Se revisaron la estructura completa, el código, los imports, `requirements.txt`, `.gitignore`, `CHECKLIST.md`, `README.md` y los seis archivos de `resultados/`. No fueron necesarias correcciones funcionales: la implementación y la documentación conservaron la metodología y los resultados reales de las fases anteriores.

La última ejecución de `main.py` terminó sin errores y reprodujo las métricas documentadas. `pip check` confirmó que no existen dependencias rotas. Una validación adicional comprobó la división 142/36, las métricas de entrenamiento y prueba, las profundidades, las hojas, la correspondencia entre modelos y archivos de reglas, y la igualdad de dos ejecuciones independientes; el resultado fue `VALIDACION_FINAL=OK`.

Se verificó que `requirements.txt` contiene únicamente `scikit-learn` y que `.gitignore` excluye cachés de Python, entornos virtuales, temporales, archivos del sistema operativo y configuraciones comunes de editores. Se eliminó el directorio temporal `__pycache__` generado durante las validaciones.
