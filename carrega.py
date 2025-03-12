import pandas as pd
from bd import engine


dados_df = pd.read_csv("tabela-fipe-historico-precos.csv")

# Escolhe as colunas
dados_df = dados_df[["marca", "modelo", "anoModelo", "valor"]]

# Seleciona as principais Marcas
lista_modelos = ("Audi", "BMW", "BYD", "Citroën", "Ferrari","Fiat","Ford", "GM - Chevrolet", "Honda",
                 "Hyundai", "Jeep", "Mercedes-Benz", "Mitsubishi Nissan Peugeot", "Porsche", "Renault",
                 "Suzuki", "Toyota", "Volvo VW - VolksWagen")

# Filtra o DataFrame com os modelos selecionados
dados_df = dados_df[dados_df["marca"].isin(lista_modelos)]

#Renomeia as colunas para as mesmas da tabela 'veiculos'
dados_df.rename(columns={
                'anoModelo':'ano',
                'valor':'preco'}, inplace=True)

try:
    # Carrega os dados na tabela 'veiculos'
    dados_df.to_sql('veiculos',engine, if_exists='append', index=False)
    print('Dados Carregados com Sucesso!')
except:
    print('Ocorreu um erro ao carregar os dados.')