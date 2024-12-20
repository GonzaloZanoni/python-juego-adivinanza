import pandas as pd


def centimetros_a_pulgadas(cm):
    return cm / 2.54


# leer el excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna al data frame que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Pulgadas"] = df["Centimetros"].apply(centimetros_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print(
    "Conversion completada y guardada en un nuevo archivo llamado 'mueble_medidas_convertidas.xlsx'"
)
