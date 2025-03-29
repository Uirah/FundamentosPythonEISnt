"""Usando as bibliotecas Pandas e MatPlotLib e um dataset (podes selecionar das aulas, fazer
download na plataforma kaggle ou escolher um dataset pessoal), elabora um notebook
jupyter no qual efetues:
- Limpeza e tratamento de dados;
- Processamento de dados: groupby, filter, criação de novas colunas,…;
- Visualização de dados;

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de estilo
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Carregar dados do arquivo Excel
df = pd.read_excel("House_Prices_Dataset.xls", engine='openpyxl')  # Se for .xlsx, pode usar 'openpyxl' ou 'xlrd'
df.head()

# Mostrar % de valores ausentes por coluna
missing_data = df.isnull().sum() / len(df) * 100
missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
missing_data.plot(kind='barh')
plt.title("Porcentagem de Valores Ausentes por Coluna")
plt.show()

# Remover colunas com muitos valores ausentes (>30%)
df.drop(['PoolQC', 'MiscFeature', 'Alley', 'Fence'], axis=1, inplace=True, errors='ignore')  # 'errors=ignore' evita erro se a coluna não existir

# Preencher valores numéricos com a mediana
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Preencher valores categóricos com a moda
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
    
# Transformar colunas categóricas em tipo 'category' (economiza memória)
for col in categorical_cols:
    df[col] = df[col].astype('category')
    
# Preço médio por tipo de zona (MSZoning)
price_by_zone = df.groupby('MSZoning')['SalePrice'].mean().sort_values(ascending=False)
print(price_by_zone)

# Tamanho médio do lote por bairro (Neighborhood)
avg_lot_by_neighborhood = df.groupby('Neighborhood')['LotArea'].mean().sort_values(ascending=False)
print(avg_lot_by_neighborhood)

# Casas com mais de 3 quartos e preço abaixo de $300k
affordable_large_houses = df[(df['BedroomAbvGr'] > 3) & (df['SalePrice'] < 300000)]
affordable_large_houses.head()

# Ano desde a última reforma
df['YearsSinceRemod'] = df['YrSold'] - df['YearRemodAdd']

# Total de área habitável (1º andar + 2º andar + porão)
df['TotalLivArea'] = df['1stFlrSF'] + df['2ndFlrSF'] + df['TotalBsmtSF'].fillna(0)

# Faixa de preço (Barato, Médio, Caro)
df['PriceRange'] = pd.cut(df['SalePrice'], bins=[0, 150000, 300000, float('inf')], labels=['Barato', 'Médio', 'Caro'])

sns.histplot(df['SalePrice'], kde=True, bins=30)
plt.title("Distribuição do Preço das Casas")
plt.show()

sns.scatterplot(data=df, x='TotalLivArea', y='SalePrice', hue='PriceRange')
plt.title("Preço vs. Área Habitável")
plt.show()

sns.boxplot(data=df, x='BedroomAbvGr', y='SalePrice')
plt.title("Preço por Número de Quartos")
plt.show()


corr_matrix = df.select_dtypes(include=['int64', 'float64']).corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix[['SalePrice']].sort_values(by='SalePrice', ascending=False), annot=True, cmap='coolwarm')
plt.title("Correlação com o Preço de Venda")
plt.show()

top_neighborhoods = df.groupby('Neighborhood')['SalePrice'].mean().sort_values(ascending=False).head(10)
top_neighborhoods.plot(kind='barh', color='skyblue')
plt.title("Top 10 Bairros Mais Caros")
plt.show()

df.to_csv("House_Prices_Processed.csv", index=False)