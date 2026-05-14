import pandas as pd

# -----------------------------------------------------------
#     Ler os Dados de Quantidade e mediana de jogadores
# -----------------------------------------------------------

df = pd.read_csv(
    r"Trabalho_Final\Dados_Jogadores.csv",
    sep=";"
)

# -------------------------------------------------------------------
#    Tratar os Dados Nulos Encontrados na mediana de jogadores
# -------------------------------------------------------------------

df_media = df.dropna(subset=["Average Players"])

# -------------------------------------------------------------------
#    converte a data para formato real de data
# -------------------------------------------------------------------

df["DateTime"] = pd.to_datetime(df["DateTime"])

# -------------------------------------------------------------------
#    cria o primeiro grafico com matplotlib
# -------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.plot(df["Players"])

plt.show()

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df_media.info())