import pandas as pd             # Utilizada para manipulação e análise de dados
import matplotlib.pyplot as plt # Utilizada para a criação de visualizações gráficas

# Criamos um dicionário com os dados extraídos dos relatórios da organização
dados_bb = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Consumo_Energia_MWh": [1200, 1250, 1180, 1300, 1270, 1250],
    "Qtd_Funcionarios": [86000, 86100, 86050, 86200, 86150, 86100],
    "Indice_Tecnologia_Perc": [78, 80, 79, 83, 85, 80]
}

# Conversão do dicionário para um objeto DataFrame do Pandas (formato de tabela)
df = pd.DataFrame(dados_bb)
# O método .mean() calcula a média aritmética simples
media_energia = df["Consumo_Energia_MWh"].mean()
# O método .median() identifica o valor central do conjunto de dados ordenado
mediana_energia = df["Consumo_Energia_MWh"].median()
# O método .mode() retorna o valor com maior frequência (moda)
moda_energia = df["Consumo_Energia_MWh"].mode()[0] # Usamos [0] pois a moda pode retornar mais de um valor (multimodal)

# Exibição dos resultados no console (saída de texto)
print("--- RELATÓRIO DE ANÁLISE ESTATÍSTICA (BB) ---")
print(f"Média de Consumo: {media_energia:.2f} MWh")
print(f"Mediana do Período: {mediana_energia} MWh")
print(f"Moda Identificada: {moda_energia} MWh")
print("-" * 45)

# Define o tamanho da moldura do gráfico (largura x altura)
plt.figure(figsize=(14, 6))

# Subplot 1: Gráfico de Linha para o Consumo de Energia
plt.subplot(1, 2, 1) # Define uma grade de 1 linha e 2 colunas, ocupando a posição 1
plt.plot(df["Mês"], df["Consumo_Energia_MWh"], marker='o', linestyle='-', color='b')
plt.title("Evolução do Consumo de Energia (MWh)")
plt.xlabel("Meses Analisados")
plt.ylabel("Consumo em MWh")
plt.grid(True, linestyle='--', alpha=0.7) # Adiciona grade para facilitar a leitura

# Subplot 2: Gráfico de Barras para Evolução Tecnológica
plt.subplot(1, 2, 2) # Ocupa a posição 2 na mesma grade
plt.bar(df["Mês"], df["Indice_Tecnologia_Perc"], color='forestgreen')
plt.title("Índice de Uso de Recursos Tecnológicos (%)")
plt.xlabel("Meses Analisados")
plt.ylabel("Percentual de Implementação")
plt.ylim(0, 100) # Define a escala do eixo Y de 0 a 100%

# Comando para ajustar o espaçamento entre os gráficos e exibir a janela
plt.tight_layout()
plt.show()