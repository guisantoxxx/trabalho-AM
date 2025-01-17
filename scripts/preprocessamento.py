# ################################################################
# PROJETO FINAL
#
# Universidade Federal de Sao Carlos (UFSCAR)
# Departamento de Computacao - Sorocaba (DComp-So)
# Disciplina: Aprendizado de Maquina
# Prof. Tiago A. Almeida
#
#
# Nome: Guilherme Fernandes Rezende Santos
# RA: 813467
# ################################################################

# Arquivo com todas as funcoes e codigos referentes ao preprocessamento

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def converter_numeric(df, coluna):
    df[f"{coluna}"] = pd.to_numeric(df[f"{coluna}"], errors="coerce")


def identifica_outliners(df, colunas):

    # Criar uma cópia do DataFrame sem NaN nas colunas especificadas, para poder calcular Q1,Q3 e IQR
    df_not_nan = df.dropna(subset=colunas)

    Q1 = df_not_nan[colunas].quantile(0.25)
    Q3 = df_not_nan[colunas].quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    # Insere todas as amostrar que possuem outliners no df_aux
    outliners = (
        (df_not_nan[colunas] < limite_inferior)
        | (df_not_nan[colunas] > limite_superior)
    ).any(axis=1)

    return outliners


def fill_na_media(df, coluna):
    return df[coluna].fillna(df[f"{coluna}"].mean())


def fill_na_mediana(df, coluna):
    return df[coluna].fillna(df[f"{coluna}"].median())


def substituir(df, coluna, valor_original, valor_novo):
    x = df[f"{coluna}"] == valor_original

    df.loc[x, f"{coluna}"] = valor_novo
