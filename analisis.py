#!/usr/bin/env python3
"""Calcula el tiempo promedio por estación a partir de datos/tiempos.csv."""

import csv
from collections import defaultdict
from pathlib import Path

ARCHIVO_DATOS = Path(__file__).parent / "datos" / "tiempos.csv"


def calcular_promedio_por_estacion(ruta: Path) -> dict[str, float]:
    """Lee el CSV y devuelve el tiempo promedio (segundos) por estación."""
    tiempos_por_estacion: dict[str, list[float]] = defaultdict(list)

    with ruta.open(newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            estacion = fila["estacion"].strip()
            tiempo = float(fila["tiempo_seg"])
            tiempos_por_estacion[estacion].append(tiempo)

    return {
        estacion: sum(tiempos) / len(tiempos)
        for estacion, tiempos in sorted(tiempos_por_estacion.items())
    }


def main() -> None:
    if not ARCHIVO_DATOS.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ARCHIVO_DATOS}")

    promedios = calcular_promedio_por_estacion(ARCHIVO_DATOS)

    if not promedios:
        print("No hay registros en el archivo de datos.")
        return

    print("Tiempo promedio por estación (segundos):")
    print("-" * 40)
    for estacion, promedio in promedios.items():
        print(f"  {estacion}: {promedio:.2f} s")


if __name__ == "__main__":
    main()
