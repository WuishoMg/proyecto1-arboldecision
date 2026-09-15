"""Experimentos de clasificación del Wine Dataset con Árboles de Decisión."""

from pathlib import Path

from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


def cargar_datos():
    """Carga el Wine Dataset y devuelve datos, clases y nombres de características."""
    wine = load_wine()
    return wine.data, wine.target, wine.feature_names


def dividir_datos(caracteristicas, clases):
    """Crea la división reproducible de entrenamiento y prueba para la práctica."""
    return train_test_split(
        caracteristicas,
        clases,
        test_size=0.20,
        random_state=42,
        stratify=clases,
    )


PROFUNDIDADES = (1, 2, 3, 4, 5, None)
DIRECTORIO_RESULTADOS = Path(__file__).resolve().parent / "resultados"


def entrenar_y_evaluar_arbol(
    caracteristicas_entrenamiento,
    caracteristicas_prueba,
    clases_entrenamiento,
    clases_prueba,
    nombres_caracteristicas,
    profundidad_maxima,
):
    """Entrena un árbol y devuelve las métricas y reglas obtenidas realmente."""
    arbol = DecisionTreeClassifier(
        max_depth=profundidad_maxima,
        random_state=42,
    )
    arbol.fit(caracteristicas_entrenamiento, clases_entrenamiento)

    precision_entrenamiento = arbol.score(
        caracteristicas_entrenamiento,
        clases_entrenamiento,
    )
    predicciones = arbol.predict(caracteristicas_prueba)
    precision = accuracy_score(clases_prueba, predicciones)
    reglas = export_text(arbol, feature_names=list(nombres_caracteristicas))

    return {
        "max_depth": profundidad_maxima,
        "precision_entrenamiento": precision_entrenamiento,
        "precision": precision,
        "profundidad_real": arbol.get_depth(),
        "numero_hojas": arbol.get_n_leaves(),
        "reglas": reglas,
        "importancias": dict(
            zip(nombres_caracteristicas, arbol.feature_importances_)
        ),
    }


def guardar_reglas(resultados):
    """Guarda en archivos de texto las reglas reales de cada experimento."""
    DIRECTORIO_RESULTADOS.mkdir(exist_ok=True)

    for resultado in resultados:
        etiqueta_profundidad = (
            "none" if resultado["max_depth"] is None else str(resultado["max_depth"])
        )
        ruta_reglas = DIRECTORIO_RESULTADOS / (
            f"reglas_depth_{etiqueta_profundidad}.txt"
        )
        ruta_reglas.write_text(resultado["reglas"], encoding="utf-8")


def mostrar_resumen(resultados):
    """Muestra una tabla con los resultados comparables de los experimentos."""
    encabezado = (
        f"{'max_depth':<11} | {'profundidad real':<16} | "
        f"{'hojas':<5} | {'precisión train':<15} | {'precisión prueba':<16}"
    )
    print(encabezado)
    print("-" * len(encabezado))

    for resultado in resultados:
        profundidad_solicitada = (
            "None" if resultado["max_depth"] is None else resultado["max_depth"]
        )
        print(
            f"{profundidad_solicitada!s:<11} | "
            f"{resultado['profundidad_real']:<16} | "
            f"{resultado['numero_hojas']:<5} | "
            f"{resultado['precision_entrenamiento']:<15.4f} | "
            f"{resultado['precision']:.4f}"
        )


def mostrar_importancias(resultados):
    """Muestra importancias no nulas del modelo base y del árbol sin límite."""
    for profundidad in (2, None):
        resultado = next(
            resultado
            for resultado in resultados
            if resultado["max_depth"] == profundidad
        )
        etiqueta = "None" if profundidad is None else str(profundidad)
        importancias = sorted(
            (
                (nombre, importancia)
                for nombre, importancia in resultado["importancias"].items()
                if importancia > 0
            ),
            key=lambda elemento: elemento[1],
            reverse=True,
        )

        print(f"\nImportancias para max_depth={etiqueta}:")
        for nombre, importancia in importancias:
            print(f"- {nombre}: {importancia:.4f}")


def main():
    """Ejecuta todos los experimentos usando una única división de los datos."""
    caracteristicas, clases, nombres_caracteristicas = cargar_datos()
    (
        caracteristicas_entrenamiento,
        caracteristicas_prueba,
        clases_entrenamiento,
        clases_prueba,
    ) = dividir_datos(caracteristicas, clases)

    resultados = []
    for profundidad_maxima in PROFUNDIDADES:
        resultado = entrenar_y_evaluar_arbol(
            caracteristicas_entrenamiento,
            caracteristicas_prueba,
            clases_entrenamiento,
            clases_prueba,
            nombres_caracteristicas,
            profundidad_maxima,
        )
        resultados.append(resultado)

    mostrar_resumen(resultados)
    mostrar_importancias(resultados)
    guardar_reglas(resultados)
    print(f"\nReglas guardadas en: {DIRECTORIO_RESULTADOS}")


if __name__ == "__main__":
    main()
