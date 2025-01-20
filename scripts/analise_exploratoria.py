# ################################################################
# PROJETO FINAL
#
# Universidade Federal de Sao Carlos (UFSCAR)
# Departamento de Computacao - Sorocaba (DComp-So)
# Disciplina: Aprendizado de Maquina
# Prof. Tiago A. Almeida
#
#
# Nome: Guilherme Fenrnandes Rezende Santos
# RA: 813467
# ################################################################

# Arquivo com todas as funcoes e codigos referentes a analise exploratoria

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plotar_grafico_barras(df, coluna, target):
    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=df,
        x=f"{coluna}",
        hue=f"{target}",
        order=df[f"{coluna}"].value_counts().index,
    )
    plt.xlabel(f"{coluna}")
    plt.ylabel("Frequência")
    plt.title(f"Distribuição de {coluna} por {target}")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title=f"{target}")
    plt.show()


def plotar_boxplot(df, coluna, target):
    plt.figure(figsize=(8, 8))
    sns.boxplot(x=f"{target}", y=f"{coluna}", data=df, whis=1.5)
    plt.show()


def plotar_correlacao(df):
    correlacao = df.corr()

    plt.figure(figsize=(15, 12))
    sns.heatmap(correlacao, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Matriz de Correlação")
    plt.show()
