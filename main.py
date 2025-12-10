import pandas as pd
import numpy as np
import random

def gerar_df():
    
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
    

def cadastro_aluno(df):

    print("\n-> Para iniciar o cadastro do aluno, por favor preencha os campos abaixo:\n")
    dados_cadastro = {}
    dados_cadastro['nome'] = input("Digite o nome do aluno:")
    dados_cadastro['rua'] = input("Digite a rua do aluno:")
    dados_cadastro['numero'] = input("Digite o numero da casa do aluno:")
    dados_cadastro['bairro'] = input("Digite o bairro do aluno:")
    dados_cadastro['cidade'] = input("Digite a cidade do aluno:")
    dados_cadastro['uf'] = input("Digite a UF do aluno:")
    dados_cadastro['telefone'] = input("Digite o telefone do aluno:")
    dados_cadastro['email'] = input("Digite o email do aluno:")
    dados_cadastro['matricula'] = numero_matricula(df)

    novo_aluno_data = {
        'Matricula': [dados_cadastro['matricula']],
        'Nome': [dados_cadastro['nome']],
        'Rua': [dados_cadastro['rua']],
        'Número': [dados_cadastro['numero']],
        'Bairro': [dados_cadastro['bairro']],
        'Cidade': [dados_cadastro['cidade']],
        'UF': [dados_cadastro['uf']],
        'Telefone': [dados_cadastro['telefone']],
        'e-mail': [dados_cadastro['email']]
    }

    # Cria um novo DataFrame a partir dos dados do novo aluno
    df_novo_aluno = pd.DataFrame(novo_aluno_data)

    # CORREÇÃO 2: Usando pd.concat() para combinar o DataFrame existente com o novo
    df = pd.concat([df, df_novo_aluno], ignore_index=True)

    salvando_dados(df)
    print("\n-> Aluno cadastrado com sucesso!\n")
    return df

