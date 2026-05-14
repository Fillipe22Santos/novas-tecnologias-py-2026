import pandas as pd

df = pd.read_csv(
    r"Trabalho_Final\Dados_Jogadores.csv",
    sep=";"
)

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)