"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # type: ignore

def pregunta_09():
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl0["year"] = tbl0["c3"].str.split("-").str[0]
    return tbl0