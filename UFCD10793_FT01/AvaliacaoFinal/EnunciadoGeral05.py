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

df = pd.read_csv("House_Prices_Dataset.xls")  # Substitua pelo caminho do arquivo
df.head()