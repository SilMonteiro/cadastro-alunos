import pandas as pd
import numpy as np
import random

def gerar_df()
    
    try:
        df = pd.read_csv('alunos.csv')
    except FileNotFoundError:
        df = pd.DataFrame(Columns=["Matricula", "Nome", "Rua", "Número", "Bairro", "Cidade", "UF", "Telefone", "e-mail"])

    return df


def salvando_dados(df):

    df.to_csv('alunos.csv', index=False)

    
def numero_matricula(df):

    if df.empty:
        return 1
    else:
        return df['Matricula'].max() + 1

