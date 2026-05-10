import statistics

# DADOS DOS MESES DE JANEIRO A JUNHO
dados_banco = {
    "Energia (MWh)": [1200, 1250, 1180, 1300, 1270, 1250],
    "Funcionários": [86000, 86100, 86050, 86200, 86150, 86100],
    "Tecnologia (%)": [78, 80, 79, 84, 85, 80]
}

def analisar_indicadores(nome_indicador, valores):
    # FUNCÇAO QUE PROCESSA DADOS E RETORNA A ANÁLISE ESTATÍSTICA
    # CÁLCULOS ESTATÍSTICOS
    media = sum(valores) / len(valores)
    mediana = statistics.median(valores)
    
    try:
        moda = statistics.mode(valores)
    except statistics.StatisticsError:
        moda = "Não houve repetição"
        
    print(f"=== RESULTADOS: {nome_indicador} ===")
    print(f"Média Mensal: {media:.2f}")
    print(f"Mediana:      {mediana:.2f}")
    print(f"Moda:         {moda}")
    
    # EXEMPLO: SE O ÚLTIMO MÊS FOR MAIOR QUE A MÉDIA, EMITIR ALERTA
    ultimo_mes = valores[-1]
    if ultimo_mes > media:
        print(f"STATUS: ALERTA! O valor atual ({ultimo_mes}) está ACIMA da média.")
    else:
        print(f"STATUS: Normal. O valor atual ({ultimo_mes}) está dentro ou abaixo da média.")
        print("-" * 48)
    
    #EXECUÇÃO DO PROGRAMA
    print("SISTEMA DE GESTÃO DE ESTATÍSTICA -  BANCO DO BRASIL\n")
    
    for indicador, serie in dados_banco.items():
        analisar_indicadores(indicador, serie)